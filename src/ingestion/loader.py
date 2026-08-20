from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(file_path, progress_callback=None):

    if progress_callback:
        progress_callback(
            5,
            "Opening PDF..."
        )

    loader = PyMuPDFLoader(file_path)

    documents = loader.load()

    total_pages = len(documents)

    if progress_callback:
        progress_callback(
            10,
            f"PDF opened - {total_pages} pages found"
        )

    # Show extraction progress
    for i in range(total_pages):

        progress = 10 + int(
            ((i + 1) / total_pages) * 20
        )

        if progress_callback:
            progress_callback(
                progress,
                f"Extracting page {i + 1}/{total_pages}"
            )

    if progress_callback:
        progress_callback(
            30,
            f"Extracted {total_pages} pages"
        )

    return documents