#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:03:29 2021

@author: jbananafish
"""

import os
import sys
import tensorflow as tf
import numpy as np

if len(sys.argv) != 2:
    sys.stderr.write('Number of arguments wrong.')
    sys.exit(1)

input_path = sys.argv[1]

mnist_dataset = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist_dataset.load_data()

np.save(input_path + "/x_train.npy", x_train)
np.save(input_path + "/x_test.npy", x_test)
np.save(input_path + "/y_train.npy", y_train)
np.save(input_path + "/y_test.npy", y_test)
