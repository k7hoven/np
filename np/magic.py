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
                  
                

class npmodule(types.ModuleType):
    def __init__(self, dtype = None):
        if dtype is None:
            self.__name__ = numpy.__name__ # to initialize self.__dict__
            self.__dict__.update(numpy.__dict__)
            
            self.f = npmodule(dtype = numpy.float_)
            self.f64 = npmodule(dtype = numpy.float64)        
            self.f32 = npmodule(dtype = numpy.float32)            
            
            self.i = npmodule(dtype = numpy.int_)
            self.i64 = npmodule(dtype = numpy.int64)
            self.i32 = npmodule(dtype = numpy.int32)
            self.i16 = npmodule(dtype = numpy.int16)
            #self.i8 = npmodule(dtype = numpy.int8)
            
            self.ui64 = npmodule(dtype = numpy.uint64)
            self.ui32 = npmodule(dtype = numpy.uint32)
            self.ui16 = npmodule(dtype = numpy.uint16)
            #self.ui8 = npmodule(dtype = numpy.uint8)
            
            self.c = npmodule(dtype = numpy.complex_)
            self.c128 = npmodule(dtype = numpy.complex128)
            self.c64 = npmodule(dtype = numpy.complex64)
            
            self.np_quick_types = np_quick_types            
                        
            self.numpy = numpy
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


  
    
