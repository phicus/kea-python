#include "keamodule.h"

using namespace std;
using namespace isc::hooks;
using namespace isc::dhcp;
using namespace isc::asiolink;

extern "C" {

static PyObject *
Pkt4_getType(Pkt4Object *self, PyObject *args) {
    try {
        uint8_t type = self->ptr->getType();
        return (PyLong_FromLong(type));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setType(Pkt4Object *self, PyObject *args) {
    unsigned char type;

    if (!PyArg_ParseTuple(args, "b", &type)) {
        return (0);
    }

    try {
        self->ptr->setType(type);
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getFlags(Pkt4Object *self, PyObject *args) {
    try {
        uint16_t flags = self->ptr->getFlags();
        return (PyLong_FromLong(flags));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setFlags(Pkt4Object *self, PyObject *args) {
    uint16_t flags;

    if (!PyArg_ParseTuple(args, "H", &flags)) {
        return (0);
    }

    try {
        self->ptr->setFlags(flags);
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getLocalAddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getLocalAddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setLocalAddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setLocalAddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getRemoteAddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getRemoteAddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setRemoteAddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setRemoteAddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getCiaddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getCiaddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setCiaddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setCiaddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getGiaddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getGiaddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setGiaddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setGiaddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getSiaddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getSiaddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setSiaddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setSiaddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getYiaddr(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->getYiaddr().toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setYiaddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        self->ptr->setYiaddr(IOAddress(string(addr)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getHWAddr(Pkt4Object *self, PyObject *args) {
    try {
        string hwaddr = self->ptr->getHWAddr()->toText(false);
        return (PyUnicode_FromString(hwaddr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_setHWAddr(Pkt4Object *self, PyObject *args) {
    char *addr;

    if (!PyArg_ParseTuple(args, "s", &addr)) {
        return (0);
    }

    try {
        HWAddr hw = HWAddr::fromText(addr);
        self->ptr->setHWAddr(HWAddrPtr(new HWAddr(hw)));
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_delOption(Pkt4Object *self, PyObject *args) {
    unsigned short type;

    if (!PyArg_ParseTuple(args, "H", &type)) {
        return (0);
    }

    try {
        bool res = self->ptr->delOption(type);
        return (PyBool_FromLong(res));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_addOption(Pkt4Object *self, PyObject *args) {
    PyObject *opt;

    if (!PyArg_ParseTuple(args, "O!", &OptionType, &opt)) {
        return (0);
    }

    try {
        self->ptr->addOption(((OptionObject *)opt)->ptr);
        Py_INCREF(self);
        return ((PyObject *)self);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getOption(Pkt4Object *self, PyObject *args) {
    unsigned short type;

    if (!PyArg_ParseTuple(args, "H", &type)) {
        return (0);
    }

    try {
        OptionPtr ptr = self->ptr->getOption(type);
        if (!ptr) {
            Py_RETURN_NONE;
        }
        return (Option_from_handle(ptr));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_getOptions(Pkt4Object *self) {
    try {
        PyObject *options = PyList_New(0);

        if (!self->ptr->options_.empty()) {
            for (isc::dhcp::OptionCollection::const_iterator opt = self->ptr->options_.begin();
                 opt != self->ptr->options_.end(); ++opt) {
                PyList_Append(options, PyLong_FromUnsignedLong(opt->second->getType()));
            }
        } else {
            Py_RETURN_NONE;
        }
        return (options);
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_toText(Pkt4Object *self, PyObject *args) {
    try {
        string addr = self->ptr->toText();
        return (PyUnicode_FromString(addr.c_str()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_pack(Pkt4Object *self, PyObject *args) {
    try {
        self->ptr->pack();
        return (PyBytes_FromStringAndSize((char *)self->ptr->getBuffer().getData(), self->ptr->getBuffer().getLength()));
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyObject *
Pkt4_unpack(Pkt4Object *self, PyObject *args) {
    try {
        self->ptr->unpack();
        Py_RETURN_NONE;
    } catch (const exception &e) {
        PyErr_SetString(PyExc_TypeError, e.what());
        return (0);
    }
}

static PyMethodDef Pkt4_methods[] = {
    {"getType", (PyCFunction)Pkt4_getType, METH_NOARGS,
     "For packets without DHCP Message Type option, it returns DHCP_NOTYPE (0)."},
    {"setType", (PyCFunction)Pkt4_setType, METH_VARARGS,
     "Sets DHCP message type."},
    {"getFlags", (PyCFunction)Pkt4_getFlags, METH_NOARGS,
     "Returns flags field."},
    {"setFlags", (PyCFunction)Pkt4_setFlags, METH_VARARGS,
     "Sets flags field."},
    {"getLocalAddr", (PyCFunction)Pkt4_getLocalAddr, METH_NOARGS,
     "Returns local IP address."},
    {"setLocalAddr", (PyCFunction)Pkt4_setLocalAddr, METH_VARARGS,
     "Sets local IP address."},
    {"getRemoteAddr", (PyCFunction)Pkt4_getRemoteAddr, METH_NOARGS,
     "Returns remote IP address."},
    {"setRemoteAddr", (PyCFunction)Pkt4_setRemoteAddr, METH_VARARGS,
     "Sets remote IP address."},
    {"getCiaddr", (PyCFunction)Pkt4_getCiaddr, METH_NOARGS,
     "Returns ciaddr field."},
    {"setCiaddr", (PyCFunction)Pkt4_setCiaddr, METH_VARARGS,
     "Sets ciaddr field."},
    {"getGiaddr", (PyCFunction)Pkt4_getGiaddr, METH_NOARGS,
     "Returns giaddr field."},
    {"setGiaddr", (PyCFunction)Pkt4_setGiaddr, METH_VARARGS,
     "Sets giaddr field."},
    {"getSiaddr", (PyCFunction)Pkt4_getSiaddr, METH_NOARGS,
     "Returns siaddr field."},
    {"setSiaddr", (PyCFunction)Pkt4_setSiaddr, METH_VARARGS,
     "Sets siaddr field."},
    {"getYiaddr", (PyCFunction)Pkt4_getYiaddr, METH_NOARGS,
     "Returns yiaddr field."},
    {"setYiaddr", (PyCFunction)Pkt4_setYiaddr, METH_VARARGS,
     "Sets yiaddr field."},
    {"getHWAddr", (PyCFunction)Pkt4_getHWAddr, METH_NOARGS,
     "Returns hardware address."},
    {"setHWAddr", (PyCFunction)Pkt4_setHWAddr, METH_VARARGS,
     "Sets hardware address."},
    {"delOption", (PyCFunction)Pkt4_delOption, METH_VARARGS,
     "Attempts to delete first suboption of requested type."},
    {"addOption", (PyCFunction)Pkt4_addOption, METH_VARARGS,
     "Adds an option to this packet."},
    {"getOption", (PyCFunction)Pkt4_getOption, METH_VARARGS,
     "Returns the first option of specified type."},
    {"getOptions", (PyCFunction)Pkt4_getOptions, METH_NOARGS,
     "Returns a list of all of the options."},
    {"toText", (PyCFunction)Pkt4_toText, METH_NOARGS,
     "Returns text representation of the packet."},
    {"pack", (PyCFunction)Pkt4_pack, METH_NOARGS,
     "Prepares on-wire format of DHCPv4 packet."},
    {"unpack", (PyCFunction)Pkt4_unpack, METH_NOARGS,
     "Parses on-wire form of DHCPv4 packet."},
    {0}  // Sentinel
};

static PyObject *
Pkt4_use_count(Pkt4Object *self, void *closure) {
    return (PyLong_FromLong(self->ptr.use_count()));
}

static PyGetSetDef Pkt4_getsetters[] = {
    {(char *)"use_count", (getter)Pkt4_use_count, (setter)0, (char *)"shared_ptr use count", 0},
    {0}  // Sentinel
};

static void
Pkt4_dealloc(Pkt4Object *self) {
    self->ptr.~Pkt4Ptr();
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static int
Pkt4_init(Pkt4Object *self, PyObject *args, PyObject *kwds) {
    unsigned char msg_type;
    unsigned long transid;
    PyObject *data;

    new (&self->ptr) Pkt4Ptr;

    if (kwds != 0) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments are not supported");
        return (-1);
    }

    if (PyTuple_Size(args) == 1) {
        if (!PyArg_ParseTuple(args, "S", &data)) {
            return (-1);
        }
        uint8_t *buff;
        Py_ssize_t len;
        PyBytes_AsStringAndSize(data, (char **)&buff, &len);

        self->ptr.reset(new Pkt4(buff, len));
    } else {
        if (!PyArg_ParseTuple(args, "bk", &msg_type, &transid)) {
            return (-1);
        }

        self->ptr.reset(new Pkt4(msg_type, transid));
    }

    return (0);
}

static PyObject *
Pkt4_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    Pkt4Object *self;
    self = (Pkt4Object *)type->tp_alloc(type, 0);
    if (self) {
        new (&self->ptr) Pkt4Ptr;
    }
    return ((PyObject *)self);
}

PyTypeObject Pkt4Type = {
    PyObject_HEAD_INIT(0) "kea.Pkt4",  // tp_name
    sizeof(Pkt4Object),                // tp_basicsize
    0,                                 // tp_itemsize
    (destructor)Pkt4_dealloc,          // tp_dealloc
    0,                                 // tp_vectorcall_offset
    0,                                 // tp_getattr
    0,                                 // tp_setattr
    0,                                 // tp_as_async
    0,                                 // tp_repr
    0,                                 // tp_as_number
    0,                                 // tp_as_sequence
    0,                                 // tp_as_mapping
    0,                                 // tp_hash
    0,                                 // tp_call
    0,                                 // tp_str
    0,                                 // tp_getattro
    0,                                 // tp_setattro
    0,                                 // tp_as_buffer
    Py_TPFLAGS_DEFAULT,                // tp_flags
    "Kea server Pkt4",                 // tp_doc
    0,                                 // tp_traverse
    0,                                 // tp_clear
    0,                                 // tp_richcompare
    0,                                 // tp_weaklistoffset
    0,                                 // tp_iter
    0,                                 // tp_iternext
    Pkt4_methods,                      // tp_methods
    0,                                 // tp_members
    Pkt4_getsetters,                   // tp_getset
    0,                                 // tp_base
    0,                                 // tp_dict
    0,                                 // tp_descr_get
    0,                                 // tp_descr_set
    0,                                 // tp_dictoffset
    (initproc)Pkt4_init,               // tp_init
    PyType_GenericAlloc,               // tp_alloc
    Pkt4_new                           // tp_new
};

PyObject *
Pkt4_from_handle(Pkt4Ptr &ptr) {
    Pkt4Object *self = PyObject_New(Pkt4Object, &Pkt4Type);
    if (self) {
        new (&self->ptr) Pkt4Ptr;
        self->ptr = ptr;
    }
    return (PyObject *)self;
}

int
Pkt4_registerType(PyObject *mod, const char *name) {
    if (PyType_Ready(&Pkt4Type) < 0) {
        return -1;
    }
    Py_INCREF(&Pkt4Type);
    if (PyModule_AddObject(mod, name, (PyObject *)&Pkt4Type) < 0) {
        Py_DECREF(&Pkt4Type);
        return -1;
    }

    return 0;
}
}
