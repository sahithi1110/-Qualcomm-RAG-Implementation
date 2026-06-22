# Interview Explanation

I built this project to demonstrate how I would design a RAG-based LLM system for enterprise knowledge support.

The main goal was to reduce hallucinations by making sure the system retrieves approved context before answering. I used sample enterprise documents, cleaned and chunked them, generated embeddings, stored them in ChromaDB, and built retrieval logic to find the most relevant content for each question.

I also added a FastAPI layer so the system can be tested through Swagger. The API returns the answer, retrieved sources, context chunks, and grounded prompt. This makes the system easier to review and debug.

I included evaluation queries to check whether the expected document appears in the retrieved sources. This is important because a RAG system should not only generate answers, it should also prove that it is retrieving the right context.

Since this is a sanitized project, I did not include any confidential data or production credentials. The project is designed to show my understanding of RAG architecture, retrieval quality, LLM grounding, API development, and AI quality evaluation.
