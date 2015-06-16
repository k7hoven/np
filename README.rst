np -- create numpy arrays as ``np[1,3,5]``, and more
====================================================

``np``  = ``numpy`` + handy tools

For the numerical Python package ``numpy`` itself, see http://www.numpy.org/.

The idea of ``np`` is to provide a way of creating numpy arrays with a compact syntax and without an explicit function call. Making the module name ``np`` subscriptable, while still keeping it essentially an alias for numpy, does this in a clean way.

Any feedback or suggestions are very welcome: koos.zevenhoven@aalto.fi.

Getting Started
===============

Requirements
------------

* Python 3+ (Probably works with older versions too)
* numpy

Installation
------------

np can be installed with pip:

.. code-block:: bash

    $ pip install np


or directly from the source code:

.. code-block:: bash

    $ git clone https://github.com/k7hoven/np.git
    $ cd np
    $ python setup.py install 

Basic Usage
===========

A popular style of using ``numpy`` has been to import it as ``np``:

.. code-block:: python

    >>> import numpy as np
    >>> my_array = np.array([[1, 2], [3, 4]])
    >>> column_vector = np.array([[1, 2, 3]]).T

The most important feature of ``np`` is to make the creation of arrays less verbose, while everything else works as before. The above code becomes:

.. code-block:: python

    >>> import np
    >>> my_array = np[[1, 2], [3, 4]]
    >>> column_vector = np[[1, 2, 3]].T

As you can see from the above example, you can create numpy arrays by subscripting the `np` module. Since most people would have numpy imported as ``np`` anyway, this requires no additional names to clutter the namespace. Also, the syntax ``np[1,2,3]`` resembles the syntax for ``bytes`` literals, ``b"asd"``. 

The `np` package also provides a convenient way of ensuring something is a numpy array, that is, a shortcut to ``numpy.asanyarray()``:

.. code-block:: python

    >>> import np
    >>> mylist = [1, 3, 5]
    >>> mylist + [7, 9, 11]
    [1, 3, 5, 7, 9, 11]
    >>> np(mylist) + [7, 9, 11]
    array([8, 12, 16])


