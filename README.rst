np -- create numpy arrays as ``np[1,3,5]``, and more
====================================================

``np``  = ``numpy`` + handy tools

It's easy: start by importing ``np`` (the alias for numpy):

.. code-block:: python

    import np


Create a 1-D array: 
  
.. code-block:: python

    np[1, 3, 5]


Create a 2-D matrix:

.. code-block:: python

    np[1, 2, 3: 
      :4, 5, 6:
      :7, 8, 9]


For the numerical Python package ``numpy`` itself, see http://www.numpy.org/.

The idea of ``np`` is to provide a way of creating numpy arrays with a compact syntax and without an explicit function call. Making the module name ``np`` subscriptable, while still keeping it essentially an alias for numpy, does this in a clean way.

Any feedback is very welcome: ``koos.zevenhoven@aalto.fi``.

Getting Started
===============

Requirements
------------

* Works best with Python 3.5+ (Tested also with 3.4 and 2.7)
* numpy (you should install this using your python package manager like ``conda`` or ``pip``)

Installation
------------

``np`` can be installed with ``pip`` or ``pip3``:

.. code-block:: bash

    $ pip install np


or directly from the source code:

.. code-block:: bash

    $ git clone https://github.com/k7hoven/np.git
    $ cd np
    $ python setup.py install 

Basic Usage
===========

Even before the ``np`` tool, a popular style of using ``numpy`` has been to import it as ``np``:

.. code-block:: python

    >>> import numpy as np
    >>> my_array = np.array([3, 4, 5])
    >>> my_2d_array = np.array([[1, 2], [3, 4]])

The most important feature of ``np`` is to make the creation of arrays less verbose, while everything else works as before. The above code becomes:

.. code-block:: python

    >>> import np
    >>> my_array = np[3, 4, 5]
    >>> my_2d_array = np[[1, 2], [3, 4]]
    >>> my_matrix = np.m[1, 2: 3, 4]
    >>> my_matrix2 = np.m[1, 2, 3:
    ...                  :4, 5, 6:
    ...                  :7, 8, 9]
    >>> my_row_vector = np.m[1, 2, 3]


As you can see from the above example, you can create numpy arrays by subscripting the ``np`` module. Since most people would have numpy imported as ``np`` anyway, this requires no additional names to clutter the namespace. Also, the syntax ``np[1,2,3]`` resembles the syntax for ``bytes`` literals, ``b"asd"``.

The above also shows how you can use ``np.m`` and colons to easily create matrices (NxM) or row vectors (1xM).

The `np` package also provides a convenient way of ensuring something is a numpy array, that is, a shortcut to ``numpy.asarray()``:

.. code-block:: python

    >>> import np
    >>> mylist = [1, 3, 5]
    >>> mylist + [7, 9, 11]
    [1, 3, 5, 7, 9, 11]
    >>> np(mylist) + [7, 9, 11]
    array([8, 12, 16])


As an experimental feature, there are also shortcuts for giving the arrays a specific data type (numpy dtype):

.. code-block:: python

    >>> np[1, 2, 3]
    array([1, 2, 3])
    >>> np.f[1, 2, 3]
    array([ 1.,  2.,  3.])
    >>> np.f2[1, 2, 3]
    array([ 1.,  2.,  3.], dtype=float16)
    >>> np.u4[1, 2, 3]
    array([1, 2, 3], dtype=uint32)
    >>> np.c[1, 2, 3]
    array([ 1.+0.j,  2.+0.j,  3.+0.j])

