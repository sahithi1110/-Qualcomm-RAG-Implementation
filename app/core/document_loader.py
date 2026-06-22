from pathlib import Path


def load_text_documents(folder_path: str) -> list[dict]:
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Document folder not found: {folder_path}")

    documents = []

    for file_path in sorted(folder.glob("*.txt")):
        text = file_path.read_text(encoding="utf-8").strip()

        if text:
            documents.append({"source": file_path.name, "text": text})

    return documents
