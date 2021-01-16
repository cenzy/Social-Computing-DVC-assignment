#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 22:50:58 2021

@author: jbananafish
"""

import numpy as np
import tensorflow as tf
import sys
import yaml
import json

if len(sys.argv) != 5:
    sys.stderr.write('Number of arguments wrong.')
    sys.exit(1)

params = yaml.safe_load(open('params.yaml'))['train']
    
input_path = sys.argv[1]
model_path = sys.argv[2]
acc_json_path = sys.argv[3]
loss_json_path = sys.argv[4]

x_train = np.load(input_path + "/x_train_prep.npy")
y_train = np.load (input_path + "/y_train_prep.npy")

model = tf.keras.models.Sequential()

# Input layers.
model.add(tf.keras.layers.Flatten(input_shape=x_train.shape[1:]))
model.add(tf.keras.layers.Dense(
    units=128,
    activation=tf.keras.activations.relu,
    kernel_regularizer=tf.keras.regularizers.l2(params['reg'])
))

# Hidden layers.
model.add(tf.keras.layers.Dense(
    units=params['hidden_unit'],
    activation=tf.keras.activations.relu,
    kernel_regularizer=tf.keras.regularizers.l2(params['reg'])
))

# Output layers.
model.add(tf.keras.layers.Dense(
    units=10,
    activation=tf.keras.activations.softmax
))

adam_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

model.compile(
    optimizer=adam_optimizer,
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=['accuracy']
)

training_history = model.fit(
    x_train,
    y_train,
    epochs=params['epochs']
)

epochs = list(range(1, params['epochs'] + 1))

with open(acc_json_path, 'w') as fd:
    json.dump({'epoch-acc': [{
        "epochs": e, 
        "accuracy": a
        } for e, a in zip(epochs, training_history.history['accuracy'])
        ]}, fd)
    
with open(loss_json_path, 'w') as fd:
    json.dump({'epoch-loss': [{
        "epochs": e, 
        "loss": l
        } for e, l in zip(epochs, training_history.history['loss'])
        ]}, fd)
    
model_name = model_path + '/model.h5'
model.save(model_name, save_format='h5')


