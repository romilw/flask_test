import pickle
lr = pickle.load(open("lr_c35.pkl","rb"))

import numpy as np
from flask import Flask,request,render_template
app =Flask(__name__)


@app.route("/")
def homepage():
	return render_template("index.html")
	

@app.route("/predict",methods=['POST'])
def predict():
    pre_sal = lr.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html",prediction_text = "your Salary is "+str(pre_sal[0]))
    
    
    
app.run(port=5005,debug=True)
