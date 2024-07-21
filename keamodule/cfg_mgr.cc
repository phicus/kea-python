#include <dhcpsrv/cfgmgr.h>

#include "keamodule.h"

using namespace std;
using namespace isc::dhcp;

extern "C" {

static PyObject *
CfgMgr_instance(CfgMgrObject *Py_UNUSED(self), PyObject *Py_UNUSED(args)) {
    static CfgMgrObject *cfg_mgr_obj = NULL;

    if (cfg_mgr_obj == NULL) {
        cfg_mgr_obj = (CfgMgrObject *)CfgMgrType.tp_alloc(&CfgMgrType, 0);
        if (cfg_mgr_obj == NULL) {
            return PyErr_NoMemory();
        }
        try {
            cfg_mgr_obj->cfg_mgr = &CfgMgr::instance();
        } catch (const std::exception &e) {
            Py_DECREF(cfg_mgr_obj);
            cfg_mgr_obj = NULL;
            PyErr_SetString(PyExc_RuntimeError, e.what());
            return NULL;
        }
    }

    Py_INCREF(cfg_mgr_obj);
    return (PyObject *)cfg_mgr_obj;
}

static PyObject *
CfgMgr_getDataDir(CfgMgrObject *self, PyObject *Py_UNUSED(args)) {
    const char *datadir = const_cast<char *>(self->cfg_mgr->getDataDir().get().c_str());

    return PyUnicode_FromString(datadir);
}

static PyObject *
CfgMgr_setDataDir(CfgMgrObject *self, PyObject *args) {
    const char *datadir;
    int unspecified = 1;

    if (!PyArg_ParseTuple(args, "s|i", &datadir, &unspecified)) {
        return NULL;
    }

    self->cfg_mgr->setDataDir(std::string(datadir), unspecified);

    Py_RETURN_NONE;
}

static PyObject *
CfgMgr_getCurrentCfg(CfgMgrObject *self, PyObject *args) {
    try {
        SrvConfigPtr ptr = self->cfg_mgr->getCurrentCfg();
        return (SrvConfig_from_ptr(ptr));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return NULL;
    }
}

static PyObject *
CfgMgr_getStagingCfg(CfgMgrObject *self, PyObject *args) {
    try {
        SrvConfigPtr ptr = self->cfg_mgr->getStagingCfg();
        return (SrvConfig_from_ptr(ptr));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return NULL;
    }
}

PyDoc_STRVAR(CfgMgr_instance_doc,
             "Returns a single instance of Configuration Manager\n\n"
             "CfgMgr.instance() is a singleton.");

PyDoc_STRVAR(CfgMgr_getDataDir_doc,
             "Returns path do the data directory\n\n"
             "This method returns a path to writable directory that DHCP servers can store data in.");

PyDoc_STRVAR(CfgMgr_setDataDir_doc,
             "Sets new data directory.");

PyDoc_STRVAR(CfgMgr_getCurrentCfg_doc,
             "Returns the current configuration.\n\n"
             "This function returns pointer to the current configuration. If the current configuration "
             "is not set it will create a default configuration and return it.");

PyDoc_STRVAR(CfgMgr_getStagingCfg_doc,
             "Returns the staging configuration.\n\n"
             "The staging configuration is used by the configuration parsers to create new configuration. "
             "The staging configuration doesn't affect the server's operation until it is committed. "
             "The staging configuration is a non-const object which can be modified by the caller.");

static PyMethodDef CfgMgr_methods[] = {
    // clang-format off
    {"instance", (PyCFunction)CfgMgr_instance, METH_NOARGS | METH_STATIC,
     CfgMgr_instance_doc},
    {"getDataDir", (PyCFunction)CfgMgr_getDataDir, METH_NOARGS,
     CfgMgr_getDataDir_doc},
    {"setDataDir", (PyCFunction)CfgMgr_setDataDir, METH_VARARGS,
     CfgMgr_setDataDir_doc},
    {"getCurrentCfg", (PyCFunction)CfgMgr_getCurrentCfg, METH_NOARGS,
     CfgMgr_getCurrentCfg_doc},
    {"getStagingCfg", (PyCFunction)CfgMgr_getStagingCfg, METH_NOARGS,
     CfgMgr_getStagingCfg_doc},
    {NULL, NULL, 0, NULL}  // Sentinel
};  // clang-format on

static void
CfgMgr_dealloc(CfgMgrObject *self) {
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyObject *
CfgMgr_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    static CfgMgrObject *instance = NULL;
    static char *kwlist[] = {NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", kwlist)) {
        PyErr_SetString(PyExc_TypeError, "kea.CfgMgr() takes no arguments");
        return NULL;
    }

    if (instance == NULL) {
        instance = (CfgMgrObject *)CfgMgr_instance(instance, args);
    }

    Py_INCREF(instance);
    return (PyObject *)instance;
}

PyTypeObject CfgMgrType = {  // clang-format off
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "kea.CfgMgr",
    .tp_basicsize = sizeof(CfgMgrObject),
    .tp_dealloc = (destructor) CfgMgr_dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = PyDoc_STR("Kea CfgMgr singleton object"),
    .tp_methods = CfgMgr_methods,
    .tp_new = CfgMgr_new
};  // clang-format on

int
CfgMgr_registerType(PyObject *mod, const char *name) {
    if (PyType_Ready(&CfgMgrType) < 0) {
        return -1;
    }
    Py_INCREF(&CfgMgrType);
    if (PyModule_AddObject(mod, name, (PyObject *)&CfgMgrType) < 0) {
        Py_DECREF(&CfgMgrType);
        return -1;
    }

    return 0;
}
}
