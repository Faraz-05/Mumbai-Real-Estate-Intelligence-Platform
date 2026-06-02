from llm_engine import LLMEngine

engine = LLMEngine()

question = input(
    "Ask a question: "
)

response = engine.answer_question(
    question
)

print("\n")
print(response)