from llm_engine import LLMEngine


engine = LLMEngine()

response = engine.ask(
    "Why is Bandra West expensive?"
)

print(response)