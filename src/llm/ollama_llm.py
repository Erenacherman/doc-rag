from langchain_ollama import ChatOllama


class LLMManager:

    def __init__(
        self,
        model_name: str = "gemma3:1b",
        temperature: float = 0
    ):

        self.model_name = model_name
        self.temperature = temperature

        self.llm = ChatOllama(
            model=model_name,
            temperature=temperature
        )

    def get_llm(self):

        return self.llm