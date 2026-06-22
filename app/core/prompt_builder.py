def build_grounded_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    context_lines = []

    for chunk in retrieved_chunks:
        context_lines.append(
            f"Source: {chunk['source']}\nContent: {chunk['text']}"
        )

    context = "\n\n".join(context_lines)

    prompt = f'''
You are helping answer an enterprise knowledge question.

Use only the context below.
Do not guess.
If the answer is not in the context, say: "The information is not available in the provided context."

Context:
{context}

Question:
{question}

Answer:
'''.strip()

    return prompt
