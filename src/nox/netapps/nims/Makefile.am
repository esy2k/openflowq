include ../../../Make.vars 

if PY_ENABLED
AM_CPPFLAGS += $(PYTHON_CPPFLAGS)

pkglib_LTLIBRARIES =		\
	openflowq.la            

openflowq_la_CPPFLAGS = $(AM_CPPFLAGS) -I $(top_srcdir)/src/nox -I $(top_srcdir)/src/nox/netapps/ -I $(top_srcdir)/src/nox/coreapps
openflowq_la_SOURCES = openflowq.hh openflowq.cc
openflowq_la_LDFLAGS = -module -export-dynamic

NOX_RUNTIMEFILES = meta.json	

endif # PY_ENABLED


EXTRA_DIST = \
	meta.json

all-local:  nox-all-local
clean-local: nox-clean-local
install-exec-hook: nox-install-local
