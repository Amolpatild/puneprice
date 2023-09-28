from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import os
import util
import flask_cors
from flask_cors import CORS, cross_origin

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['new_total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    print(total_sqft)
    print(location)
    print(bhk)
    print(bath)

    response = jsonify({
        'estimated_price': util.get_estimated_price(total_sqft, bath, bhk,location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # app.run(host='0.0.0.0', port=8080) #local host
    # # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80) #for AZURE