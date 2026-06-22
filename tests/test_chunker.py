from app.core.chunker import clean_text, split_text_into_chunks, create_document_chunks


def test_clean_text_removes_extra_spacing():
    text = "This   is a test.\nThis is another line."
    assert clean_text(text) == "This is a test. This is another line."


def test_split_text_into_chunks_returns_chunks():
    text = "A" * 1200
    chunks = split_text_into_chunks(text, chunk_size=300, overlap=50)

    assert len(chunks) > 1
    assert all(len(chunk) <= 300 for chunk in chunks)


def test_create_document_chunks_adds_source_information():
    documents = [{"source": "sample.txt", "text": "This is a simple sample document."}]
    chunks = create_document_chunks(documents, chunk_size=100, overlap=10)

    assert chunks[0]["source"] == "sample.txt"
    assert chunks[0]["chunk_number"] == 1
