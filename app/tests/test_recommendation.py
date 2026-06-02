from recommendation_engine import RecommendationEngine

engine = RecommendationEngine()

result = engine.recommend_localities(
    budget=25000000
)

print(result)