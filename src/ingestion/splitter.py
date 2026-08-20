from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(
    documents,
    progress_callback=None
):

    if progress_callback:
        progress_callback(
            32,
            "Splitting document into chunks..."
        )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = text_splitter.split_documents(
        documents
    )

    if progress_callback:
        progress_callback(
            40,
            f"Created {len(chunks)} chunks"
        )

    return chunks