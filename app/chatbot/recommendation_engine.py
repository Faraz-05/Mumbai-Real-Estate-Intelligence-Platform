from chatbot.data_engine import DataEngine
# from data_engine import DataEngine

class RecommendationEngine:

    def __init__(self):

        self.data_engine = DataEngine()

        self.data_engine.load_data()

    def recommend_localities(
        self,
        region=None,
        budget=None,
        top_n=5
    ):

        df = self.data_engine.investment_df.copy()

        # Filter by budget
        if budget is not None:

            lower = budget * 0.7
            upper = budget * 1.3

            df = df[
                (df["price_inr"] >= lower)
                &
                (df["price_inr"] <= upper)
            ]

        recommendations = (

            df.groupby("locality")
            .agg({
                "investment_score": "mean",
                "price_inr": "mean",
                "luxury_score": "mean"
            })
            .reset_index()

            .sort_values(
                by="investment_score",
                ascending=False
            )
            .head(top_n)
        )

        return recommendations