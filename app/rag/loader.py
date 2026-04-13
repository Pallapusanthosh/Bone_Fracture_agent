from langchain_community.document_loaders import TextLoader, PyPDFLoader
from pathlib import Path




def load_documents():
    docs = []

    
    base_path = Path(__file__).resolve().parent / "KnowledgeBase"

    # print("📁 Using path:", base_path)

    for file in base_path.rglob("*"):
        # print("📂 Checking:", file)

        if file.suffix in [".txt", ".md"]:
            # print("✅ Loading text:", file)
            loader = TextLoader(str(file), encoding="utf-8")
            docs.extend(loader.load())

        elif file.suffix == ".pdf":
            # print("✅ Loading PDF:", file)
            loader = PyPDFLoader(str(file))
            docs.extend(loader.load())

    print("📄 Total docs loaded:", len(docs))
    return docs