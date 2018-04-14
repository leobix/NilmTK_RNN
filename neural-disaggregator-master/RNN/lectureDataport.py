#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 01:47:32 2018

@author: leobix
"""

from __future__ import print_function, division
import time

from matplotlib import rcParams
import matplotlib.pyplot as plt

from nilmtk import DataSet, TimeFrame, MeterGroup, HDFDataStore
from rnndisaggregator import RNNDisaggregator
import metrics

print("========== OPEN DATASETS ============")
train = DataSet('/Users/leobix/Desktop/testdataport3.h5')
test = DataSet('/Users/leobix/Desktop/testdataport3.h5')

#train.set_window(start="13-4-2013", end="1-1-2014")
#test.set_window(start="1-1-2014", end="30-3-2014")
print(train.describe)
train_building = 0
test_building = 0
sample_period = 6
meter_key = 'dryer1'
train_elec = train.buildings[train_building].elec
test_elec = test.buildings[test_building].elec