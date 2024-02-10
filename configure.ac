#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_INIT(kea_python, 1.1)

AM_INIT_AUTOMAKE(foreign)

AC_CONFIG_MACRO_DIR([m4macros])

# Libtool configuration
#
LT_INIT

# Let's check for a C++ compiler
AC_LANG(C++)

# Let's set a C++ compiler
AC_PROG_CXX

# This suppresses the error we get for also having the cc version of helper library.
AC_SUBST([CC])

defaultdirs="/ /usr /usr/local /usr/local/kea /usr/pkg /opt /opt/local"


AC_ARG_WITH([kea],
            [AS_HELP_STRING([--with-kea[[=PATH]]],
                            [optional path to the kea installation directory])],
            [kea_path="$withval"])
if test "${kea_path}" = "no" ; then
    AC_MSG_ERROR([Need kea installation directory])
elif test -n "${kea_path}" -a "${kea_path}" != "yes" ; then
    AC_MSG_NOTICE([kea installation directory is _${kea_path}_])
    KEA_INCLUDES="-I${kea_path}/src -I ${kea_path}/src/lib"
    KEA_LIBS="-L${kea_path}/lib"
else
    AC_MSG_NOTICE([kea installation directory not specified, searching for it in default locations])
    # find kea installation directory using defaultdirs
    for d in $defaultdirs
    do
        echo "Checking kea ${d}/include/kea/config.h"
        if test -f ${d}/include/kea/config.h; then
            KEA_INCLUDES="-I$d/include/kea"
            KEA_LIBS="-L$d/lib"
            break
        fi
    done
fi
AC_SUBST(KEA_INCLUDES)
AC_SUBST(KEA_LIBS)

# Check for kea-msg-compiler
AC_MSG_CHECKING([for kea-msg-compiler])
# Check if kea-msg-compiler is in the PATH
AC_PATH_PROG(KEA_MSG_COMPILER, kea-msg-compiler, no)
if test "$KEA_MSG_COMPILER" = "no"; then
    KEA_MSG_COMPILER="${kea_path}/src/lib/log/compiler/kea-msg-compiler"
    if test -x "$KEA_MSG_COMPILER"; then
        AC_MSG_RESULT([yes - found at ${KEA_MSG_COMPILER}])
        enable_generate_messages=yes
    else
        AC_MSG_RESULT([no - kea-msg-compiler not found, disabled generation of message files])
        enable_generate_messages=no
    fi
else
    AC_MSG_RESULT([yes - found in PATH])
    enable_generate_messages=yes
fi
AC_SUBST(KEA_MSG_COMPILER)
AM_CONDITIONAL(GENERATE_MESSAGES, test "x$enable_generate_messages" = "xyes")

# Let's check for Python
# AC_PATH_PROG(PYTHON, python3, no)
# if test "$PYTHON" = "no"; then
#     AC_MSG_ERROR([Python 3 is required])
# fi

# Let's check for Python development files
# AC_MSG_CHECKING([for Python development files])
# AC_RUN_IFELSE([AC_LANG_PROGRAM([#include <Python.h>], [Py_Initialize();])],
#              [AC_MSG_RESULT([yes])],
#              [AC_MSG_ERROR([Python development files are required])])

AX_PYTHON_DEVEL

AC_CONFIG_FILES([keamodule/setup.py], [chmod +x keamodule/setup.py])

# Let's specify where the Makefiles should be produced.
# These are the same locations as your Makefile.in's, but named as Makefile only
# We need to do this because both Autoconf and Automake read this file and
# produce Makefiles from this list.

AC_CONFIG_FILES([Makefile])
AC_CONFIG_FILES([m4macros/Makefile])
AC_CONFIG_FILES([keahook/Makefile])
AC_CONFIG_FILES([keamodule/Makefile])

# Finally produce "configure" script
AC_OUTPUT

echo "Configuration successful. Now type 'make' to compile the code."