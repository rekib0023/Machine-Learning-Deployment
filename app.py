# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:27:28 2020

@author: rkbra
"""

from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import joblib
import config

pipeline = joblib.load(filename=config.PIPELINE_NAME)

app = Flask(__name__)


@app.route('/predict_via_postman', methods=['POST'])
def predict_via_postman():
    # print("hello")
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0], columns=config.FEATURES)

    prediction = pipeline.predict(data)
    # print(prediction)
    return str(prediction)


if __name__ == "__main__":
    app.run(debug=True)
