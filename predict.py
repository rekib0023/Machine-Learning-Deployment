# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:51:57 2020

@author: rkbra
"""

import pandas as pd
import config
import joblib

import warnings

warnings.simplefilter(action='ignore')


def make_prediction(input_data):
    _pipeline = joblib.load(filename=config.PIPELINE_NAME)

    results = _pipeline.predict(input_data)
    results_proba = _pipeline.predict_proba(input_data)

    return results, results_proba


if __name__ == '__main__':
    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix, roc_curve, auc

    print("Reading data...")
    data = pd.read_csv(config.TRAINING_DATA_FILE)

    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.33,
        random_state=0)

    print("Making prediction...")
    pred, pred_proba = make_prediction(X_test)
    print("Prediction made")

    # determine mse and rmse
    conf_matrix = confusion_matrix(y_test, pred)

    total = sum(sum(conf_matrix))

    sensitivity = conf_matrix[0, 0] / (conf_matrix[0, 0] + conf_matrix[1, 0])
    print('Sensitivity : ', sensitivity)

    specificity = conf_matrix[1, 1] / (conf_matrix[1, 1] + conf_matrix[0, 1])
    print('Specificity : ', specificity)

    fpr, tpr, thresholds = roc_curve(y_test, pred_proba[:, 1])
    print('AUC Score :', auc(fpr, tpr))
