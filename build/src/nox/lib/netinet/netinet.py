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
            fp, pathname, description = imp.find_module('_netinet', [dirname(__file__)])
        except ImportError:
            import _netinet
            return _netinet
        if fp is not None:
            try:
                _mod = imp.load_module('_netinet', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _netinet = swig_import_helper()
    del swig_import_helper
else:
    import _netinet
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


class imaxdiv_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, imaxdiv_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, imaxdiv_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["quot"] = _netinet.imaxdiv_t_quot_set
    __swig_getmethods__["quot"] = _netinet.imaxdiv_t_quot_get
    if _newclass:quot = _swig_property(_netinet.imaxdiv_t_quot_get, _netinet.imaxdiv_t_quot_set)
    __swig_setmethods__["rem"] = _netinet.imaxdiv_t_rem_set
    __swig_getmethods__["rem"] = _netinet.imaxdiv_t_rem_get
    if _newclass:rem = _swig_property(_netinet.imaxdiv_t_rem_get, _netinet.imaxdiv_t_rem_set)
    def __init__(self): 
        this = _netinet.new_imaxdiv_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _netinet.delete_imaxdiv_t
    __del__ = lambda self : None;
imaxdiv_t_swigregister = _netinet.imaxdiv_t_swigregister
imaxdiv_t_swigregister(imaxdiv_t)


def imaxabs(*args):
  return _netinet.imaxabs(*args)
imaxabs = _netinet.imaxabs

def imaxdiv(*args):
  return _netinet.imaxdiv(*args)
imaxdiv = _netinet.imaxdiv

def strtoimax(*args):
  return _netinet.strtoimax(*args)
strtoimax = _netinet.strtoimax

def strtoumax(*args):
  return _netinet.strtoumax(*args)
strtoumax = _netinet.strtoumax

def wcstoimax(*args):
  return _netinet.wcstoimax(*args)
wcstoimax = _netinet.wcstoimax

def wcstoumax(*args):
  return _netinet.wcstoumax(*args)
wcstoumax = _netinet.wcstoumax

def exit(*args):
  return _netinet.exit(*args)
exit = _netinet.exit
class ipaddr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ipaddr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ipaddr, name)
    __repr__ = _swig_repr
    __swig_setmethods__["addr"] = _netinet.ipaddr_addr_set
    __swig_getmethods__["addr"] = _netinet.ipaddr_addr_get
    if _newclass:addr = _swig_property(_netinet.ipaddr_addr_get, _netinet.ipaddr_addr_set)
    def __init__(self, *args): 
        this = _netinet.new_ipaddr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __invert__(self): return _netinet.ipaddr___invert__(self)
    def __and__(self, *args): return _netinet.ipaddr___and__(self, *args)
    def __iand__(self, *args): return _netinet.ipaddr___iand__(self, *args)
    def __or__(self, *args): return _netinet.ipaddr___or__(self, *args)
    def __ior__(self, *args): return _netinet.ipaddr___ior__(self, *args)
    def __iadd__(self, *args): return _netinet.ipaddr___iadd__(self, *args)
    def __add__(self, *args): return _netinet.ipaddr___add__(self, *args)
    def __sub__(self, *args): return _netinet.ipaddr___sub__(self, *args)
    def __lt__(self, *args): return _netinet.ipaddr___lt__(self, *args)
    def __le__(self, *args): return _netinet.ipaddr___le__(self, *args)
    def __gt__(self, *args): return _netinet.ipaddr___gt__(self, *args)
    def __ge__(self, *args): return _netinet.ipaddr___ge__(self, *args)
    def __copy__(self, *args): return _netinet.ipaddr___copy__(self, *args)
    def __deepcopy__(self, *args): return _netinet.ipaddr___deepcopy__(self, *args)
    def __str__(self): return _netinet.ipaddr___str__(self)
    def __nonzero__(self): return _netinet.ipaddr___nonzero__(self)
    def __eq__(self, *args): return _netinet.ipaddr___eq__(self, *args)
    def __ne__(self, *args): return _netinet.ipaddr___ne__(self, *args)
    def __hash__(self): return _netinet.ipaddr___hash__(self)
    __swig_destroy__ = _netinet.delete_ipaddr
    __del__ = lambda self : None;
