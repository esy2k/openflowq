# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pytopology', [dirname(__file__)])
        except ImportError:
            import _pytopology
            return _pytopology
        if fp is not None:
            try:
                _mod = imp.load_module('_pytopology', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pytopology = swig_import_helper()
    del swig_import_helper
else:
    import _pytopology
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


import nox.lib.netinet
class PyLinkPorts(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PyLinkPorts, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PyLinkPorts, name)
    __repr__ = _swig_repr
    __swig_setmethods__["src"] = _pytopology.PyLinkPorts_src_set
    __swig_getmethods__["src"] = _pytopology.PyLinkPorts_src_get
    if _newclass:src = _swig_property(_pytopology.PyLinkPorts_src_get, _pytopology.PyLinkPorts_src_set)
    __swig_setmethods__["dst"] = _pytopology.PyLinkPorts_dst_set
    __swig_getmethods__["dst"] = _pytopology.PyLinkPorts_dst_get
    if _newclass:dst = _swig_property(_pytopology.PyLinkPorts_dst_get, _pytopology.PyLinkPorts_dst_set)
    def __init__(self): 
        this = _pytopology.new_PyLinkPorts()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pytopology.delete_PyLinkPorts
    __del__ = lambda self : None;
PyLinkPorts_swigregister = _pytopology.PyLinkPorts_swigregister
PyLinkPorts_swigregister(PyLinkPorts)

class LLinkSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LLinkSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LLinkSet, name)
    __repr__ = _swig_repr
    def iterator(self): return _pytopology.LLinkSet_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _pytopology.LLinkSet___nonzero__(self)
    def __bool__(self): return _pytopology.LLinkSet___bool__(self)
    def __len__(self): return _pytopology.LLinkSet___len__(self)
    def pop(self): return _pytopology.LLinkSet_pop(self)
    def __getslice__(self, *args): return _pytopology.LLinkSet___getslice__(self, *args)
    def __setslice__(self, *args): return _pytopology.LLinkSet___setslice__(self, *args)
    def __delslice__(self, *args): return _pytopology.LLinkSet___delslice__(self, *args)
    def __delitem__(self, *args): return _pytopology.LLinkSet___delitem__(self, *args)
    def __getitem__(self, *args): return _pytopology.LLinkSet___getitem__(self, *args)
    def __setitem__(self, *args): return _pytopology.LLinkSet___setitem__(self, *args)
    def append(self, *args): return _pytopology.LLinkSet_append(self, *args)
    def empty(self): return _pytopology.LLinkSet_empty(self)
    def size(self): return _pytopology.LLinkSet_size(self)
    def clear(self): return _pytopology.LLinkSet_clear(self)
    def swap(self, *args): return _pytopology.LLinkSet_swap(self, *args)
    def get_allocator(self): return _pytopology.LLinkSet_get_allocator(self)
    def begin(self): return _pytopology.LLinkSet_begin(self)
    def end(self): return _pytopology.LLinkSet_end(self)
    def rbegin(self): return _pytopology.LLinkSet_rbegin(self)
    def rend(self): return _pytopology.LLinkSet_rend(self)
    def pop_back(self): return _pytopology.LLinkSet_pop_back(self)
    def erase(self, *args): return _pytopology.LLinkSet_erase(self, *args)
    def __init__(self, *args): 
        this = _pytopology.new_LLinkSet(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _pytopology.LLinkSet_push_back(self, *args)
    def front(self): return _pytopology.LLinkSet_front(self)
    def back(self): return _pytopology.LLinkSet_back(self)
    def assign(self, *args): return _pytopology.LLinkSet_assign(self, *args)
    def resize(self, *args): return _pytopology.LLinkSet_resize(self, *args)
    def insert(self, *args): return _pytopology.LLinkSet_insert(self, *args)
    def pop_front(self): return _pytopology.LLinkSet_pop_front(self)
    def push_front(self, *args): return _pytopology.LLinkSet_push_front(self, *args)
    def reverse(self): return _pytopology.LLinkSet_reverse(self)
    __swig_destroy__ = _pytopology.delete_LLinkSet
    __del__ = lambda self : None;
LLinkSet_swigregister = _pytopology.LLinkSet_swigregister
LLinkSet_swigregister(LLinkSet)

class pytopology_proxy(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pytopology_proxy, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pytopology_proxy, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pytopology.new_pytopology_proxy(*args)
        try: self.this.append(this)
        except: self.this = this
    def configure(self, *args): return _pytopology.pytopology_proxy_configure(self, *args)
    def install(self, *args): return _pytopology.pytopology_proxy_install(self, *args)
    def get_outlinks(self, *args): return _pytopology.pytopology_proxy_get_outlinks(self, *args)
    def is_internal(self, *args): return _pytopology.pytopology_proxy_is_internal(self, *args)
    __swig_destroy__ = _pytopology.delete_pytopology_proxy
    __del__ = lambda self : None;
pytopology_proxy_swigregister = _pytopology.pytopology_proxy_swigregister
pytopology_proxy_swigregister(pytopology_proxy)

from nox.lib.core import Component

class pytopology(Component):
    """
    An adaptor over the C++ based Python bindings to
    simplify their implementation.
    """  
    def __init__(self, ctxt):
        self.pytop = pytopology_proxy(ctxt)

    def configure(self, configuration):
        self.pytop.configure(configuration)

    def install(self):
        pass

    def getInterface(self):
        return str(pytopology)

    def get_outlinks(self, dpsrc, dpdst):
        return self.pytop.get_outlinks(dpsrc, dpdst)

    def is_internal(self, dp, port):
        return self.pytop.is_internal(dp, port)


def getFactory():
    class Factory():
        def instance(self, context):
                    
            return pytopology(context)

    return Factory()



