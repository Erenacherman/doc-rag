import os

from dotenv import load_dotenv

from src.llm.cloud_llm import CloudLLM


load_dotenv()


def create_llm():

    provider = os.getenv(
        "LLM_PROVIDER",
        "openrouter"
    ).lower()

    print()
    print("=" * 60)
    print("LLM PROVIDER")
    print("=" * 60)

    if provider == "openrouter":

        print("☁️ Using OpenRouter Cloud LLM")
        print("🚫 Ollama will NOT be used")

        return CloudLLM()

    else:

        raise ValueError(
            f"Unknown LLM_PROVIDER: {provider}\n"
            f"Currently supported: openrouter"
        )