import pandas as pd
from pathlib import Path


class DataEngine:

    def __init__(self):

        self.data_path = Path(__file__).parent.parent / "data"

        self.locality_df = None
        self.hotspot_df = None
        self.investment_df = None
        self.kpi_df = None

    def load_data(self):

        print("Loading datasets...")

        self.locality_df = pd.read_csv(
            self.data_path / "locality_analysis.csv"
        )

        self.hotspot_df = pd.read_csv(
            self.data_path / "hotspot_analysis.csv"
        )

        self.investment_df = pd.read_csv(
            self.data_path / "investment_analysis.csv"
        )

        self.kpi_df = pd.read_csv(
            self.data_path / "kpi_data.csv"
        )

        print("Datasets loaded successfully")

    # -----------------------------
    # BASIC SUMMARY
    # -----------------------------

    def get_summary(self):

        return {
            "localities": len(self.locality_df),
            "hotspots": len(self.hotspot_df),
            "investment_records": len(self.investment_df),
            "kpi_records": len(self.kpi_df)
        }

    # -----------------------------
    # TOP INVESTMENT LOCALITIES
    # -----------------------------

    def get_top_investment_localities(self, top_n=10):

        return self.hotspot_df.sort_values(
            by="investment_score",
            ascending=False
        ).head(top_n)

    # -----------------------------
    # TOP LUXURY LOCALITIES
    # -----------------------------

    def get_top_luxury_localities(self, top_n=10):

        return self.hotspot_df.sort_values(
            by="luxury_score",
            ascending=False
        ).head(top_n)

    # -----------------------------
    # TOP EXPENSIVE LOCALITIES
    # -----------------------------

    def get_top_expensive_localities(self, top_n=10):

        return self.locality_df.sort_values(
            by="Avg_Price",
            ascending=False
        ).head(top_n)

    # -----------------------------
    # AVERAGE PROPERTY PRICE
    # -----------------------------

    def get_average_property_price(self):

        return round(
            self.investment_df["price_inr"].mean(),
            2
        )

    # -----------------------------
    # TOP REGIONS
    # -----------------------------

    def get_top_regions(self):

        return (
            self.investment_df
            .groupby("region")["investment_score"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

    # -----------------------------
    # LOCALITY DETAILS
    # -----------------------------

    def get_locality_details(self, locality_name):

        locality_data = self.investment_df[
            self.investment_df["locality"]
            .str.lower()
            ==
            locality_name.lower()
        ]

        if locality_data.empty:
            return None

        return {
            "average_price":
                round(locality_data["price_inr"].mean(), 2),

            "average_luxury_score":
                round(locality_data["luxury_score"].mean(), 2),

            "average_investment_score":
                round(locality_data["investment_score"].mean(), 2),

            "average_connectivity_score":
                round(locality_data["connectivity_score"].mean(), 2),

            "properties":
                len(locality_data)
        }
    
    ## Comparing localities 

    def compare_localities(
        self,
        locality1,
        locality2
    ):

        data1 = self.get_locality_details(
            locality1
        )

        data2 = self.get_locality_details(
            locality2
        )

        if data1 is None or data2 is None:

            return None

        comparison = pd.DataFrame({

            "Metric": [
                "Average Price",
                "Investment Score",
                "Luxury Score",
                "Connectivity Score",
                "Properties"
            ],

            locality1: [
                data1["average_price"],
                data1["average_investment_score"],
                data1["average_luxury_score"],
                data1["average_connectivity_score"],
                data1["properties"]
            ],

            locality2: [
                data2["average_price"],
                data2["average_investment_score"],
                data2["average_luxury_score"],
                data2["average_connectivity_score"],
                data2["properties"]
            ]

        })

        return comparison