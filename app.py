from flask import Flask, render_template, request, jsonify
import numpy as np
from model import predict_fraud

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/lavisha')
def lavisha():
    return render_template('lavisha.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/comparison')
def comparison():
    return render_template('comparison.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form[f'feature{i}']) for i in range(30)]
        prediction = predict_fraud(np.array([data]))
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
