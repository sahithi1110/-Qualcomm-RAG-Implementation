import re


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_text_into_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    cleaned_text = clean_text(text)

    if len(cleaned_text) <= chunk_size:
        return [cleaned_text]

    chunks = []
    start = 0

    while start < len(cleaned_text):
        end = start + chunk_size
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks


def create_document_chunks(documents: list[dict], chunk_size: int, overlap: int) -> list[dict]:
    all_chunks = []

    for document in documents:
        chunks = split_text_into_chunks(
            text=document["text"],
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for index, chunk_text in enumerate(chunks, start=1):
            all_chunks.append(
                {
                    "chunk_id": f"{document['source'].replace('.txt', '')}_{index}",
                    "source": document["source"],
                    "text": chunk_text,
                    "chunk_number": index,
                }
            )

    return all_chunks
