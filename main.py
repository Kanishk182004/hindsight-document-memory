import os

from dotenv import load_dotenv
from hindsight_client import Hindsight
from pypdf import PdfReader

load_dotenv()

HINDSIGHT_BASE_URL = os.getenv("HINDSIGHT_BASE_URL")
BANK_ID = os.getenv("BANK_ID")

client = Hindsight(base_url=HINDSIGHT_BASE_URL)


def load_documents(folder_path: str = "data"):
    """Load TXT and PDF documents from a folder."""

    documents = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        # TXT Files
        if filename.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()

            if content:
                documents.append(
                    f"FILE: {filename}\n"
                    f"PAGE: 1\n\n"
                    f"{content}"
                )

        # PDF Files
        elif filename.lower().endswith(".pdf"):
            reader = PdfReader(file_path)

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text()

                if text and text.strip():
                    documents.append(
                        f"FILE: {filename}\n"
                        f"PAGE: {page_number}\n\n"
                        f"{text.strip()}"
                    )

    return documents


def ingest_documents():
    """Ingest all documents into the Hindsight memory bank."""

    print("\nIngesting documents...\n")

    documents = load_documents()

    if not documents:
        print("No documents found.")
        return

    for index, content in enumerate(documents, start=1):
        print(f"Ingesting {index}/{len(documents)}")

        client.retain(
            bank_id=BANK_ID,
            content=content
        )

    print("\nIngestion complete.\n")


def query_loop():
    """Interactive query interface."""

    print("Memory bank ready.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Question: ").strip()

        if query.lower() == "exit":
            break

        response = client.reflect(
            bank_id=BANK_ID,
            query=query
        )

        print("\nAnswer:\n")
        print(response.text)
        print()


def main():
    INGEST = True

    if INGEST:
        ingest_documents()

    query_loop()
    client.close()


if __name__ == "__main__":
    main()