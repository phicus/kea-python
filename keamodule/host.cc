#include "keamodule.h"

using namespace std;
using namespace isc::dhcp;
using namespace isc::asiolink;
using namespace isc::data;

extern "C" {

static PyObject *
Host_getHostId(HostObject *self, PyObject *args) {
    try {
        HostID host_id = (self->is_const ? self->const_ptr : self->ptr)->getHostId();
        return (PyLong_FromUnsignedLongLong(host_id));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Host_toElement(HostObject *self, PyObject *args) {
    try {
        ElementPtr ptr = (self->is_const ? self->const_ptr : self->ptr)->toElement4();
        return (element_to_object(ptr));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return NULL;
    }
}

static PyObject *
Host_getIdentifier(HostObject *self, PyObject *args) {
    return PyUnicode_FromString((self->is_const ? self->const_ptr : self->ptr)->toText().c_str());
}

static PyMethodDef Host_methods[] = {
    // clang-format off
    {"getHostId", (PyCFunction) Host_getHostId, METH_NOARGS,
     "Returns Host ID (primary key in MySQL, PostgreSQL and Cassandra backends)."},
    {"toElement", (PyCFunction) Host_toElement, METH_NOARGS,
     "Element representation of the host."},
    {"getIdentifier", (PyCFunction) Host_getIdentifier, METH_NOARGS,
     "Host::getIdentifier()"},
    {NULL, NULL, 0, NULL}  // Sentinel
};  // clang-format on

static PyObject *
Host_use_count(HostObject *self, void *closure) {
    return (PyLong_FromLong(self->is_const ? self->const_ptr.use_count() : self->ptr.use_count()));
}

static PyGetSetDef Host_getsetters[] = {
    {(char *)"use_count", (getter)Host_use_count, (setter)0, (char *)"shared_ptr use count", 0},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static void
Host_dealloc(HostObject *self) {
    self->ptr.~HostPtr();
    self->const_ptr.~ConstHostPtr();
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
Host_str(HostObject *self) {
    return PyUnicode_FromString((self->is_const ? self->const_ptr : self->ptr)->toText().c_str());
}

static int
Host_init(HostObject *self, PyObject *args, PyObject *kwds) {
    static const char *kwlist[] = {"identifier", "identifier_type", "subnet_id", "ipv4_reservation", NULL};
    const char *identifier;
    const char *identifier_type;
    unsigned long subnet_id;
    const char *ipv4_reservation;

    new (&self->ptr) HostPtr;
    new (&self->const_ptr) ConstHostPtr;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "ssks", (char **)kwlist,
                                     &identifier, &identifier_type, &subnet_id, &ipv4_reservation)) {
        return -1;
    }

    try {
        self->ptr.reset(new Host(identifier, identifier_type, subnet_id, 0, IOAddress(string(ipv4_reservation))));
        self->const_ptr.reset();
        self->is_const = false;
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return -1;
    }

    return 0;
}

static PyObject *
Host_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    HostObject *self;
    self = (HostObject *)type->tp_alloc(type, 0);
    if (self) {
        new (&self->ptr) HostPtr;
        new (&self->const_ptr) ConstHostPtr;
    }
    return ((PyObject *)self);
}

PyTypeObject HostType = {  // clang-format off
    PyVarObject_HEAD_INIT(NULL, 0).tp_name = "kea.Host",
    .tp_basicsize = sizeof(HostObject),
    .tp_dealloc = (destructor) Host_dealloc,
    .tp_str = (reprfunc) Host_str,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("Kea server Host"),
    .tp_methods = Host_methods,
    .tp_getset = Host_getsetters,
    .tp_init = (initproc) Host_init,
    .tp_alloc = PyType_GenericAlloc,
    .tp_new = Host_new
};  // clang-format on

PyObject *
Host_from_ptr(HostPtr host) {
    HostObject *self = PyObject_New(HostObject, &HostType);
    if (self) {
        new (&self->ptr) HostPtr;
        new (&self->const_ptr) ConstHostPtr;
        self->is_const = false;
        self->ptr = host;
    }
    return (PyObject *)self;
}

PyObject *
Host_from_constptr(ConstHostPtr host) {
    HostObject *self = PyObject_New(HostObject, &HostType);
    if (self) {
        new (&self->ptr) HostPtr;
        new (&self->const_ptr) ConstHostPtr;
        self->is_const = true;
        self->const_ptr = host;
    }
    return (PyObject *)self;
}

int
Host_registerType(PyObject *mod, const char *name) {
    if (PyType_Ready(&HostType) < 0) {
        return -1;
    }
    Py_INCREF(&HostType);
    if (PyModule_AddObject(mod, name, (PyObject *)&HostType) < 0) {
        Py_DECREF(&HostType);
        return -1;
    }

    return 0;
}
}
