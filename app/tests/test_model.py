import joblib

model = joblib.load("../models/final_lightgbm_model.pkl")

print(type(model))

try:
    print(model.feature_name_)
except:
    print("feature_name_ not available")

try:
    print(model.feature_names_in_)
except:
    print("feature_names_in_ not available")