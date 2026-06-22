from pathlib import Path
import json

import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, settings: dict):
        self.settings = settings
        self.model_name = settings["embedding"]["model_name"]
        self.collection_name = settings["rag"]["collection_name"]
        self.vector_store_path = settings["paths"]["vector_store_path"]

        self.model = SentenceTransformer(self.model_name)
        self.client = chromadb.PersistentClient(path=self.vector_store_path)
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def save_chunks_to_file(self, chunks: list[dict]) -> None:
        output_file = Path(self.settings["paths"]["chunk_output_file"])
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with output_file.open("w", encoding="utf-8") as file:
            for chunk in chunks:
                file.write(json.dumps(chunk) + "\n")

    def build_index(self, chunks: list[dict]) -> None:
        if not chunks:
            raise ValueError("No chunks found to index.")

        ids = [chunk["chunk_id"] for chunk in chunks]
        texts = [chunk["text"] for chunk in chunks]
        metadata = [
            {"source": chunk["source"], "chunk_number": chunk["chunk_number"]}
            for chunk in chunks
        ]

        embeddings = self.model.encode(texts).tolist()

        self.collection.upsert(
            ids=ids,
            documents=texts,
            metadatas=metadata,
            embeddings=embeddings,
        )

    def search(self, question: str, top_k: int) -> list[dict]:
        question_embedding = self.model.encode([question]).tolist()[0]

        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        retrieved = []

        for text, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            retrieved.append(
                {
                    "source": metadata["source"],
                    "chunk_number": metadata["chunk_number"],
                    "text": text,
                    "distance": float(distance),
                }
            )

        return retrieved
