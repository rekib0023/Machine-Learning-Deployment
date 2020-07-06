# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 05:43:17 2020

@author: rkbra
"""

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin



class LogTransformer(BaseEstimator, TransformerMixin):
    """Log transformation of the skewed numerical features"""

    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()

        for var in self.variables:
            if var in ['systolic_blood_pressure', 'diastolic_blood_pressure']:
                variance = np.var(X[var])
                X[var] = X[var].apply(lambda x: (variance + x)**2)
            X[var] = np.log1p(X[var])
        return X
    

class CategoricalEncoding(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables
            
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X = X.copy()
        X = pd.get_dummies(X, drop_first=True)
        return X
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    