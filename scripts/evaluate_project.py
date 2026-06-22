from app.core.evaluator import run_evaluation


def main() -> None:
    result = run_evaluation()

    print("Evaluation completed.")
    print(f"Total questions: {result['total_questions']}")
    print(f"Successful hits: {result['successful_hits']}")
    print(f"Retrieval Hit Rate: {result['retrieval_hit_rate_percent']}")

    print("\nDetailed Results:")
    for item in result["results"]:
        print("-" * 60)
        print(f"Question: {item['question']}")
        print(f"Expected Source: {item['expected_source']}")
        print(f"Retrieved Sources: {item['retrieved_sources']}")
        print(f"Hit: {item['hit']}")


if __name__ == "__main__":
    main()
