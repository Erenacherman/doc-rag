from src.embeddings.embedder import EmbeddingManager
from src.vectorstore.chroma_store import VectorStoreManager


class Retriever:

    def __init__(
        self,
        persist_directory: str = "vectorstore/chroma"
    ):

        embedding_manager = EmbeddingManager()

        embeddings = embedding_manager.get_embeddings()

        self.vector_store = VectorStoreManager(
            embedding_function=embeddings,
            persist_directory=persist_directory
        )

    def retrieve(self, query: str, k: int = 4):

        return self.vector_store.similarity_search(
            query,
            k=k
        )

    def retrieve_with_scores(
        self,
        query: str,
        k: int = 4
    ):

        return self.vector_store.similarity_search_with_score(
            query,
            k=k
        )