ipaddr_swigregister = _netinet.ipaddr_swigregister
ipaddr_swigregister(ipaddr)


def create_bin_ipaddr(*args):
  return _netinet.create_bin_ipaddr(*args)
create_bin_ipaddr = _netinet.create_bin_ipaddr
class cidr_ipaddr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cidr_ipaddr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cidr_ipaddr, name)
    __repr__ = _swig_repr
    __swig_setmethods__["addr"] = _netinet.cidr_ipaddr_addr_set
    __swig_getmethods__["addr"] = _netinet.cidr_ipaddr_addr_get
    if _newclass:addr = _swig_property(_netinet.cidr_ipaddr_addr_get, _netinet.cidr_ipaddr_addr_set)
    __swig_setmethods__["mask"] = _netinet.cidr_ipaddr_mask_set
    __swig_getmethods__["mask"] = _netinet.cidr_ipaddr_mask_get
    if _newclass:mask = _swig_property(_netinet.cidr_ipaddr_mask_get, _netinet.cidr_ipaddr_mask_set)
    def __init__(self, *args): 
        this = _netinet.new_cidr_ipaddr(*args)
        try: self.this.append(this)
        except: self.this = this
    def matches(self, *args): return _netinet.cidr_ipaddr_matches(self, *args)
    def get_prefix_len(self): return _netinet.cidr_ipaddr_get_prefix_len(self)
    def __copy__(self, *args): return _netinet.cidr_ipaddr___copy__(self, *args)
    def __deepcopy__(self, *args): return _netinet.cidr_ipaddr___deepcopy__(self, *args)
    def __str__(self): return _netinet.cidr_ipaddr___str__(self)
    def __eq__(self, *args): return _netinet.cidr_ipaddr___eq__(self, *args)
    def __ne__(self, *args): return _netinet.cidr_ipaddr___ne__(self, *args)
    def __hash__(self): return _netinet.cidr_ipaddr___hash__(self)
    __swig_destroy__ = _netinet.delete_cidr_ipaddr
    __del__ = lambda self : None;
cidr_ipaddr_swigregister = _netinet.cidr_ipaddr_swigregister
cidr_ipaddr_swigregister(cidr_ipaddr)

def create_ipaddr(*args):
  return _netinet.create_ipaddr(*args)
create_ipaddr = _netinet.create_ipaddr


def create_cidr_ipaddr(*args):
  return _netinet.create_cidr_ipaddr(*args)
