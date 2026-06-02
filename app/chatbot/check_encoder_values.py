import joblib

encoders = joblib.load(
    "../models/label_encoders.pkl"
)

for col, encoder in encoders.items():

    print("\n", col)
    print(encoder.classes_)