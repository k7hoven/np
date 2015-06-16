# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:05:47 2015

@author: Koos Zevenhoven
"""

import types
import sys
import numpy
from numpy import array, arange, asanyarray

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
            self.i8 = npmodule(dtype = numpy.int8)

            self.ui64 = npmodule(dtype = numpy.uint64)
            self.ui32 = npmodule(dtype = numpy.uint32)
            self.ui16 = npmodule(dtype = numpy.uint16)
            self.ui8 = npmodule(dtype = numpy.uint8)
            
            self.c = npmodule(dtype = numpy.complex_)
            self.c128 = npmodule(dtype = numpy.complex128)
            self.c64 = npmodule(dtype = numpy.complex64)
                        
            self.numpy = numpy
            sys.modules[numpy.__name__] = self
            sys.modules['np'] = self
        
        self.dtype = dtype

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

npmodule()


  
    
