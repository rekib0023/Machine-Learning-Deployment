# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:06:25 2020

@author: rkbra
"""

from sklearn.linear import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import preprocessing as pp
import config


pipeline = Pipeline(
    [
        ('log_transformer', pp.LogTransformer(variables=config.VARIABLE_LOG)),
        ('dummy_variables', pp.GetDummyVariables(variables=config.CATEGORICAL_FEATURES)),
        ('std_scaler', StandardScaler()),
        ('lr', LogisticRegression(random_state=42))
    ]
)
 