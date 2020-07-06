# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 20:57:06 2020

@author: rkbra
"""

TRAINING_DATA_FILE = "cleaned_data.csv"
PIPELINE_NAME = "classifier_model.pkl"

# target feature
TARGET = "target"

# features
FEATURES = ['age', 'gender', 'height', 'weight', 'systolic_blood_pressure',
       'diastolic_blood_pressure', 'cholesterol', 'glucose_level', 'smoking',
       'alcohol_intake', 'physical_activity']

FEATURES_AFTER_ENCODING = ['age', 'height', 'weight', 'systolic_blood_pressure',
       'diastolic_blood_pressure', 'gender_male',
       'cholesterol_normal', 'cholesterol_well above normal',
       'glucose_level_normal', 'glucose_level_well above normal',
       'smoking_yes', 'alcohol_intake_yes', 'physical_activity_yes']

# numerical features
NUMERICAL_FEATURES = ['age', 'height', 'weight', 'systolic_blood_pressure', 'diastolic_blood_pressure']

# categorical features
CATEGORICAL_FEATURES = ['gender', 'cholesterol', 'glucose_level', 'smoking', 'alcohol_intake', 'physical_activity']