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
        self.assertIdenticalArray(np([1,3,4,5,6,9]), np.array([1,3,4,5,6,9]))
        
    def test_mixed_values(self):
        self.assertIdenticalArray(np[1,2.3,4,5.6], np.array([1,2.3,4,5.6]))
        self.assertIdenticalArray(np([1,2.3,4,5.6]), np.array([1,2.3,4,5.6]))
        
    def test_float_values(self):
        self.assertIdenticalArray(np[1.0,2.0], np.array([1.0, 2.0]))
        
    def test_2D(self):
        a2d = np.arange(12).reshape((3,4))
        self.assertIdenticalArray(np[[0,1,2,3],[4,5,6,7],[8,9,10,11]],
                                  np.array(a2d))
        self.assertIdenticalArray(np(a2d), np.array(a2d))                                  
        
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
        
    
def make_quick_type_tests():
    
    pass

if __name__ == "__main__":
    unittest.main()