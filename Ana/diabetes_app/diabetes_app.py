import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

# Create Flask app
app = Flask(__name__, template_folder="templates", static_folder="sta")

# Load your pickle model
model = pickle.load(open('models/model.pkl', 'rb'))

# Create routes

@app.route('/')
def home():
    """Serve homepage template."""
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]  
    prediction = model.predict(features) 
    result = prediction[0]

    return render_template('index.html', prediction=result)



if __name__ == "__main__":
    app.run(debug=True)