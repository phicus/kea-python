#include "keamodule.h"

using namespace std;
using namespace isc::hooks;
using namespace isc::dhcp;
using namespace isc::data;

extern "C" {

static PyObject *
Lease4_setContext(Lease4Object *self, PyObject *args) {
    PyObject *ctx;

    if (!PyArg_ParseTuple(args, "O", &ctx)) {
        return (0);
    }

    try {
        self->ptr->setContext(object_to_element(ctx));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Lease4_getContext(Lease4Object *self, PyObject *args) {
    try {
        return (element_to_object(self->ptr->getContext()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Lease4_toElement(Lease4Object *self, PyObject *args) {
    try {
        if (!self->ptr->hwaddr_) {
            // avoid assertion error in shared_ptr
            PyErr_SetString(PyExc_RuntimeError, "hwaddr must not be empty");
            return (0);
        }
        ElementPtr ptr = self->ptr->toElement();
        return (element_to_object(ptr));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyMethodDef Lease4_methods[] = {
    {"setContext", (PyCFunction)Lease4_setContext, METH_VARARGS,
     "Sets user context."},
    {"getContext", (PyCFunction)Lease4_getContext, METH_NOARGS,
     "Returns user context."},
    {"toElement", (PyCFunction)Lease4_toElement, METH_NOARGS,
     "Return the JSON representation of a lease."},
    {0}  // Sentinel
};

static PyObject *
Lease4_use_count(Lease4Object *self, void *closure) {
    return (PyLong_FromLong(self->ptr.use_count()));
}

static PyObject *
Lease4_get_addr(Lease4Object *self, void *closure) {
    try {
        string addr = self->ptr->addr_.toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_addr(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_string_value(value, "addr", false)) {
        return (1);
    }
    try {
        const char *addr = PyUnicode_AsUTF8(value);
        self->ptr->addr_ = isc::asiolink::IOAddress(string(addr));
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_valid_lft(Lease4Object *self, void *closure) {
    try {
        return (PyLong_FromLong(self->ptr->valid_lft_));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_valid_lft(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_long_value(value, "valid_lft")) {
        return (1);
    }
    try {
        self->ptr->valid_lft_ = PyLong_AsLong(value);
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_cltt(Lease4Object *self, void *closure) {
    try {
        return (PyLong_FromLong(self->ptr->cltt_));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_cltt(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_long_value(value, "cltt")) {
        return (1);
    }
    try {
        self->ptr->cltt_ = PyLong_AsLong(value);
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_subnet_id(Lease4Object *self, void *closure) {
    try {
        return (PyLong_FromLong(self->ptr->subnet_id_));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_subnet_id(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_long_value(value, "subnet_id")) {
        return (1);
    }
    try {
        self->ptr->subnet_id_ = PyLong_AsLong(value);
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_hostname(Lease4Object *self, void *closure) {
    try {
        if (self->ptr->hostname_.empty()) {
            Py_RETURN_NONE;
        }
        return (PyUnicode_FromString(self->ptr->hostname_.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_hostname(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_string_value(value, "hostname", true)) {
        return (1);
    }
    try {
        if (value == Py_None) {
            self->ptr->hostname_.clear();
        } else {
            self->ptr->hostname_ = PyUnicode_AsUTF8(value);
            boost::algorithm::to_lower(self->ptr->hostname_);
        }
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_fqdn_fwd(Lease4Object *self, void *closure) {
    try {
        if (self->ptr->fqdn_fwd_) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_fqdn_fwd(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_bool_value(value, "fqdn_fwd")) {
        return (1);
    }
    try {
        self->ptr->fqdn_fwd_ = value == Py_True;
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_fqdn_rev(Lease4Object *self, void *closure) {
    try {
        if (self->ptr->fqdn_rev_) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_FALSE;
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_fqdn_rev(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_bool_value(value, "fqdn_rev")) {
        return (1);
    }
    try {
        self->ptr->fqdn_rev_ = value == Py_True;
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_hwaddr(Lease4Object *self, void *closure) {
    try {
        if (!self->ptr->hwaddr_) {
            Py_RETURN_NONE;
        }
        string hwaddr = self->ptr->hwaddr_->toText(false);
        return (PyUnicode_FromString(hwaddr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_hwaddr(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_string_value(value, "hwaddr", false)) {
        return (1);
    }
    try {
        HWAddr hw = HWAddr::fromText(PyUnicode_AsUTF8(value));
        self->ptr->hwaddr_ = HWAddrPtr(new HWAddr(hw));
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_client_id(Lease4Object *self, void *closure) {
    try {
        if (!self->ptr->client_id_) {
            Py_RETURN_NONE;
        }
        return (PyUnicode_FromString(self->ptr->client_id_->toText().c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_client_id(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_string_value(value, "client_id", true)) {
        return (1);
    }
    try {
        if (value == Py_None) {
            self->ptr->client_id_.reset();
        } else {
            self->ptr->client_id_ = ClientId::fromText(PyUnicode_AsUTF8(value));
        }
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyObject *
Lease4_get_state(Lease4Object *self, void *closure) {
    try {
        return (PyLong_FromLong(self->ptr->state_));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static int
Lease4_set_state(Lease4Object *self, PyObject *value, void *closure) {
    if (assert_long_value(value, "state")) {
        return (1);
    }
    try {
        self->ptr->state_ = PyLong_AsLong(value);
        return (0);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (-1);
    }
}

static PyGetSetDef Lease4_getsetters[] = {
    {(char *)"use_count", (getter)Lease4_use_count, (setter)0, (char *)"shared_ptr use count", 0},
    {(char *)"addr", (getter)Lease4_get_addr, (setter)Lease4_set_addr, (char *)"Address in string form", 0},
    {(char *)"valid_lft", (getter)Lease4_get_valid_lft, (setter)Lease4_set_valid_lft, (char *)"Valid lifetime", 0},
    {(char *)"cltt", (getter)Lease4_get_cltt, (setter)Lease4_set_cltt, (char *)"Client last transmission time", 0},
    {(char *)"subnet_id", (getter)Lease4_get_subnet_id, (setter)Lease4_set_subnet_id, (char *)"Subnet identifier", 0},
    {(char *)"hostname", (getter)Lease4_get_hostname, (setter)Lease4_set_hostname, (char *)"Client hostname", 0},
    {(char *)"fqdn_fwd", (getter)Lease4_get_fqdn_fwd, (setter)Lease4_set_fqdn_fwd, (char *)"Forward zone updated?", 0},
    {(char *)"fqdn_rev", (getter)Lease4_get_fqdn_rev, (setter)Lease4_set_fqdn_rev, (char *)"Reverse zone updated?", 0},
    {(char *)"hwaddr", (getter)Lease4_get_hwaddr, (setter)Lease4_set_hwaddr, (char *)"Client's MAC/hardware address", 0},
    {(char *)"client_id", (getter)Lease4_get_client_id, (setter)Lease4_set_client_id, (char *)"Client identifier", 0},
    {(char *)"state", (getter)Lease4_get_state, (setter)Lease4_set_state, (char *)"Holds the lease state(s)", 0},
    {0}  // Sentinel
};

static void
Lease4_dealloc(Lease4Object *self) {
    self->ptr.~Lease4Ptr();
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static int
Lease4_init(Lease4Object *self, PyObject *args, PyObject *kwds) {
    new (&self->ptr) Lease4Ptr;

    if (kwds != 0) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments are not supported");
        return (-1);
    }
    if (!PyArg_ParseTuple(args, "")) {
        return (-1);
    }
    self->ptr = Lease4Ptr(new Lease4());

    return (0);
}

static PyObject *
Lease4_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    Lease4Object *self;
    self = (Lease4Object *)type->tp_alloc(type, 0);
    if (self) {
        new (&self->ptr) Lease4Ptr;
    }
    return ((PyObject *)self);
}

PyTypeObject Lease4Type = {
    PyObject_HEAD_INIT(0) "kea.Lease4",  // tp_name
    sizeof(Lease4Object),                // tp_basicsize
    0,                                   // tp_itemsize
    (destructor)Lease4_dealloc,          // tp_dealloc
    0,                                   // tp_vectorcall_offset
    0,                                   // tp_getattr
    0,                                   // tp_setattr
    0,                                   // tp_as_async
    0,                                   // tp_repr
    0,                                   // tp_as_number
    0,                                   // tp_as_sequence
    0,                                   // tp_as_mapping
    0,                                   // tp_hash
    0,                                   // tp_call
    0,                                   // tp_str
    0,                                   // tp_getattro
    0,                                   // tp_setattro
    0,                                   // tp_as_buffer
    Py_TPFLAGS_DEFAULT,                  // tp_flags
    "Kea server Lease4",                 // tp_doc
    0,                                   // tp_traverse
    0,                                   // tp_clear
    0,                                   // tp_richcompare
    0,                                   // tp_weaklistoffset
    0,                                   // tp_iter
    0,                                   // tp_iternext
    Lease4_methods,                      // tp_methods
    0,                                   // tp_members
    Lease4_getsetters,                   // tp_getset
    0,                                   // tp_base
    0,                                   // tp_dict
    0,                                   // tp_descr_get
    0,                                   // tp_descr_set
    0,                                   // tp_dictoffset
    (initproc)Lease4_init,               // tp_init
    PyType_GenericAlloc,                 // tp_alloc
    Lease4_new                           // tp_new
};

PyObject *
Lease4_from_handle(Lease4Ptr &ptr) {
    Lease4Object *self = PyObject_New(Lease4Object, &Lease4Type);
    if (self) {
        new (&self->ptr) Lease4Ptr;
        self->ptr = ptr;
    }
    return (PyObject *)self;
}

int
Lease4_registerType(PyObject *mod, const char *name) {
    if (PyType_Ready(&Lease4Type) < 0) {
        return -1;
    }
    Py_INCREF(&Lease4Type);
    if (PyModule_AddObject(mod, name, (PyObject *)&Lease4Type) < 0) {
        Py_DECREF(&Lease4Type);
        return -1;
    }

    return 0;
}
}
