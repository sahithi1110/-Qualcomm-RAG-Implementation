from app.core.rag_service import RAGService


def main() -> None:
    service = RAGService()

    question = "How does the RAG system reduce hallucinations?"
    result = service.ask(question)

    print("\nQuestion:")
    print(result["question"])

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")
    for source in result["sources"]:
        print(f"- {source}")

    print("\nRetrieved Context:")
    for item in result["retrieved_context"]:
        print(f"- {item['source']} | Chunk {item['chunk_number']}")


if __name__ == "__main__":
    main()
