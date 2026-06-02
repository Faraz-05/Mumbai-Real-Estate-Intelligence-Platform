from prediction_engine import PredictionEngine
from explainability_engine import ExplainabilityEngine


prediction_engine = PredictionEngine()

prediction_engine.load_model()


explainer = ExplainabilityEngine(
    prediction_engine
)


sample_property = {

    "region": "Western",
    "tier": "premium",
    "property_type": "2BHK",
    "bedrooms": 2,
    "carpet_area_sqft": 900,
    "built_up_area_sqft": 1100,
    "floor": 12,
    "total_floors": 30,
    "property_age": 5,
    "furnishing": "semi_furnished",
    "parking": "1_covered",
    "balconies": 2,
    "builder_tier": "tier1",
    "metro_distance_min": 5,
    "to_bkc_km": 7,
    "to_nariman_point_km": 18,
    "luxury_score": 3,
    "connectivity_score": 80
}


results = explainer.get_top_explanations(
    sample_property
)


print("\nTOP POSITIVE FACTORS")
print(results["positive"])

print("\nTOP NEGATIVE FACTORS")
print(results["negative"])