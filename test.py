from src.ingestion.pipeline import ingest_pdf


PDF_PATH = "data/uploads/machine_learning.pdf"


chunks = ingest_pdf(PDF_PATH)


lengths = [
    len(chunk.page_content)
    for chunk in chunks
]


print("=" * 60)
print("CHUNK QUALITY TEST")
print("=" * 60)

print("Total chunks:", len(chunks))
print("Smallest chunk:", min(lengths))
print("Largest chunk:", max(lengths))
print("Average chunk:", sum(lengths) / len(lengths))


empty_chunks = [
    chunk
    for chunk in chunks
    if not chunk.page_content.strip()
]


print("Empty chunks:", len(empty_chunks))


if len(chunks) == 0:
    print("❌ FAILED: No chunks.")
    raise SystemExit(1)


if len(empty_chunks) > 0:
    print("⚠️ WARNING: Empty chunks detected.")
else:
    print("✅ No empty chunks.")


print("\nPHASE 2 CHUNK QUALITY CHECK PASSED ✅")