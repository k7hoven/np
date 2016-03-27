# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 00:54:30 2016

@author: Koos Zevenhoven
"""
import np.quickarrays as quickarrays
import sys

np = quickarrays.npmodule()

for shortcut in quickarrays.np_quick_types:
    setattr(np, shortcut, quickarrays.NPQuickTypeShortcut(shortcut))
np.np_quick_types = quickarrays.np_quick_types            
np.numpy = quickarrays.numpy
np.np = np
np._repr = quickarrays._repr

sys.modules['np'] = np  
sys.modules['numpy'] = np    

