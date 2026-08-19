from langchain_chroma import Chroma


class VectorStoreManager:

    def __init__(
        self,
        embedding_function,
        persist_directory: str = "vectorstore/chroma"
    ):

        self.persist_directory = persist_directory

        self.vector_store = Chroma(
            collection_name="docchat_documents",
            embedding_function=embedding_function,
            persist_directory=persist_directory
        )

    def add_documents(self, documents):

        self.vector_store.add_documents(
            documents
        )

    def similarity_search(
        self,
        query,
        k=4
    ):

        return self.vector_store.similarity_search(
            query,
            k=k
        )

    def similarity_search_with_score(
        self,
        query,
        k=4
    ):

        return self.vector_store.similarity_search_with_score(
            query,
            k=k
        )