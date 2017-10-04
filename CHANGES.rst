Changelog
=========

1.0.0 (2017-09-20)
------------

- Creating matrices is now even simpler::
 
    np.m[1, 2: 3, 4] == np.array([[1, 2], [3, 4]])

    np.m[1, 2:
        :3, 4] == np.array([[1, 2], [3, 4]])

    np.m[1, 2] == np.array([[1, 2]])

    np.m[1, 2].T == np.array([[1],
                              [2]])


- ``np(...)`` corresponds to ``np.asarray(...)``
- Many improvements to error handling
- Some more cleanups to type shortcuts

0.2.0 (2016-03-29)
------------------

- Quick types are now ``np.i``, ``np.f``, ``np.u``, ``np.c``, or with the 
  number of *bytes* per value appended: 
  ``np.i4`` -> int32, ``np.u2`` -> uint16, ``np.c16`` -> complex128, ...
  (still somewhat experimental)
- Removed the old np.i8 and np.ui8 which represented 8-bit types, which
  was inconsistent with short numpy dtype names which correspond to numbers of
  bytes. The rest of the bit-based shortcuts are deprecated and will be removed
  later.
- Handle Python versions >=3.5 better; now even previously imported plain numpy
  module objects become the exact same object as np. 
- Tests for all np functionality
- Ridiculously slow tests that runs the numpy test suite several times to
  make sure that np does not affect numpy functionality.
- Remove numpy from requirements and give a meaningful error instead if numpy
  is missing (i.e. install it using your package manager like conda or pip)
- Better reprs for subscriptable array creator objects and the np/numpy module.

0.1.4 (2016-01-26)
------------------

- Bug fix

0.1.2 (2015-06-17)
------------------

- Improved experimental dtype shortcuts: np.f[1,2], np.i32[1,2], etc.

0.1.1 (2015-06-17)
------------------

- PyPI-friendly readme

0.1.0 (2015-06-17)
------------------

- First distributable version
- Easy arrays such as np[[1,2],[3,4]]
- Shortcut for np.asanyarray(obj): np(obj)
- Experimental dtype shortcuts: np.f64[[1,2],[3,4]]
 


