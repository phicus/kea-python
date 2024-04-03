AM_CPPFLAGS = $(KEA_INCLUDES) $(PYTHON_CPPFLAGS)
AM_LDFLAGS = $(KEA_LIBS) 

noinst_LTLIBRARIES = libpython.la

libpython_la_SOURCES  =
libpython_la_SOURCES += load_unload.cc
libpython_la_SOURCES += messages.cc
libpython_la_SOURCES += multi_threading_compatible.cc 
libpython_la_SOURCES += version.cc

libpython_la_CXXFLAGS = $(AM_CXXFLAGS)
libpython_la_CPPFLAGS = $(AM_CPPFLAGS)

# install the shared object into $(libdir)/kea/hooks
lib_hooksdir = $(libdir)/kea/hooks
lib_hooks_LTLIBRARIES = libdhcp_python.la

libdhcp_python_la_SOURCES  =
libdhcp_python_la_LIBADD  = libpython.la
libdhcp_python_la_LDFLAGS  = $(AM_LDFLAGS)
libdhcp_python_la_LDFLAGS  += -avoid-version -export-dynamic -module

.PHONY: maintainer-clean-local
maintainer-clean-local:
	rm -f messages.cc messages.h

.PHONY: messages-clean
messages-clean: maintainer-clean-local

if GENERATE_MESSAGES

messages: messages.h messages.cc
	@echo Message files regenerated

messages.h messages.cc: messages.mes
	$(KEA_MSG_COMPILER) messages.mes

else

messages messages.h messages.cc:
	@echo Messages generation disabled. Compile kea with --enable-generate-messages to enable it.

endif
