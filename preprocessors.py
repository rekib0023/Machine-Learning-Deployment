# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:57:58 2020

@author: rkbra
"""

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin, clone


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


class AveragingModels(BaseEstimator, TransformerMixin):
    def __init__(self, models):
        self.models = models

    # we define clones of the original models to fit the data in
    # the reason of clone is avoiding affect the original base models
    def fit(self, X, y):
        self.models_ = [clone(x) for x in self.models]
        # Train cloned base models
        for model in self.models_:
            model.fit(X, y)
        return self

    # Now we do the predictions for cloned models and average them
    def predict(self, X):
        predictions = np.column_stack(
            [model.predict(X) for model in self.models_])
        return np.mean(predictions, axis=1)
