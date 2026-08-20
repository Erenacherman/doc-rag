class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(
        self,
        query,
        k=4,
        progress_callback=None
    ):

        # -----------------------------------------
        # 1. Start search
        # -----------------------------------------

        if progress_callback:
            progress_callback(
                45,
                "🔎 Searching vector database..."
            )

        # -----------------------------------------
        # 2. Similarity search
        # -----------------------------------------

        documents = self.vector_store.similarity_search(
            query,
            k=k
        )

        # -----------------------------------------
        # 3. Search completed
        # -----------------------------------------

        if progress_callback:
            progress_callback(
                60,
                f"✅ Retrieved {len(documents)} relevant chunks"
            )

        return documents