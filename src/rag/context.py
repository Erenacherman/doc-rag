def format_context(documents):

    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown"
        )

        page = document.metadata.get(
            "page",
            "Unknown"
        )

        text = document.page_content

        context_parts.append(
            f"""
Source: {source}
Page: {page}

{text}
"""
        )

    return "\n\n".join(context_parts)