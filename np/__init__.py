# -*- coding: utf-8 -*-
# Author: Koos Zevenhoven

# Needs to do some magic to import numpy and replace it with a monkey-patched
# version implementing __getitem__ etc. This seems to be close to the cleanest
# way to do this in Python.

import np.magic
del np.magic # clean up: no need for the magic module after this

