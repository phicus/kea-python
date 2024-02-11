# Kea Python
Develop Kea hooks in Python.

This project integrates a Python3 interpreter into Kea, offering a lightweight interface to a selection of Kea classes. This enables the development of hooks in Python. The Python module 'kea' is designed to mirror the API of the Kea classes as closely as possible, ensuring a familiar experience for users.

## Installation

Clone the kea-python project, compile it, and install it:
```
$ git clone https://github.com/phicus/kea-python.git
$ cd kea-python
$ autoreconf --install --force
$ make
$ sudo make install
```

## Loading the kea-python hook
To load this hook into kea you will need a `hook-libraries` section in kea config that looks something
like the following:

```jsonc
        "hooks-libraries": [{
            "library": "/usr/lib/kea/hooks/libdhcp_python.so",
            "parameters": {
                "libpython": "libpython3.8.so",
                "module": "/usr/local/lib/kea/keahook.py"
            }
        }],
```

## Acknowledgements

This project has benefited from the development, contributions and resources provided by the following:

- [invite-networks/kea_python](https://github.com/invite-networks/kea_python)

- [davejohncole/kea_python](https://github.com/davejohncole/kea_python)