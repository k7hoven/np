# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:05:47 2015

@author: Koos Zevenhoven
"""

import types
import sys
try:
    import numpy
except ImportError as e:
    raise RuntimeError("The numpy package must be installed to use the np extensions. \n"
                       "Please install numpy using your package manager such as conda or pip.")
    
from numpy import array, asarray, asanyarray, isscalar, shape

np_quick_types = {
    'f': numpy.float_,
    'f8': numpy.float64,
    'f64': numpy.float64,
    'f4': numpy.float32,
    'f32': numpy.float32,
    'f2': numpy.float16,
    'i': numpy.int_,
#    'i8': numpy.int64,  allow this in the future?
    'i64': numpy.int64,
    'i4': numpy.int32,
    'i32': numpy.int32,
    'i2': numpy.int16,
    'i16': numpy.int16,
    'i1': numpy.int8,
#    'i8': numpy.int8,   not ok; this might mean 8*8 == 64 bits
    'u8': numpy.uint64,
    'ui64': numpy.uint64,
    'u4': numpy.uint32,
    'ui32': numpy.uint32,
    'u2': numpy.uint16,
    'ui16': numpy.uint16,
    'u1': numpy.uint8,
#    'ui8': numpy.uint8, not ok; this might mean 8*8 == 64 bits 
    'c': numpy.complex_,
    'c16': numpy.complex128,
#    'c128': numpy.complex128,  leave out for consistency
    'c8': numpy.complex64,
#    'c64': numpy.complex64     leave out for consistency
}

def all_scalar(objs):
    return all(isscalar(obj) for obj in objs)

def all_equal_len(objs):
    lengths = [len(obj) for obj in objs]
    return len(set(lengths)) <= 1

def all_equal_shape(objs):
    return len(set(shape(obj) for obj in objs)) <= 1

def shape_ok(objs):
    if all_scalar(objs):
        return True
    if not all_equal_shape(objs):
        return False
    return shape_ok([obj for cont in objs
                             for obj in cont])

def getitem_process(arg):
    if not isinstance(arg, tuple):
        # We know that the user did not use
        # multiple arguments to subscript [arg1, ...].
        arg = (arg,)
    if any(type(obj) is tuple for obj in arg):
        raise TypeError("use np.m or lists [...] instead of tuples (...)")
    if not shape_ok(arg):
        raise SyntaxError("cannot construct n-dimensional array")
    return arg

class CheckEqual(object):
    def new(self, new_value):
        try:
            return self.value == new_value
        except AttributeError:
            self.value = new_value
            return True

def getitem_process_matrix(arg):
    if type(arg) is slice:
        raise SyntaxError("to create a column vector, use np.m[1, 2, 3].T")
    count = 0
    columns_check = CheckEqual()
    style_check = CheckEqual()
    elements = []
    for val in arg:
        if type(val) is slice:
            # always an element in 'start'
            if not isscalar(val.start):
                if val.start is None:
                    raise SyntaxError("missing element(s) or misplaced punctuation")
                tname = type(val.start).__name__
                raise ValueError("'{}' object is not scalar".format(tname))
            
            elements.append(val.start)
            count += 1

            if not columns_check.new(count):
                raise SyntaxError("matrix row lengths "
                                  "{} and {} do not match".format(columns_check.value, 
                                                                  count))
            count = 0

            if val.step is val.stop is None:
                raise SyntaxError("missing element(s) or misplaced punctuation")

            # look for element in 'stop' and 'step'
            if val.step is None:
                if not style_check.new('single'):
                    raise SyntaxError("inconsistent use of colons in matrix")
                val = val.stop
            elif val.stop is None:
                if not style_check.new('double'):
                    raise SyntaxError("inconsistent use of colons in matrix")
                val = val.step
            else:
                raise SyntaxError("missing element(s) or misplaced punctuation")

            # continue just as with a plain value
 
        if not isscalar(val):
            tname = type(val).__name__
            raise ValueError("'{}' object is not scalar".format(tname))
            
        elements.append(val)
        count += 1
    
    if not columns_check.new(count):
        raise SyntaxError("matrix row lengths "
                          "{} and {} do not match".format(columns_check.value,
                                                          count))
    return elements, columns_check.value
    
class NPQuickTypeShortcut(object):
    def __init__(self, shortcut):
        self.dtype = np_quick_types[shortcut]
        self._shortcut_name = 'np.' + shortcut
        
    def __getitem__(self, arg):
        return array(getitem_process(arg), dtype = self.dtype)
  
    def __call__(self, *args, **kwargs):
        return asarray(*args, dtype = self.dtype, **kwargs)
    
    def __repr__(self):
        return "<np quick array creator for dtype %s>" % repr(self.dtype.__name__)

class NPQuickMatrixCreator(object):
    def __init__(self, dtype_shortcut = None):
        self._shortcut_name = 'np.m'
        self.dtype = np_quick_types.get(dtype_shortcut, None)
    
    def __getitem__(self, arg):
        data, columns = getitem_process_matrix(arg)
        return array(data, dtype=self.dtype).reshape((-1, columns))

    def __repr__(self):
        return "<np quick matrix creator>"
    

class npmodule(types.ModuleType):
    def __init__(self):
        self.__name__ = numpy.__name__ # to initialize self.__dict__
        self.__dict__.update(numpy.__dict__)
        
        sys.modules[numpy.__name__] = self
        sys.modules['np'] = self

    def __getitem__(self, arg):
        return array(getitem_process(arg))
  
    def __call__(self, *args, **kwargs):
        return asarray(*args, **kwargs)
        
    def __repr__(self):
        return self._repr

_repr = repr(numpy).replace("<module", "<np-enhanced module")
