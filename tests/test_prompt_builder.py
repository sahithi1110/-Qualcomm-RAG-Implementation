from app.core.prompt_builder import build_grounded_prompt


def test_prompt_contains_question_and_source():
    prompt = build_grounded_prompt(
        question="How does RAG work?",
        retrieved_chunks=[
            {
                "source": "rag_process_overview.txt",
                "text": "RAG retrieves context before answering.",
            }
        ],
    )

    assert "How does RAG work?" in prompt
    assert "rag_process_overview.txt" in prompt
    assert "Do not guess" in prompt
