# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 23:54:15 2020

@author: Gowtham Muruganandam
"""

import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("finalized_model.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    try:
        form_values = [ x for x in request.form.values()]
        for j in range(0,len(form_values)):
            form_values[j] = int(form_values[j])
        pred = model.predict([np.array(form_values)])
    
        if pred == 1:
            return render_template('index.html', prediction_text = 'Potential Customer')
        else:
            return render_template('index.html', prediction_text = 'Not a Potential Customer')
    except:
        return render_template('index.html', prediction_text = 'Please fill all the fields')
    

if __name__ == "__main__":
    app.run(debug = True)
