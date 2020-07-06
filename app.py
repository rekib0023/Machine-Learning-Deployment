# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:50:55 2020

@author: rkbra
"""

from flask import Flask, request, render_template
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
    json_data = {}
    if request.method == 'POST':
        json_data['age'] = int(request.form['age'])
        if str(request.form['gender']) == 'male':
            json_data['gender_male'] = 1
        else:
            json_data['gender_male'] = 0
        json_data['height'] = float(request.form['height'])
        json_data['weight'] = float(request.form['weight'])
        json_data['systolic_blood_pressure'] = float(request.form['systolic_blood_pressure'])
        json_data['diastolic_blood_pressure'] = float(request.form['diastolic_blood_pressure'])
        if str(request.form['cholesterol']) == 'normal':
            json_data['cholesterol_normal'] = 1
            json_data['cholesterol_well above normal'] = 0
        elif str(request.form['cholesterol']) == 'well above normal':
            json_data['cholesterol_normal'] = 0
            json_data['cholesterol_well above normal'] = 1
        else:
            json_data['cholesterol_normal'] = 0
            json_data['cholesterol_well above normal'] = 0
        if str(request.form['glucose_level']) == 'normal':
            json_data['glucose_level_normal'] = 1
            json_data['glucose_level_well above normal'] = 0
        elif str(request.form['glucose_level']) == 'well above normal':
            json_data['glucose_level_normal'] = 0
            json_data['glucose_level_well above normal'] = 1
        else:
            json_data['glucose_level_normal'] = 0
            json_data['glucose_level_well above normal'] = 0
        if str(request.form['smoking']) == 'yes':
            json_data['smoking_yes'] = 1
        else:
            json_data['smoking_yes'] = 0
        if str(request.form['alcohol_intake']) == 'yes':
            json_data['alcohol_intake_yes'] = 1
        else:
            json_data['alcohol_intake_yes'] = 0
        if str(request.form['physical_activity']) == 'yes':
            json_data['physical_activity_yes'] = 1
        else:
            json_data['physical_activity_yes'] = 0
    
    data = pd.DataFrame(json_data, index=[0], columns=config.FEATURES_AFTER_ENCODING)
    predict_proba = pipeline.predict_proba(data)[:,1]
    
    if predict_proba > .25:
        result = f'You have a risk of having cardio vascular disease!'
    elif predict_proba > .5:
        result = f'You have a high risk of having cardio vascular disease!'
    else:
        result = f'You do not seem to have any high risk of having cardio vascular disease.'
        
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)