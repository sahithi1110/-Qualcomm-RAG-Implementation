from app.core.rag_service import RAGService


def main() -> None:
    service = RAGService()
    result = service.build_index()

    print("Index build completed.")
    print(f"Documents loaded: {result['documents_loaded']}")
    print(f"Chunks created: {result['chunks_created']}")
    print(f"Collection name: {result['collection_name']}")


if __name__ == "__main__":
    main()
