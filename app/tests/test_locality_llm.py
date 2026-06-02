from llm_engine import LLMEngine


engine = LLMEngine()

response = engine.ask_locality_question(
    "Powai",
    "Should I invest in Powai?"
)

print(response)