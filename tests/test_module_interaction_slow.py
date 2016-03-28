# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:35:18 2016

@author: Koos Zevenhoven
"""
import unittest
import sys
import subprocess

def run_in_subprocess(code):
    PIPE = subprocess.PIPE
    p = subprocess.Popen([sys.executable, '-c', code], stdout=PIPE, stderr=PIPE)
    return p.communicate()

def run_suite(code):
    return run_in_subprocess(code + "; print(repr([_.testsRun, _.failure, _.errors]))")
     
class NumpyTestComparison(unittest.TestCase):
    _numpytest = None
    
    @property
    def numpytest(self):
        if self._numpytest is not None:
            return self._numpytest
        return run_suite("import numpy; numpy.test()")
        
    def assertSameTestResults(self, results1, results2):
        # for key in results1.__dict__:
        #     if isinstance(getattr(results1, key), list):
        #         self.assertEqual(repr(getattr(results1, key)), repr(getattr(results2, key)))
        # comparing reprs of the lists made the tests fail
        
        # OK, make things easier and compare stdout (see also run_test_suite())
        # TODO: more accurate results comparison
        self.assertEqual(results1[0], results2[0])
        
    def test_clean_numpy_vs_clean_np(self):
        res = run_suite("import np; np.test()")
        self.assertSameTestResults(res, self.numpytest)
    
    def test_clean_numpy_vs_after_np(self):
        res = run_suite("import numpy; import np; numpy.test()")
        self.assertSameTestResults(res, self.numpytest)
    
    @unittest.skipIf(sys.version_info >= (3,5,0),
                     "No need to test np and numpy separately when np is numpy")    
    def test_clean_numpy_vs_dirty_np(self):
        res = run_suite("import numpy; import np; np.test()")
        self.assertSameTestResults(res, self.numpytest)
        
class ModuleIdentity(unittest.TestCase):
    @unittest.skipIf(sys.version_info < (3,5,0), 
                     "numpy imported before np is a different object in pre-3.5 Python.")
    def test_numpy_is_np(self):
        res = run_in_subprocess("import numpy; import np; print(numpy is np)")
        self.assertEqual(res[0].strip(), b"True")
    
    def test_np_is_numpy(self):
        res = run_in_subprocess("import np; import numpy; print(np is numpy)")
        self.assertEqual(res[0].strip(), b"True")
        
if __name__ == "__main__":
    unittest.main()
        
        
        
        

