# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:39:27 2020

@author: rkbra
"""

# datafile and model name
TRAINING_DATA_FILE = "cleaned_data.csv"
PIPELINE_NAME = "regression_model.pickle"

# Target Feature
TARGET = "mpg"

# Features
FEATURES = ['cylinders', 'displacement', 'horsepower', 'weight', \
            'acceleration', 'model year', 'origin']


# numerical features
NUMERICAL_FEATURES = ['displacement', 'horsepower',\
                      'weight', 'acceleration', 'model year']

# categorical features(values are numeric but considered categorical)
CATEGORICAL_FEATURES = ['cylinders','origin']

# variables to transform
VARIABLE_LOG = ['displacement', 'horsepower', 'weight', 'acceleration']


