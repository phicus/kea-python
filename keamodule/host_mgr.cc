#include "keamodule.h"

using namespace std;
using namespace isc::dhcp;
using namespace isc::asiolink;
using namespace isc::util;

extern "C" {

// need BaseHostDataSource

static PyObject *
HostMgr_add(HostMgrObject *self, PyObject *args) {
    HostObject *host;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALTERNATE_SOURCES;

    if (!PyArg_ParseTuple(args, "O!|i", &HostType, &host, &target)) {
        return (0);
    }

    try {
        self->mgr->add(host->ptr, target);
        Py_RETURN_NONE;
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
HostMgr_get4(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    const char *ip_address = 0;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALL_SOURCES;

    if (!PyArg_ParseTuple(args, "ks|i", &subnet_id, &ip_address, &target)) {
        return NULL;
    }

    try {
        ConstHostPtr host;
        host = self->mgr->get4(subnet_id, IOAddress(ip_address), target);
        if (!host.get()) {
            Py_RETURN_NONE;
        }
        return Host_from_constptr(host);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
HostMgr_get4Any(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    const char *identifier_type = 0;
    const char *identifier = 0;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALL_SOURCES;

    if (!PyArg_ParseTuple(
            args, "kss|i", &subnet_id, &identifier_type, &identifier, &target)) {
        return NULL;
    }

    try {
        ConstHostPtr host;
        std::vector<uint8_t> binary = str::quotedStringToBinary(identifier);
        if (binary.empty()) {
            str::decodeFormattedHexString(identifier, binary);
        }
        host = self->mgr->get4Any(
            subnet_id,
            Host::getIdentifierType(identifier_type),
            &binary.front(),
            binary.size(),
            target);
        if (!host.get()) {
            Py_RETURN_NONE;
        }
        return Host_from_constptr(host);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
HostMgr_get(HostMgrObject *self, PyObject *args) {
    if (PyTuple_Size(args) >= 3 && PyUnicode_Check(PyTuple_GetItem(args, 2))) {
        return HostMgr_get4Any(self, args);
    } else {
        return HostMgr_get4(self, args);
    }
}

static PyObject *
collection_to_list(ConstHostCollection &hosts) {
    PyObject *result = PyList_New(hosts.size());
    if (result == 0) {
        return 0;
    }
    int pos = 0;
    for (auto host : hosts) {
        PyObject *pyhost = Host_from_constptr(host);
        if (pyhost == 0) {
            Py_DECREF(result);
            return (0);
        }
        if (PyList_SetItem(result, pos++, pyhost) < 0) {
            Py_DECREF(result);
            return (0);
        }
    }
    return (result);
}

static PyObject *
HostMgr_getAll4(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALL_SOURCES;

    if (!PyArg_ParseTuple(args, "k|i", &subnet_id, &target)) {
        return NULL;
    }

    try {
        ConstHostCollection hosts = self->mgr->getAll4(subnet_id, target);
        return (collection_to_list(hosts));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return NULL;
    }
}

static PyObject *
HostMgr_getPage4(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    unsigned long source_index = 0;
    uint64_t lower_host_id = 0;
    unsigned long page_size = 0;

    if (!PyArg_ParseTuple(args, "kkKk", &subnet_id, &source_index, &lower_host_id, &page_size)) {
        return NULL;
    }

    try {
        HostPageSize host_page_size(page_size);
        ConstHostCollection hosts = self->mgr->getPage4(subnet_id, source_index, lower_host_id, host_page_size);
        PyObject *host_list = collection_to_list(hosts);
        if (host_list == 0) {
            return (0);
        }
        PyObject *result = Py_BuildValue("Ok", host_list, source_index);
        Py_DECREF(host_list);
        return (result);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
HostMgr_del_(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    const char *ip_address;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALTERNATE_SOURCES;

    if (!PyArg_ParseTuple(args, "ks|i", &subnet_id, &ip_address, &target)) {
        return (0);
    }

    try {
        if (self->mgr->del(subnet_id, IOAddress(ip_address), target)) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
HostMgr_del4(HostMgrObject *self, PyObject *args) {
    unsigned long subnet_id;
    const char *identifier_type;
    const char *identifier;
    HostMgrOperationTarget target = HostMgrOperationTarget::ALTERNATE_SOURCES;

    if (!PyArg_ParseTuple(args, "kss|i", &subnet_id, &identifier_type, &identifier, &target)) {
        return NULL;
    }

    try {
        std::vector<uint8_t> binary = str::quotedStringToBinary(identifier);
        if (binary.empty()) {
            str::decodeFormattedHexString(identifier, binary);
        }
        if (self->mgr->del4(subnet_id, Host::getIdentifierType(identifier_type), &binary.front(), binary.size(), target)) {
            Py_RETURN_TRUE;
        } else {
            Py_RETURN_FALSE;
        }
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return NULL;
    }
}

PyObject *
HostMgr_from_ptr(HostMgr *mgr) {
    HostMgrObject *self = PyObject_New(HostMgrObject, &HostMgrType);
    if (self) {
        self->mgr = mgr;
    }
    return (PyObject *)self;
}

static PyObject *
HostMgr_instance(HostMgrObject *self, PyObject *args) {
    Py_INCREF(self);
    return (PyObject *)self;
}

static PyMethodDef HostMgr_methods[] = {
    // clang-format off
    {"instance", (PyCFunction) HostMgr_instance, METH_NOARGS,
     "Returns a sole instance of the HostMgr."},
    {"add", (PyCFunction) HostMgr_add, METH_VARARGS,
     "Adds a new host to the alternate data source."},
    {"get", (PyCFunction) HostMgr_get, METH_VARARGS,
     "Returns a host connected to the IPv4 subnet."},
    {"get4", (PyCFunction) HostMgr_get4, METH_VARARGS,
     "Returns a host connected to the IPv4 subnet by address."},
    {"get4Any", (PyCFunction) HostMgr_get4Any, METH_VARARGS,
     "Returns a host connected to the IPv4 subnet by (subnet4-id, identifier)."},
    {"getAll4", (PyCFunction) HostMgr_getAll4, METH_VARARGS,
     "Return all hosts in a DHCPv4 subnet."},
    {"getPage4", (PyCFunction) HostMgr_getPage4, METH_VARARGS,
     "Returns range of hosts in a DHCPv4 subnet."},
    {"del_", (PyCFunction) HostMgr_del_, METH_VARARGS,
     "Attempts to delete a host by address."},
    {"del4", (PyCFunction) HostMgr_del4, METH_VARARGS,
     "Attempts to delete a host by (subnet4-id, identifier, identifier-type)."},
    {NULL, NULL, 0, NULL}  // Sentinel
}; // clang-format off

static void
HostMgr_dealloc(HostMgrObject *self) {
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
HostMgr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    static HostMgrObject *instance = NULL;
    static char *kwlist[] = {NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", kwlist)) {
        PyErr_SetString(PyExc_TypeError, "kea.HostMgr() takes no arguments");
        return NULL;
    }

    if (instance == NULL) {
        instance = (HostMgrObject *)type->tp_alloc(type, 0);
        if (instance == NULL) {
            return PyErr_NoMemory();
        }

        try {
            instance->mgr = &HostMgr::instance();
        } catch (const std::exception &e) {
            Py_DECREF(instance);
            instance = NULL;
            PyErr_SetString(PyExc_RuntimeError, e.what());
            return NULL;
        }

        // Py_INCREF(instance);
    }

    Py_INCREF(instance);
    return (PyObject *)instance;
}

PyTypeObject HostMgrType = { // clang-format off
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "kea.HostMgr",
    .tp_basicsize = sizeof(HostMgrObject),
    .tp_dealloc = (destructor) HostMgr_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("Kea HostMgr singleton object"),
    .tp_methods = HostMgr_methods,
    .tp_new = HostMgr_new
};  // clang-format on

int
HostMgr_define() {
    if (PyType_Ready(&HostMgrType) < 0) {
        return (1);
    }
    Py_INCREF(&HostMgrType);
    if (PyModule_AddObject(kea_module, "HostMgr", (PyObject *)&HostMgrType) < 0) {
        Py_DECREF(&HostMgrType);
        return (1);
    }

    return (0);
}
}
