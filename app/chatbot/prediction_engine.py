import joblib
import pandas as pd
from pathlib import Path


class PredictionEngine:

    def __init__(self):

        self.model = None
        self.label_encoders = None

        self.model_path = (
            Path(__file__).resolve().parent.parent.parent
            / "models"
            / "final_lightgbm_model.pkl"
        )

        self.encoder_path = (
            Path(__file__).resolve().parent.parent.parent
            / "models"
            / "label_encoders.pkl"
        )

    def load_model(self):

        print("Loading LightGBM model...")

        self.model = joblib.load(
            self.model_path
        )

        self.label_encoders = joblib.load(
            self.encoder_path
        )

        print("Model loaded successfully")

    def preprocess_input(self, property_data):

        df = pd.DataFrame([property_data])

        categorical_cols = [
            'region',
            'tier',
            'property_type',
            'furnishing',
            'parking',
            'builder_tier'
        ]

        for col in categorical_cols:

            encoder = self.label_encoders[col]

            df[col] = encoder.transform(
                [str(df[col].iloc[0])]
            )

        return df

    def predict_price(self, property_data):

        df = self.preprocess_input(
            property_data
        )

        prediction = self.model.predict(df)

        return round(prediction[0], 2)