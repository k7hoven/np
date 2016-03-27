# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:49:23 2016

@author: Koos Zevenhoven
"""

import unittest
import np
import sys

class NPTestCase(unittest.TestCase):
    def assertIdenticalArray(self, arr1, arr2):
        self.assertTrue((arr1 == arr2).all())
        self.assertEqual(arr1.dtype, arr2.dtype)
        self.assertEqual(arr1.shape, arr2.shape)


class QuickSubscriptArray(NPTestCase):
    
    def test_1D(self):
        self.assertIdenticalArray(np[1,3,4,5,6,9], np.array([1,3,4,5,6,9]))
        
    def test_mixed_values(self):
        self.assertIdenticalArray(np[1,2.3,4,5.6], np.array([1,2.3,4,5.6]))
        
    def test_float_values(self):
        self.assertIdenticalArray(np[1.0,2.0], np.array([1.0, 2.0]))
        
    def test_2D(self):
        a2d = np.arange(12).reshape((3,4))
        self.assertIdenticalArray(np[[0,1,2,3],[4,5,6,7],[8,9,10,11]],
                                  np.array(a2d))                         
        
    def test_3D(self):
        a3d = np.arange(12).reshape((2,3,2))
        self.assertIdenticalArray(np[[[ 0,  1], [ 2,  3], [ 4,  5]],
                                     [[ 6,  7], [ 8,  9], [10, 11]]],
                                  np.array(a3d))
    
class QuickArray(NPTestCase):
    def test_0D(self):
        self.assertIdenticalArray(np(3), np.array(3))
    
    def test_1D(self):
        self.assertIdenticalArray(np([1,3,4,5,6,9]), np.array([1,3,4,5,6,9]))
        
    def test_mixed_values(self):
        self.assertIdenticalArray(np([1,2.3,4,5.6]), np.array([1,2.3,4,5.6]))
    
    def test_float_values(self):
        self.assertIdenticalArray(np([1.0, 2.0]), np.array([1.0,2.0]))
        
    def test_2D(self):
        a2d = np.arange(12).reshape((3,4))
        self.assertIdenticalArray(np(a2d), np.array(a2d))                                  
        
    def test_3D(self):
        a3d = np.arange(12).reshape((2,3,2))
        self.assertIdenticalArray(np(a3d), np.array(a3d))
                        
def for_dtype_shortcuts(test_method):
    def test_for_all_shortcuts(self):
        for shortcut, dtype in np.np_quick_types.items():
            test_method(self, getattr(np, shortcut), dtype)
    return test_for_all_shortcuts
    
class QuickTypeSubscriptArray(NPTestCase):
    
    @for_dtype_shortcuts
    def test_1D(self, sc, dtype):
        self.assertIdenticalArray(sc[1,3,4,5,6,9], np.array([1,3,4,5,6,9], dtype=dtype))
 
    @for_dtype_shortcuts    
    def test_mixed_values(self, sc, dtype):
        self.assertIdenticalArray(sc[1,2.3,4,5.6], np.array([1,2.3,4,5.6], dtype=dtype))

    @for_dtype_shortcuts    
    def test_float_values(self, sc, dtype):
        self.assertIdenticalArray(sc[1.0,2.0], np.array([1.0, 2.0], dtype=dtype))
    
    @for_dtype_shortcuts    
    def test_2D(self, sc, dtype):
        a2d = np.arange(12).reshape((3,4))
        self.assertIdenticalArray(sc[[0,1,2,3],[4,5,6,7],[8,9,10,11]],
                                  np.array(a2d, dtype=dtype))
                                  
    @for_dtype_shortcuts                             
    def test_3D(self, sc, dtype):
        a3d = np.arange(12).reshape((2,3,2))
        self.assertIdenticalArray(sc[[[ 0,  1], [ 2,  3], [ 4,  5]],
                                     [[ 6,  7], [ 8,  9], [10, 11]]],
                                  np.array(a3d, dtype=dtype))


class QuickTypeArray(NPTestCase):
    @for_dtype_shortcuts
    def test_0D(self, sc, dtype):
        self.assertIdenticalArray(sc(3), np.array(3, dtype=dtype))

    @for_dtype_shortcuts    
    def test_1D(self, sc, dtype):
        self.assertIdenticalArray(sc([1,3,4,5,6,9]), np.array([1,3,4,5,6,9], dtype=dtype))
    
    @for_dtype_shortcuts
    def test_mixed_values(self, sc, dtype):
        self.assertIdenticalArray(sc([1,2.3,4,5.6]), np.array([1,2.3,4,5.6], dtype=dtype))
    
    @for_dtype_shortcuts
    def test_float_values(self, sc, dtype):
        self.assertIdenticalArray(sc([1.0, 2.0]), np.array([1.0,2.0], dtype=dtype))
    
    @for_dtype_shortcuts
    def test_2D(self, sc, dtype):
        a2d = np.arange(12).reshape((3,4))
        self.assertIdenticalArray(sc(a2d), np.array(a2d, dtype=dtype))                                  
    
    @for_dtype_shortcuts
    def test_3D(self, sc, dtype):
        a3d = np.arange(12).reshape((2,3,2))
        self.assertIdenticalArray(sc(a3d), np.array(a3d, dtype=dtype))

if __name__ == "__main__":
    unittest.main()