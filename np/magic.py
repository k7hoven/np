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
            self.f64 = npmodule(dtype = 'float64')
            self.i8 = npmodule(dtype = 'int8')
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
            rangeargs = (arg.start, 
                         arg.stop, 
                         arg.step if arg.step is not None else 1)
            return arange(*rangeargs, dtype = self.dtype)
        return array((arg,), dtype = self.dtype)
  
    def __call__(self, *args, **kwargs):
        return asanyarray(*args, dtype = self.dtype, **kwargs)

npmodule()


  
    
