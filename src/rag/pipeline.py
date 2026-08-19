from src.retrieval.retriever import Retriever
from src.llm.ollama_llm import LLMManager
from src.rag.context import format_context
from src.rag.prompt import RAG_PROMPT


class RAGPipeline:

    def __init__(
        self,
        persist_directory: str = "vectorstore/chroma",
        model_name: str = "gemma3:1b",
        top_k: int = 4
    ):

        self.top_k = top_k

        self.retriever = Retriever(
            persist_directory=persist_directory
        )

        llm_manager = LLMManager(
            model_name=model_name
        )

        self.llm = llm_manager.get_llm()

    def answer(self, question: str):

        # 1. Retrieve relevant documents
        documents = self.retriever.retrieve(
            question,
            k=self.top_k
        )

        # 2. Convert documents into context
        context = format_context(documents)

        # 3. Build prompt
        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        # 4. Send prompt to LLM
        response = self.llm.invoke(prompt)

        # 5. Return answer and source documents
        return {
            "answer": response.content,
            "documents": documents
        }