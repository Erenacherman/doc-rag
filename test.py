from src.llm.cloud_llm import CloudLLM


llm = CloudLLM()

answer = llm.generate(
    "Explain vector databases in very simple words."
)

print("\n")
print("=" * 60)
print("OPENROUTER RESPONSE")
print("=" * 60)
print(answer)