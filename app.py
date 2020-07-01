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
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = {}
        json_data['age'] = int(request.form['age'])
        json_data['sex'] = str(request.form['sex'])
        json_data['chest_pain_type'] = str(request.form['chest_pain_type'])
        json_data['resting_blood_pressure'] = int(request.form['resting_blood_pressure'])
        json_data['cholesterol'] = int(request.form['cholesterol'])
        json_data['fasting_blood_sugar'] = str(request.form['fasting_blood_sugar'])
        json_data['rest_ecg'] = str(request.form['rest_ecg'])
        json_data['max_heart_rate_achieved'] = int(request.form['max_heart_rate_achieved'])
        json_data['exercise_induced_angina'] = str(request.form['exercise_induced_angina'])
        json_data['st_depression'] = float(request.form['st_depression'])
        json_data['st_slope'] = str(request.form['st_slope'])
        json_data['num_major_vessels'] = int(request.form['num_major_vessels'])
        json_data['thalassemia'] = str(request.form['thalassemia'])
        data = pd.DataFrame(json_data, index=[0], columns=config.FEATURES)
        prediction = pipeline.predict_proba(data)
        result = f'You are {np.round(float(prediction[:, 1]*100), 2)}% likely to have any heart disease'
    return render_template('index.html', result=result)


@app.route('/predict_via_postman', methods=['POST'])
def predict_via_postman():
    if request.method == 'POST':
        json_data = request.get_json()
        data = pd.DataFrame(json_data, index=[0], columns=config.FEATURES)

    prediction = pipeline.predict(data)
    # print(prediction)
    return str(prediction)


if __name__ == "__main__":
    app.run(debug=True)
