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
    
from numpy import array, arange, asanyarray

np_quick_types = {
    'f': numpy.float_,
    'f64': numpy.float64,
    'f32': numpy.float32,
    'i': numpy.int_,
    'i64': numpy.int64,
    'i32': numpy.int32,
    'i16': numpy.int16,
#    'i8': numpy.int8,   not ok; this might mean 8*8 == 64 bits
    'ui64': numpy.uint64,
    'ui32': numpy.uint32,
    'ui16': numpy.uint16,
#    'ui8': numpy.uint8, not ok; this might mean 8*8 == 64 bits 
    'c': numpy.complex_,
    'c128': numpy.complex128,
    'c64': numpy.complex64 
}
                  

class NPQuickTypeShortcut(object):
    def __init__(self, shortcut):
        self.dtype = np_quick_types[shortcut]
        self._shortcut_name = 'np.' + shortcut
        
    def __getitem__(self, arg):
        if isinstance(arg, tuple):
            # Assume the tuple was not created by the user,
            # i.e. multiple arguments to subscript [arg1, ...].
            return array(arg, dtype = self.dtype)
        if isinstance(arg, list):
            return array((arg,), dtype = self.dtype)
        if isinstance(arg, slice):
            rangeargs = (arg.start if arg.start is not None else 0, 
                         arg.stop, 
                         arg.step if arg.step is not None else 1)
            return arange(*rangeargs, dtype = self.dtype)
        return array((arg,), dtype = self.dtype)
  
    def __call__(self, *args, **kwargs):
        return asanyarray(*args, dtype = self.dtype, **kwargs)
    
                

class npmodule(types.ModuleType):
    def __init__(self, dtype = None):
        if dtype is None:
            self.__name__ = numpy.__name__ # to initialize self.__dict__
            self.__dict__.update(numpy.__dict__)
            
            for shortcut in np_quick_types:
                setattr(self, shortcut, NPQuickTypeShortcut(shortcut))
            self.np_quick_types = np_quick_types            
                        
            self.numpy = numpy
            self.np = self
            sys.modules[numpy.__name__] = self
            sys.modules['np'] = self
        
        self.__dtype = dtype

    def __getitem__(self, arg):
        if isinstance(arg, tuple):
            # Assume the tuple was not created by the user,
            # i.e. multiple arguments to subscript [arg1, ...].
            return array(arg, dtype = self.__dtype)
        if isinstance(arg, list):
            return array((arg,), dtype = self.__dtype)
        if isinstance(arg, slice):
            rangeargs = (arg.start if arg.start is not None else 0, 
                         arg.stop, 
                         arg.step if arg.step is not None else 1)
            return arange(*rangeargs, dtype = self.__dtype)
        return array((arg,), dtype = self.__dtype)
  
    def __call__(self, *args, **kwargs):
        return asanyarray(*args, dtype = self.__dtype, **kwargs)

npmodule()


  
    
