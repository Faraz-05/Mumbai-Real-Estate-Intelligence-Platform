from data_engine import DataEngine

engine = DataEngine()
engine.load_data()

print("\nLOCALITY")
print(engine.locality_df.columns)

print("\nHOTSPOT")
print(engine.hotspot_df.columns)

print("\nINVESTMENT")
print(engine.investment_df.columns)

print("\nKPI")
print(engine.kpi_df.columns)