from query_router import QueryRouter


router = QueryRouter()

while True:

    question = input(
        "\nAsk a question: "
    )

    if question.lower() == "exit":
        break

    answer = router.route(
        question
    )

    print("\n")
    print(answer)