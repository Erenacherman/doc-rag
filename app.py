import os

from dotenv import load_dotenv

# ------------------------------------------------------------
# Load environment variables
# ------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------
# PDF
# ------------------------------------------------------------

from src.ingestion.loader import load_pdf
from src.ingestion.splitter import split_documents


# ------------------------------------------------------------
# Embeddings
# ------------------------------------------------------------

from src.embeddings.embedder import EmbeddingManager


# ------------------------------------------------------------
# Vector database
# ------------------------------------------------------------

from src.vectorstore.chroma_store import VectorStoreManager


# ------------------------------------------------------------
# Retriever
# ------------------------------------------------------------

from src.retrieval.retriever import Retriever


# ------------------------------------------------------------
# RAG
# ------------------------------------------------------------

from src.rag.context import format_context
from src.rag.prompt import RAG_PROMPT


# ------------------------------------------------------------
# LLM
# ------------------------------------------------------------

from src.llm.llm_factory import create_llm


# ============================================================
# CONFIGURATION
# ============================================================

PDF_PATH = "data/uploads/test.pdf"

CHROMA_PATH = "vectorstore/chroma"


# ============================================================
# PROGRESS
# ============================================================

def progress(percent, message):

    print(
        f"[{percent:3d}%] {message}"
    )


# ============================================================
# STEP 1 + STEP 2
# LOAD AND SPLIT PDF
# ============================================================

def load_and_split_pdf():

    print()
    print("=" * 60)
    print("STEP 1 - LOADING PDF")
    print("=" * 60)

    # --------------------------------------------------------
    # Check PDF
    # --------------------------------------------------------

    if not os.path.exists(PDF_PATH):

        print()
        print("❌ PDF not found:")
        print(PDF_PATH)

        print()
        print(
            "Put your PDF at:"
        )

        print(PDF_PATH)

        return None

    # --------------------------------------------------------
    # Load
    # --------------------------------------------------------

    progress(
        10,
        "Loading PDF..."
    )

    documents = load_pdf(
        PDF_PATH
    )

    print()

    print(
        f"✅ Documents loaded: "
        f"{len(documents)}"
    )

    # --------------------------------------------------------
    # Split
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("STEP 2 - SPLITTING DOCUMENT")
    print("=" * 60)

    progress(
        30,
        "Splitting document into chunks..."
    )

    chunks = split_documents(
        documents
    )

    print()

    print(
        f"✅ Total chunks: "
        f"{len(chunks)}"
    )

    # --------------------------------------------------------
    # Show first chunk
    # --------------------------------------------------------

    if chunks:

        print()
        print("-" * 60)
        print("FIRST CHUNK")
        print("-" * 60)

        print(
            chunks[0].page_content[:500]
        )

        print()
        print("-" * 60)
        print("METADATA")
        print("-" * 60)

        print(
            chunks[0].metadata
        )

    return chunks


# ============================================================
# STEP 3 + STEP 4
# EMBEDDINGS + CHROMA
# ============================================================

def create_vector_store(chunks):

    # --------------------------------------------------------
    # Embeddings
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("STEP 3 - CREATING EMBEDDINGS")
    print("=" * 60)

    progress(
        50,
        "Loading embedding model..."
    )

    embedding_manager = (
        EmbeddingManager()
    )

    embeddings = (
        embedding_manager
        .get_embeddings()
    )

    print()

    print(
        "✅ Embedding model loaded"
    )

    # --------------------------------------------------------
    # Chroma
    # --------------------------------------------------------

    print()
    print("=" * 60)
    print("STEP 4 - CREATING VECTOR DATABASE")
    print("=" * 60)

    progress(
        70,
        "Creating Chroma vector store..."
    )

    vector_store = (
        VectorStoreManager(
            embedding_function=embeddings,
            persist_directory=CHROMA_PATH
        )
    )

    print()

    print(
        "Adding documents to Chroma..."
    )

    vector_store.add_documents(
        chunks
    )

    print()

    print(
        "✅ Documents added to Chroma"
    )

    return vector_store


# ============================================================
# QUESTION ANSWERING
# ============================================================

def ask_questions(
    vector_store,
    llm
):

    print()
    print("=" * 60)
    print("STEP 5 - RAG QUESTION ANSWERING")
    print("=" * 60)

    # --------------------------------------------------------
    # Create retriever
    # --------------------------------------------------------

    retriever = Retriever(
        vector_store
    )

    while True:

        print()

        question = input(
            "Ask a question "
            "(type 'exit' to stop): "
        )

        question = question.strip()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        if question.lower() == "exit":

            print()

            print(
                "👋 Goodbye!"
            )

            break

        # ----------------------------------------------------
        # Empty question
        # ----------------------------------------------------

        if not question:

            print(
                "❌ Please enter a question."
            )

            continue

        # ====================================================
        # RETRIEVAL
        # ====================================================

        print()
        print(
            "🔎 Searching Chroma..."
        )

        progress(
            80,
            "Finding relevant documents..."
        )

        documents = retriever.retrieve(
            question,
            k=4
        )

        # ----------------------------------------------------
        # No documents
        # ----------------------------------------------------

        if not documents:

            print()

            print(
                "❌ No relevant documents found."
            )

            continue

        print()

        print(
            f"✅ Retrieved "
            f"{len(documents)} chunks"
        )

        # ====================================================
        # BUILD CONTEXT
        # ====================================================

        progress(
            85,
            "Preparing context..."
        )

        context = format_context(
            documents
        )

        # ====================================================
        # BUILD PROMPT
        # ====================================================

        progress(
            90,
            "Building RAG prompt..."
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        # ====================================================
        # GENERATE ANSWER
        # ====================================================

        progress(
            95,
            "Generating answer..."
        )

        answer = llm.generate(
            prompt
        )

        # ====================================================
        # SHOW ANSWER
        # ====================================================

        print()
        print("=" * 60)
        print("🤖 ANSWER")
        print("=" * 60)

        print()

        print(
            answer
        )

        # ====================================================
        # SHOW SOURCES
        # ====================================================

        print()
        print("=" * 60)
        print("📚 SOURCES")
        print("=" * 60)

        for i, document in enumerate(
            documents,
            start=1
        ):

            metadata = (
                document.metadata
            )

            page = metadata.get(
                "page",
                "Unknown"
            )

            source = metadata.get(
                "source",
                "Unknown"
            )

            print(
                f"{i}. "
                f"Page: {page} | "
                f"Source: {source}"
            )


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)

    print(
        "             📚 DOCCHAT"
    )

    print("=" * 60)

    print()
    print(
        "Starting application..."
    )

    # ========================================================
    # SHOW LLM CONFIGURATION
    # ========================================================

    provider = os.getenv(
        "LLM_PROVIDER",
        "openrouter"
    ).lower()

    print()

    print(
        f"Configured LLM: {provider}"
    )

    # ========================================================
    # CREATE LLM
    # ========================================================

    llm = create_llm()

    # ========================================================
    # LOAD PDF
    # ========================================================

    chunks = load_and_split_pdf()

    if not chunks:

        print()

        print(
            "❌ Application stopped."
        )

        return

    # ========================================================
    # CREATE VECTOR STORE
    # ========================================================

    vector_store = (
        create_vector_store(
            chunks
        )
    )

    # ========================================================
    # ASK QUESTIONS
    # ========================================================

    ask_questions(
        vector_store,
        llm
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()