create_cidr_ipaddr = _netinet.create_cidr_ipaddr
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _netinet.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _netinet.SwigPyIterator_value(self)
    def incr(self, n = 1): return _netinet.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _netinet.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _netinet.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _netinet.SwigPyIterator_equal(self, *args)
    def copy(self): return _netinet.SwigPyIterator_copy(self)
    def next(self): return _netinet.SwigPyIterator_next(self)
    def __next__(self): return _netinet.SwigPyIterator___next__(self)
    def previous(self): return _netinet.SwigPyIterator_previous(self)
    def advance(self, *args): return _netinet.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _netinet.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _netinet.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _netinet.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _netinet.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _netinet.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _netinet.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _netinet.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class cidrlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cidrlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cidrlist, name)
    __repr__ = _swig_repr
    def iterator(self): return _netinet.cidrlist_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _netinet.cidrlist___nonzero__(self)
    def __bool__(self): return _netinet.cidrlist___bool__(self)
    def __len__(self): return _netinet.cidrlist___len__(self)
    def pop(self): return _netinet.cidrlist_pop(self)
    def __getslice__(self, *args): return _netinet.cidrlist___getslice__(self, *args)
    def __setslice__(self, *args): return _netinet.cidrlist___setslice__(self, *args)
    def __delslice__(self, *args): return _netinet.cidrlist___delslice__(self, *args)
    def __delitem__(self, *args): return _netinet.cidrlist___delitem__(self, *args)
    def __getitem__(self, *args): return _netinet.cidrlist___getitem__(self, *args)
    def __setitem__(self, *args): return _netinet.cidrlist___setitem__(self, *args)
    def append(self, *args): return _netinet.cidrlist_append(self, *args)
    def empty(self): return _netinet.cidrlist_empty(self)
    def size(self): return _netinet.cidrlist_size(self)
    def clear(self): return _netinet.cidrlist_clear(self)
    def swap(self, *args): return _netinet.cidrlist_swap(self, *args)
    def get_allocator(self): return _netinet.cidrlist_get_allocator(self)
    def begin(self): return _netinet.cidrlist_begin(self)
    def end(self): return _netinet.cidrlist_end(self)
    def rbegin(self): return _netinet.cidrlist_rbegin(self)
    def rend(self): return _netinet.cidrlist_rend(self)
    def pop_back(self): return _netinet.cidrlist_pop_back(self)
    def erase(self, *args): return _netinet.cidrlist_erase(self, *args)
    def __init__(self, *args): 
        this = _netinet.new_cidrlist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _netinet.cidrlist_push_back(self, *args)
    def front(self): return _netinet.cidrlist_front(self)
    def back(self): return _netinet.cidrlist_back(self)
    def assign(self, *args): return _netinet.cidrlist_assign(self, *args)
    def resize(self, *args): return _netinet.cidrlist_resize(self, *args)
    def insert(self, *args): return _netinet.cidrlist_insert(self, *args)
    def pop_front(self): return _netinet.cidrlist_pop_front(self)
    def push_front(self, *args): return _netinet.cidrlist_push_front(self, *args)
    def reverse(self): return _netinet.cidrlist_reverse(self)
    __swig_destroy__ = _netinet.delete_cidrlist
    __del__ = lambda self : None;
cidrlist_swigregister = _netinet.cidrlist_swigregister
cidrlist_swigregister(cidrlist)

class ethernetaddr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ethernetaddr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ethernetaddr, name)
    __repr__ = _swig_repr
    LEN = _netinet.ethernetaddr_LEN
    __swig_setmethods__["octet"] = _netinet.ethernetaddr_octet_set
    __swig_getmethods__["octet"] = _netinet.ethernetaddr_octet_get
    if _newclass:octet = _swig_property(_netinet.ethernetaddr_octet_get, _netinet.ethernetaddr_octet_set)
    def __init__(self, *args): 
        this = _netinet.new_ethernetaddr(*args)
        try: self.this.append(this)
        except: self.this = this
    def hb_long(self): return _netinet.ethernetaddr_hb_long(self)
    def nb_long(self): return _netinet.ethernetaddr_nb_long(self)
    def __lt__(self, *args): return _netinet.ethernetaddr___lt__(self, *args)
    def __le__(self, *args): return _netinet.ethernetaddr___le__(self, *args)
    def __gt__(self, *args): return _netinet.ethernetaddr___gt__(self, *args)
    def __ge__(self, *args): return _netinet.ethernetaddr___ge__(self, *args)
    def is_private(self): return _netinet.ethernetaddr_is_private(self)
    def is_multicast(self): return _netinet.ethernetaddr_is_multicast(self)
    def is_broadcast(self): return _netinet.ethernetaddr_is_broadcast(self)
    def is_zero(self): return _netinet.ethernetaddr_is_zero(self)
    def __copy__(self, *args): return _netinet.ethernetaddr___copy__(self, *args)
    def __deepcopy__(self, *args): return _netinet.ethernetaddr___deepcopy__(self, *args)
    def __str__(self): return _netinet.ethernetaddr___str__(self)
    def binary_str(self): return _netinet.ethernetaddr_binary_str(self)
    def __nonzero__(self): return _netinet.ethernetaddr___nonzero__(self)
    def __eq__(self, *args): return _netinet.ethernetaddr___eq__(self, *args)
    def __ne__(self, *args): return _netinet.ethernetaddr___ne__(self, *args)
    def __hash__(self): return _netinet.ethernetaddr___hash__(self)
    __swig_destroy__ = _netinet.delete_ethernetaddr
    __del__ = lambda self : None;
