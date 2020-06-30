# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:06:25 2020

@author: rkbra
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

import preprocessing as pp
import config


pipeline = Pipeline(
    [
        ('log_transformer', pp.LogTransformer(variables=config.LOG_VARIABLES)),
        ('dummy_variables', pp.GetDummyVariables(variables=config.CATEGORICAL_FEATURES)),
        ('rf', RandomForestClassifier(max_depth=7, min_samples_leaf=2))
    ]
)
 