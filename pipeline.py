# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 05:53:08 2020

@author: rkbra
"""

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.pipeline import Pipeline

import preprocessors as pp
import config


# define the base models
level0 = list()
level0.append(('lr', LogisticRegression(random_state=42)))
level0.append(('svm', SVC(C=10, gamma=0.01, probability=True, random_state=42)))
level0.append(('rf', RandomForestClassifier(max_depth=10, min_samples_leaf=5, min_samples_split=5,
                   n_estimators=1000, random_state=42)))

# define meta learner model
level1 = LogisticRegression()


pipeline = Pipeline(
    [
        ('log_transformer', pp.LogTransformer(variables=config.NUMERICAL_FEATURES)),
        ('classification_model', StackingClassifier(estimators=level0, final_estimator=level1, n_jobs=1))
    ]
)
