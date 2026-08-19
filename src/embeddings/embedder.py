from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingManager:

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    ):
        self.model_name = model_name

        self.embeddings = HuggingFaceEmbeddings(
            model_name=model_name
        )

    def get_embeddings(self):
        return self.embeddings