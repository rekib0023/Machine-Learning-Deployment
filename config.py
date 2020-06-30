# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:27:50 2020

@author: rkbra
"""

# datafile and model name
TRAINING_DATA_FILE = "cleaned_data.csv"
PIPELINE_NAME = "classification_model.pickle"

# target feature
TARGET = "target"

# features
FEATURES = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure',
       'cholesterol', 'fasting_blood_sugar', 'rest_ecg',
       'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression',
       'st_slope', 'num_major_vessels', 'thalassemia']


# variables to transform
LOG_VARIABLES = ['age', 'resting_blood_pressure', 
                 'cholesterol', 'max_heart_rate_achieved', 'st_depression']

# numerical features
NUMERICAL_FEATURES = ['age', 'resting_blood_pressure', 
                      'cholesterol', 'max_heart_rate_achieved', 
                      'st_depression', 'num_major_vessels']

# categorical features
CATEGORICAL_FEATURES = ['sex', 'chest_pain_type', 'fasting_blood_sugar', 
                        'rest_ecg', 'exercise_induced_angina ', 'st_slope ', 
                        'thalassemia']