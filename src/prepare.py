#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:10:02 2021

@author: jbananafish
"""

import numpy as np
import sys

if len(sys.argv) != 3:
    sys.stderr.write('Number of arguments wrong.')
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

x_train = np.load(input_path + "/x_train.npy")
y_train = np.load (input_path + "/y_train.npy")
x_test = np.load(input_path + "/x_test.npy")
y_test = np.load(input_path + "/y_test.npy")

x_train_normalized = x_train / 255
x_test_normalized = x_test / 255

np.save(output_path + "/x_train_prep.npy", x_train)
np.save(output_path + "/x_test_prep.npy", x_test)
np.save(output_path + "/y_train_prep.npy", y_train)
np.save(output_path + "/y_test_prep.npy", y_test)