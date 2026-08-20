import hashlib
import json
from pathlib import Path


REGISTRY_PATH = Path(
    "vectorstore/document_registry.json"
)


def calculate_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(1024 * 1024)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def load_registry():

    if not REGISTRY_PATH.exists():
        return {}

    try:

        with open(
            REGISTRY_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (json.JSONDecodeError, OSError):

        return {}


def save_registry(registry):

    REGISTRY_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        REGISTRY_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            registry,
            file,
            indent=4
        )


def is_document_processed(file_path):

    file_hash = calculate_file_hash(
        file_path
    )

    registry = load_registry()

    if file_hash in registry:

        return True, file_hash

    return False, file_hash


def register_document(
    file_path,
    file_hash,
    chunk_count
):

    registry = load_registry()

    registry[file_hash] = {

        "filename": Path(
            file_path
        ).name,

        "path": str(
            file_path
        ),

        "chunk_count": chunk_count
    }

    save_registry(registry)