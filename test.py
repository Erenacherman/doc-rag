from src.rag.pipeline import RAGPipeline


rag = RAGPipeline()


questions = [
    "What is machine learning?",
    "What is supervised learning?",
    "What is a neural network?",
]


for question in questions:

    print("\n" + "=" * 70)

    print("QUESTION:")
    print(question)

    result = rag.answer(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")

    for document in result["documents"]:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        page = document.metadata.get(
            "page",
            "Unknown"
        )

        print(
            f"- {source} | Page {page}"
        )