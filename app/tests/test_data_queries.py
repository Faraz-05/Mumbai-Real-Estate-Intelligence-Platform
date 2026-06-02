from data_engine import DataEngine

engine = DataEngine()

engine.load_data()

print("\nTOP INVESTMENT LOCALITIES")
print(
    engine.get_top_investment_localities()
)

print("\nTOP LUXURY LOCALITIES")
print(
    engine.get_top_luxury_localities()
)

print("\nAVERAGE PROPERTY PRICE")
print(
    engine.get_average_property_price()
)

print("\nTOP REGIONS")
print(
    engine.get_top_regions()
)

print("\nPOWAI DETAILS")
print(
    engine.get_locality_details("Powai")
)