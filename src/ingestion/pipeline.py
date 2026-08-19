from src.ingestion.loader import load_pdf
from src.ingestion.splitter import split_documents


def ingest_pdf(
    file_path: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
):
    """
    Complete PDF ingestion pipeline.

    PDF
    ↓
    Documents
    ↓
    Chunks
    """

    documents = load_pdf(file_path)

    chunks = split_documents(
        documents,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    return chunks