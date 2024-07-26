from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application  = Flask(__name__)
app =application

# Import ridge model and standard scaler
ridge_model = pickle.load(open("models/ridge.pkl","rb"))
standard_scaler= pickle.load(open("models/scaler.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")

if __name__ =="__main__":
    application.run(host="0.0.0.0")
