# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:57:06 2020

@author: rkbra
"""

TRAINING_DATA_FILE = "dataset/cleaned_data.csv"
PIPELINE_NAME = "classifier.pkl"

# target feature
TARGET = "target"

# features
FEATURES = ['age', 'gender', 'height', 'weight', 'systolic_blood_pressure',
       'diastolic_blood_pressure', 'cholesterol', 'glucose_level', 'smoking',
       'alcohol_intake', 'physical_activity']

# numerical features
NUMERICAL_FEATURES = ['age', 'height', 'weight', 'systolic_blood_pressure', 'diastolic_blood_pressure']

# categorical features
CATEGORICAL_FEATURES = ['gender', 'cholesterol', 'glucose_level', 'smoking', 'alcohol_intake', 'physical_activity']