#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:39:39 2018

@author: leobix
"""

import numpy as np
import pandas as pd

filename = '/Users/leobix/Desktop/test_premier.h5'
df = pd.read_csv('/Users/leobix/Desktop/dataport-export-3.csv')
print(df)
#    A  B
# 0  0  1
# 1  2  3
# 2  4  5
# 3  6  7
# 4  8  9

# Save to HDF5
df.to_hdf(filename, 'data', mode='w', format='table')


print(pd.read_hdf(filename, 'data'))