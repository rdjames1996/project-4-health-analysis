#!/usr/bin/env python
# coding: utf-8

# ## Preprocessing

# In[1]:
import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

# In[1]:
# Create Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
app
# In[1]:
# Load your pickle model
model = pickle.load(open('models/model.pkl', 'rb'))

# In[1]: # Create routes
@app.route('/')
def home():
    """Serve homepage template."""
    return render_template('index.html')

# In[1]:
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  
    prediction = model.predict(features) 
    result = prediction[0]

    return render_template('index.html', prediction=result)


# In[1]:
if __name__ == "__main__":
    app.run(debug=False)

# %%
