#include <process/daemon.h>

#include "keamodule.h"

using namespace std;

extern "C" {

PyObject *kea_module;

static PyObject *
kea__loggerInit(PyObject *self, PyObject *args) {
    char *logger_name;

    if (!PyArg_ParseTuple(args, "s", &logger_name)) {
        return NULL;
    }

    isc::process::Daemon::setDefaultLoggerName(logger_name);
    isc::process::Daemon::loggerInit(logger_name, true);
    Py_RETURN_NONE;
}

static PyMethodDef kea_methods[] = {
    {"_loggerInit", (PyCFunction)kea__loggerInit, METH_VARARGS, "Init logger for test propouses."},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static PyModuleDef kea_module_def = {
    PyModuleDef_HEAD_INIT,
    "kea",
    0,
    -1,
    kea_methods};

PyMODINIT_FUNC
PyInit_kea(void) {
    kea_module = PyModule_Create(&kea_module_def);
    if (kea_module == NULL) {
        return NULL;
    }

    if (PyModule_AddStringConstant(kea_module, "__version__", MODULE_VERSION) < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (PyModule_AddStringConstant(kea_module, "KEA_VERSION", VERSION) < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Constants_registerTypes(kea_module) < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Capsule_registerTypes(kea_module) < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (LibraryHandle_registerType(kea_module, "LibraryHandle") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (CalloutManager_registerType(kea_module, "CalloutManager") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (CalloutHandle_registerType(kea_module, "CalloutHandle") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Lease4_registerType(kea_module, "Lease4") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Pkt4_registerType(kea_module, "Pkt4") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Option_registerType(kea_module, "Option") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (CfgMgr_registerType(kea_module, "CfgMgr") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (SrvConfig_registerType(kea_module, "SrvConfig") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (CfgSubnets4_registerType(kea_module, "CfgSubnets4") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Subnet4_registerType(kea_module, "Subnet4") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (LeaseMgr_registerType(kea_module, "LeaseMgr") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (Host_registerType(kea_module, "Host") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (HostMgr_registerType(kea_module, "HostMgr") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    if (HostReservationParser4_registerType(kea_module, "HostReservationParser4") < 0) {
        Py_DECREF(kea_module);
        return NULL;
    }

    return (kea_module);
}
}
