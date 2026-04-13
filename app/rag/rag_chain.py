from app.rag.vector_store import build_vector_store
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from app.rag.prompt import build_prompt
import os

load_dotenv()

db = build_vector_store()


def get_llm():
    return HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.3,
        max_new_tokens=512
    )


def run_rag(query: str, context: dict):
    docs = db.similarity_search(query, k=3)

    prompt = build_prompt(
        context=context,
        docs=docs,
        query=query
    )

    llm = get_llm()   # ✅ fresh instance every time

    response = llm.invoke(prompt)

    return response