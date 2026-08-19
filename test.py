from src.retrieval.retriever import Retriever


retriever = Retriever()


query = "What is machine learning?"


results = retriever.retrieve_with_scores(
    query,
    k=5
)


print("=" * 60)
print("SIMILARITY SEARCH TEST")
print("=" * 60)


for i, (document, score) in enumerate(results):

    print("\n" + "-" * 60)

    print(f"RESULT {i + 1}")

    print("Score:", score)

    print("Page:", document.metadata.get("page"))

    print("Text:")
    print(document.page_content[:500])