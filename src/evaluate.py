#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 23:03:34 2021

@author: jbananafish
"""

import numpy as np
import tensorflow as tf
import sys
import yaml
import json

#it take the test dataset and the model
if len(sys.argv) != 3:
    sys.stderr.write('Number of arguments wrong.')
    sys.exit(1)

params = yaml.safe_load(open('params.yaml'))['train']
    
test_path = sys.argv[1]
model_path = sys.argv[2]
scores_path = "scores.json"

x_test = np.load(test_path + "/x_test_prep.npy")
y_test = np.load(test_path + "/y_test_prep.npy")

loaded_model = tf.keras.models.load_model(model_path)
validation_loss, validation_accuracy = loaded_model.evaluate(x_test, y_test)

#metric
with open(scores_path, 'w') as file:
    json.dump({"loss": validation_loss, "accuracy": validation_accuracy }, file)
