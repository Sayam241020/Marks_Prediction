from copyreg import pickle
from crypt import methods
from django.shortcuts import render
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
regmodel=pickle.load(open('regmodel.pkl','rb'))

@app.route('/')

def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(-1,1))
    output=regmodel.predict(data)
    print(output[0])
@app.route('/predict',methods=['POST'])

def predict():
    data=[float(x) for x in request.form.values()]
    print(data)
    output=regmodel.predict(data)[0]
    return render_template("home.html",Prediction_text="the house price")