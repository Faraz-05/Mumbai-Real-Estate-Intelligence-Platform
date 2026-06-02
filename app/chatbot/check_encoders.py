import joblib

encoders = joblib.load(
    "../models/label_encoders.pkl"
)

print(encoders.keys())