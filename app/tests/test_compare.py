from data_engine import DataEngine

engine = DataEngine()

engine.load_data()

result = engine.compare_localities(
    "Powai",
    "Worli"
)

print(result)