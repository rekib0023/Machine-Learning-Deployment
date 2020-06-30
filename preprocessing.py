# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:57:47 2020

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
            X[var] = np.log1p(X[var])
        return X
    

class GetDummyVariables(BaseEstimator, TransformerMixin):
    """Getting dummy variables for the categorical features"""
    
        def __init__(self, variables=None):
            if not isinstance(variables, list):
                self.variables = [variables]
            else:
                self.variables = variables
    
        def fit(self, X, y=None):
            return self
        
        def transform(self, X, y=None):
            X = X.copy()
            
            return pd.get_dummies(X, drop_first=True)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        