ethernetaddr_swigregister = _netinet.ethernetaddr_swigregister
ethernetaddr_swigregister(ethernetaddr)


def create_bin_eaddr(*args):
  return _netinet.create_bin_eaddr(*args)
create_bin_eaddr = _netinet.create_bin_eaddr
class ethlist(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ethlist, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ethlist, name)
    __repr__ = _swig_repr
    def iterator(self): return _netinet.ethlist_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _netinet.ethlist___nonzero__(self)
    def __bool__(self): return _netinet.ethlist___bool__(self)
    def __len__(self): return _netinet.ethlist___len__(self)
    def pop(self): return _netinet.ethlist_pop(self)
    def __getslice__(self, *args): return _netinet.ethlist___getslice__(self, *args)
    def __setslice__(self, *args): return _netinet.ethlist___setslice__(self, *args)
    def __delslice__(self, *args): return _netinet.ethlist___delslice__(self, *args)
    def __delitem__(self, *args): return _netinet.ethlist___delitem__(self, *args)
    def __getitem__(self, *args): return _netinet.ethlist___getitem__(self, *args)
    def __setitem__(self, *args): return _netinet.ethlist___setitem__(self, *args)
    def append(self, *args): return _netinet.ethlist_append(self, *args)
    def empty(self): return _netinet.ethlist_empty(self)
    def size(self): return _netinet.ethlist_size(self)
    def clear(self): return _netinet.ethlist_clear(self)
    def swap(self, *args): return _netinet.ethlist_swap(self, *args)
    def get_allocator(self): return _netinet.ethlist_get_allocator(self)
    def begin(self): return _netinet.ethlist_begin(self)
    def end(self): return _netinet.ethlist_end(self)
    def rbegin(self): return _netinet.ethlist_rbegin(self)
    def rend(self): return _netinet.ethlist_rend(self)
    def pop_back(self): return _netinet.ethlist_pop_back(self)
    def erase(self, *args): return _netinet.ethlist_erase(self, *args)
    def __init__(self, *args): 
        this = _netinet.new_ethlist(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _netinet.ethlist_push_back(self, *args)
    def front(self): return _netinet.ethlist_front(self)
    def back(self): return _netinet.ethlist_back(self)
    def assign(self, *args): return _netinet.ethlist_assign(self, *args)
    def resize(self, *args): return _netinet.ethlist_resize(self, *args)
    def insert(self, *args): return _netinet.ethlist_insert(self, *args)
    def pop_front(self): return _netinet.ethlist_pop_front(self)
    def push_front(self, *args): return _netinet.ethlist_push_front(self, *args)
    def reverse(self): return _netinet.ethlist_reverse(self)
    __swig_destroy__ = _netinet.delete_ethlist
    __del__ = lambda self : None;
ethlist_swigregister = _netinet.ethlist_swigregister
ethlist_swigregister(ethlist)

def create_eaddr(*args):
  return _netinet.create_eaddr(*args)
create_eaddr = _netinet.create_eaddr

class datapathid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, datapathid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, datapathid, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _netinet.new_datapathid(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["from_host"] = lambda x: _netinet.datapathid_from_host
    if _newclass:from_host = staticmethod(_netinet.datapathid_from_host)
    __swig_getmethods__["from_net"] = lambda x: _netinet.datapathid_from_net
    if _newclass:from_net = staticmethod(_netinet.datapathid_from_net)
    def as_host(self): return _netinet.datapathid_as_host(self)
    def as_net(self): return _netinet.datapathid_as_net(self)
    def __lt__(self, *args): return _netinet.datapathid___lt__(self, *args)
    def __le__(self, *args): return _netinet.datapathid___le__(self, *args)
    def __gt__(self, *args): return _netinet.datapathid___gt__(self, *args)
    def __ge__(self, *args): return _netinet.datapathid___ge__(self, *args)
    def empty(self): return _netinet.datapathid_empty(self)
    def string(self): return _netinet.datapathid_string(self)
    def __copy__(self, *args): return _netinet.datapathid___copy__(self, *args)
    def __deepcopy__(self, *args): return _netinet.datapathid___deepcopy__(self, *args)
    def __str__(self): return _netinet.datapathid___str__(self)
    def __nonzero__(self): return _netinet.datapathid___nonzero__(self)
    def __eq__(self, *args): return _netinet.datapathid___eq__(self, *args)
    def __ne__(self, *args): return _netinet.datapathid___ne__(self, *args)
    def __hash__(self): return _netinet.datapathid___hash__(self)
    __swig_destroy__ = _netinet.delete_datapathid
    __del__ = lambda self : None;
datapathid_swigregister = _netinet.datapathid_swigregister
datapathid_swigregister(datapathid)

def datapathid_from_host(*args):
  return _netinet.datapathid_from_host(*args)
datapathid_from_host = _netinet.datapathid_from_host

def datapathid_from_net(*args):
  return _netinet.datapathid_from_net(*args)
datapathid_from_net = _netinet.datapathid_from_net


def create_datapathid_from_bytes(*args):
  return _netinet.create_datapathid_from_bytes(*args)
create_datapathid_from_bytes = _netinet.create_datapathid_from_bytes

def create_datapathid_from_host(*args):
  return _netinet.create_datapathid_from_host(*args)
create_datapathid_from_host = _netinet.create_datapathid_from_host

def create_datapathid_from_net(*args):
  return _netinet.create_datapathid_from_net(*args)
create_datapathid_from_net = _netinet.create_datapathid_from_net
class Packet_expr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Packet_expr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Packet_expr, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _netinet.new_Packet_expr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _netinet.delete_Packet_expr
    __del__ = lambda self : None;
    AP_SRC = _netinet.Packet_expr_AP_SRC
    AP_DST = _netinet.Packet_expr_AP_DST
    DL_VLAN = _netinet.Packet_expr_DL_VLAN
    DL_VLAN_PCP = _netinet.Packet_expr_DL_VLAN_PCP
    DL_TYPE = _netinet.Packet_expr_DL_TYPE
    DL_SRC = _netinet.Packet_expr_DL_SRC
    DL_DST = _netinet.Packet_expr_DL_DST
    NW_SRC = _netinet.Packet_expr_NW_SRC
    NW_DST = _netinet.Packet_expr_NW_DST
    NW_PROTO = _netinet.Packet_expr_NW_PROTO
    TP_SRC = _netinet.Packet_expr_TP_SRC
    TP_DST = _netinet.Packet_expr_TP_DST
    GROUP_SRC = _netinet.Packet_expr_GROUP_SRC
    GROUP_DST = _netinet.Packet_expr_GROUP_DST
    def set_uint32_field(self, *args): return _netinet.Packet_expr_set_uint32_field(self, *args)
    def set_ip_field(self, *args): return _netinet.Packet_expr_set_ip_field(self, *args)
    def set_eth_field(self, *args): return _netinet.Packet_expr_set_eth_field(self, *args)
    def __str__(self): return _netinet.Packet_expr___str__(self)
Packet_expr_swigregister = _netinet.Packet_expr_swigregister
Packet_expr_swigregister(Packet_expr)

class Flow(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Flow, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Flow, name)
    __repr__ = _swig_repr
    __swig_setmethods__["in_port"] = _netinet.Flow_in_port_set
    __swig_getmethods__["in_port"] = _netinet.Flow_in_port_get
    if _newclass:in_port = _swig_property(_netinet.Flow_in_port_get, _netinet.Flow_in_port_set)
    __swig_setmethods__["dl_vlan"] = _netinet.Flow_dl_vlan_set
    __swig_getmethods__["dl_vlan"] = _netinet.Flow_dl_vlan_get
    if _newclass:dl_vlan = _swig_property(_netinet.Flow_dl_vlan_get, _netinet.Flow_dl_vlan_set)
    __swig_setmethods__["dl_vlan_pcp"] = _netinet.Flow_dl_vlan_pcp_set
    __swig_getmethods__["dl_vlan_pcp"] = _netinet.Flow_dl_vlan_pcp_get
    if _newclass:dl_vlan_pcp = _swig_property(_netinet.Flow_dl_vlan_pcp_get, _netinet.Flow_dl_vlan_pcp_set)
    __swig_setmethods__["dl_src"] = _netinet.Flow_dl_src_set
    __swig_getmethods__["dl_src"] = _netinet.Flow_dl_src_get
    if _newclass:dl_src = _swig_property(_netinet.Flow_dl_src_get, _netinet.Flow_dl_src_set)
    __swig_setmethods__["dl_dst"] = _netinet.Flow_dl_dst_set
    __swig_getmethods__["dl_dst"] = _netinet.Flow_dl_dst_get
    if _newclass:dl_dst = _swig_property(_netinet.Flow_dl_dst_get, _netinet.Flow_dl_dst_set)
    __swig_setmethods__["dl_type"] = _netinet.Flow_dl_type_set
    __swig_getmethods__["dl_type"] = _netinet.Flow_dl_type_get
    if _newclass:dl_type = _swig_property(_netinet.Flow_dl_type_get, _netinet.Flow_dl_type_set)
    __swig_setmethods__["nw_src"] = _netinet.Flow_nw_src_set
    __swig_getmethods__["nw_src"] = _netinet.Flow_nw_src_get
    if _newclass:nw_src = _swig_property(_netinet.Flow_nw_src_get, _netinet.Flow_nw_src_set)
    __swig_setmethods__["nw_dst"] = _netinet.Flow_nw_dst_set
    __swig_getmethods__["nw_dst"] = _netinet.Flow_nw_dst_get
    if _newclass:nw_dst = _swig_property(_netinet.Flow_nw_dst_get, _netinet.Flow_nw_dst_set)
    __swig_setmethods__["nw_proto"] = _netinet.Flow_nw_proto_set
    __swig_getmethods__["nw_proto"] = _netinet.Flow_nw_proto_get
    if _newclass:nw_proto = _swig_property(_netinet.Flow_nw_proto_get, _netinet.Flow_nw_proto_set)
    __swig_setmethods__["tp_src"] = _netinet.Flow_tp_src_set
    __swig_getmethods__["tp_src"] = _netinet.Flow_tp_src_get
    if _newclass:tp_src = _swig_property(_netinet.Flow_tp_src_get, _netinet.Flow_tp_src_set)
    __swig_setmethods__["tp_dst"] = _netinet.Flow_tp_dst_set
    __swig_getmethods__["tp_dst"] = _netinet.Flow_tp_dst_get
    if _newclass:tp_dst = _swig_property(_netinet.Flow_tp_dst_get, _netinet.Flow_tp_dst_set)
    def __init__(self): 
        this = _netinet.new_Flow()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _netinet.delete_Flow
    __del__ = lambda self : None;
Flow_swigregister = _netinet.Flow_swigregister
Flow_swigregister(Flow)


def c_htonl(*args):
  return _netinet.c_htonl(*args)
c_htonl = _netinet.c_htonl

def c_ntohl(*args):
  return _netinet.c_ntohl(*args)
c_ntohl = _netinet.c_ntohl


