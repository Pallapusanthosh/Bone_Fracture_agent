from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# from app.rag.loader import load_documents
from app.rag.loader import load_documents

def build_vector_store():
    documents = load_documents()
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(documents, embeddings)
    return db
