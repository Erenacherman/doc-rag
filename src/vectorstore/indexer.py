from src.ingestion.pipeline import ingest_pdf
from src.embeddings.embedder import EmbeddingManager
from src.vectorstore.chroma_store import VectorStoreManager


def index_pdf(
    file_path: str,
    persist_directory: str = "vectorstore/chroma"
):

    # 1. Load and split PDF
    chunks = ingest_pdf(file_path)

    # 2. Create embedding manager
    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.get_embeddings()

    # 3. Create vector store
    vector_store = VectorStoreManager(
        embedding_function=embeddings,
        persist_directory=persist_directory
    )

    # 4. Store chunks and their embeddings
    vector_store.add_documents(chunks)

    return vector_store