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

    form_values = [ x for x in request.form.values()]
    
    print()
    print()
    print(form_values)
    
    mapper = {'Direct' :  0,'Network' : 1,'Organic' : 2,
     'Ahmedabad' : 0,'Bangalore' : 1,'Cochin' : 2,'Chandigarh' : 3,'Chennai' : 4,'Delhi' : 5,
     'Hyderabad' : 6,'Kolkata' : 7,'Mumbai' : 8,'New Delhi' : 9,'Surat' : 10,
     'Female' : 0,'Male' : 1, 'None' : 0,'Base' : 1,'Silver' : 2,'Gold' : 3,'Platinum' : 4,
    'Yes' : 1, 'No' : 0}
    
    cat = [1,2,4,5,7,8]
    
    for i in cat:
        form_values[i] = mapper[form_values[i]]
                      
    for j in range(0,len(form_values)):
        form_values[j] = int(form_values[j])
     
    print()
    print()
    print(form_values)    
    
    pred = model.predict([np.array(form_values)])
    
    if pred == 1:
        return render_template('index.html', prediction_text = 'Potential Customer')
    else:
        return render_template('index.html', prediction_text = 'Not a Potential Customer')


if __name__ == "__main__":
    app.run(debug = True)