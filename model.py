import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

def predict_fraud(data):
    return model.predict(data)[0]
