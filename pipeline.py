# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:07:44 2020

@author: rkbra
"""

from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

import preprocessors as pp
import config

model_xgb = xgb.XGBRegressor(objective="reg:squarederror", max_depth=5,
                             min_child_weight=4, subsample=0.7,
                             n_estimator=1000, learning_rate=0.07)

rf = RandomForestRegressor(random_state=101, n_estimators=200)

lasso = Lasso(alpha=0.0028072162039411755, max_iter=10000, random_state=42)


pipeline = Pipeline(
    [
        ('log_transformer', pp.LogTransformer(variables=config.VARIABLE_LOG)),
        ('regression_model', pp.AveragingModels(models=(model_xgb, rf, lasso)))
    ]
)
