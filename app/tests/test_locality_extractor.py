from locality_extractor import LocalityExtractor

extractor = LocalityExtractor()

questions = [

    "Should I invest in Powai?",

    "Tell me about Worli",

    "Is Bandra West expensive?",

    "What is the future of Malabar Hill?"

]

for q in questions:

    locality = extractor.extract_locality(q)

    print(f"\nQuestion: {q}")

    print(f"Locality Found: {locality}")