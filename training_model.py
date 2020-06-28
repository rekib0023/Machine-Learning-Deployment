# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:16:52 2020

@author: rkbra
"""

import pandas as pd
from pipeline import pipeline
import config
import joblib
from sklearn.model_selection import train_test_split

import warnings
warnings.simplefilter(action='ignore')


def run_training():
    """ Train the model"""
    
    # read and clean the training data
    data = pd.read_csv(config.TRAINING_DATA_FILE)
    
    
    pipeline.fit(data[config.FEATURES], data[config.TARGET])
    joblib.dump(pipeline, config.PIPELINE_NAME, compress=('zlib',9))
    

if __name__ == '__main__':
    run_training()
