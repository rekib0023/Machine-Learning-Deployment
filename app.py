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


@app.route('/', methods=['GET', 'POST'])
def home():
    json_data = {}
    json_data['cylinders'] = 8
    json_data['displacement'] = 307
    json_data['horsepower'] = 130
    json_data['weight'] = 3504
    json_data['acceleration'] = 120
    json_data['model year'] = 70
    json_data['origin'] = 1
    
    return render_template('index.html', json_data=json_data)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = {}
        json_data['cylinders'] = int(request.form['cylinders'])
        json_data['displacement'] = float(request.form['displacement'])
        json_data['horsepower'] = int(request.form['horsepower'])
        json_data['weight'] = int(request.form['weight'])
        json_data['acceleration'] = float(request.form['acceleration'])
        json_data['model year'] = int(request.form['model_year'])
        json_data['origin'] = int(request.form['origin'])

    data = pd.DataFrame(json_data, index=[0], columns=config.FEATURES)
    prediction = pipeline.predict(data)
    result = "The MPG Score for your car is: " + \
        str(np.round(prediction[0])) + "."
    return render_template('index.html', result=result, json_data=json_data)


if __name__ == "__main__":
    app.run(debug=True)
