import shap
import pandas as pd
import matplotlib.pyplot as plt

class ExplainabilityEngine:

    def __init__(self, prediction_engine):

        self.prediction_engine = prediction_engine

        print("Loading model for SHAP...")

        self.explainer = shap.TreeExplainer(
            prediction_engine.model
        )

        print("SHAP ready")

    def get_shap_values(self, property_data):

        df = self.prediction_engine.preprocess_input(
            property_data
        )

        shap_values = self.explainer.shap_values(df)

        return shap_values, df

    def get_feature_importance(self, property_data):

        shap_values, df = self.get_shap_values(
            property_data
        )

        feature_names = df.columns

        contributions = pd.DataFrame({

            "Feature": feature_names,

            "Impact": shap_values[0]

        })

        contributions = contributions.sort_values(
            by="Impact",
            ascending=False
        )

        return contributions

    def get_top_explanations(self, property_data):

        contributions = self.get_feature_importance(
            property_data
        )

        positive = contributions.head(5)

        negative = contributions.sort_values(
            by="Impact"
        ).head(5)

        return {

            "positive": positive,

            "negative": negative

        }
    
    def create_waterfall_plot(self, property_data):

        df = self.prediction_engine.preprocess_input(
            property_data
        )

        shap_values = self.explainer(df)

        plt.figure(figsize=(10, 6))

        shap.plots.waterfall(
            shap_values[0],
            show=False
        )

        return plt.gcf()