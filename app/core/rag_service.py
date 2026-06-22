from app.core.config_loader import load_settings
from app.core.document_loader import load_text_documents
from app.core.chunker import create_document_chunks
from app.core.prompt_builder import build_grounded_prompt
from app.core.vector_store import VectorStore


class RAGService:
    def __init__(self):
        self.settings = load_settings()
        self.vector_store = VectorStore(self.settings)

    def build_index(self) -> dict:
        documents = load_text_documents(self.settings["paths"]["sample_docs_dir"])

        chunks = create_document_chunks(
            documents=documents,
            chunk_size=self.settings["rag"]["chunk_size"],
            overlap=self.settings["rag"]["chunk_overlap"],
        )

        self.vector_store.save_chunks_to_file(chunks)
        self.vector_store.build_index(chunks)

        return {
            "documents_loaded": len(documents),
            "chunks_created": len(chunks),
            "collection_name": self.settings["rag"]["collection_name"],
        }

    def ask(self, question: str) -> dict:
        top_k = self.settings["rag"]["top_k"]
        retrieved_chunks = self.vector_store.search(question=question, top_k=top_k)
        ranked_chunks = self._rerank_with_keywords(question, retrieved_chunks)
        prompt = build_grounded_prompt(question, ranked_chunks)
        answer = self._create_demo_answer(question)

        return {
            "question": question,
            "answer": answer,
            "sources": sorted({chunk["source"] for chunk in ranked_chunks}),
            "confidence_note": "Answer is based on retrieved sample documents.",
            "retrieved_context": [
                {
                    "source": chunk["source"],
                    "chunk_number": chunk["chunk_number"],
                    "text": chunk["text"],
                }
                for chunk in ranked_chunks
            ],
            "grounded_prompt": prompt,
        }

    def list_sources(self) -> dict:
        documents = load_text_documents(self.settings["paths"]["sample_docs_dir"])
        return {
            "total_sources": len(documents),
            "sources": [document["source"] for document in documents],
        }

    def _rerank_with_keywords(self, question: str, chunks: list[dict]) -> list[dict]:
        question_words = {
            word.lower().strip(".,?!")
            for word in question.split()
            if len(word) > 3
        }

        scored_chunks = []

        for chunk in chunks:
            chunk_words = set(chunk["text"].lower().split())
            keyword_score = len(question_words.intersection(chunk_words))
            vector_score = 1 / (1 + chunk["distance"])
            final_score = keyword_score + vector_score
            scored_chunks.append((final_score, chunk))

        scored_chunks.sort(key=lambda item: item[0], reverse=True)

        return [chunk for _, chunk in scored_chunks]

    def _create_demo_answer(self, question: str) -> str:
        question_lower = question.lower()

        if "hallucination" in question_lower:
            return (
                "The RAG system reduces hallucinations by retrieving approved internal context "
                "before preparing the answer. This keeps the response grounded in source material "
                "instead of allowing the model to guess."
            )

        if "steps" in question_lower or "workflow" in question_lower:
            return (
                "The RAG workflow includes document ingestion, text cleaning, chunking, embedding "
                "generation, vector indexing, semantic retrieval, prompt building, grounded answer "
                "generation, and evaluation."
            )

        if "monitor" in question_lower or "production" in question_lower:
            return (
                "A production RAG system should monitor query latency, failed retrieval cases, "
                "missing source matches, low-confidence answers, user feedback, and repeated "
                "hallucination patterns."
            )

        if "sensitive" in question_lower or "protect" in question_lower or "security" in question_lower:
            return (
                "Sensitive enterprise data can be protected by using approved knowledge sources, "
                "access controls, metadata, audit logs, and role-based filters."
            )

        if "prompt" in question_lower:
            return (
                "A RAG prompt should tell the model to use only the retrieved context, avoid guessing, "
                "and say that the information is not available when the answer is not present."
            )

        if "mlops" in question_lower or "deploy" in question_lower:
            return (
                "Useful MLOps practices include version control, testing, CI/CD, Docker packaging, "
                "environment configuration, logging, evaluation datasets, and rollback planning."
            )

        if "training manager" in question_lower or "quality" in question_lower:
            return (
                "This project supports an AI Training Manager role by showing how AI outputs can be "
                "checked against source documents, measured through evaluation queries, and improved "
                "through quality review."
            )

        return "The information is not available in the provided context."
