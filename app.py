# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 19:46:17 2022

@author: Dell
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('Project6.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = float(request.args.get('exp1'))
    exp2= float(request.args.get('exp2'))
    exp3= float(request.args.get('exp3'))
    exp4= float(request.args.get('exp4'))
    exp5 = float(request.args.get('exp5'))
    exp6 = float(request.args.get('exp6'))
    exp7 = float(request.args.get('exp7'))
    exp8 = float(request.args.get('exp8'))
    
    prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8]])
    
    if prediction==[1]:
      prediction='Yes'
    else:
      prediction='No'

        
    return render_template('index.html', prediction_text=' Placement prediction according to model is : {}'.format(prediction))




if __name__ == "__main__":
    app.run(debug=True)