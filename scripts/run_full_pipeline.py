from app.core.rag_service import RAGService
from app.core.evaluator import run_evaluation


def main() -> None:
    service = RAGService()

    print("Step 1: Building vector index")
    index_result = service.build_index()
    print(index_result)

    print("\nStep 2: Running demo query")
    question = "How does the RAG system reduce hallucinations?"
    response = service.ask(question)
    print(f"Question: {response['question']}")
    print(f"Answer: {response['answer']}")
    print(f"Sources: {response['sources']}")

    print("\nStep 3: Running evaluation")
    evaluation = run_evaluation()
    print(f"Retrieval Hit Rate: {evaluation['retrieval_hit_rate_percent']}")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()
