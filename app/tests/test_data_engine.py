from data_engine import DataEngine

engine = DataEngine()

engine.load_data()

print(engine.get_summary())