from app.rag.vector_store import build_vector_store
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from app.rag.prompt import build_prompt
import os

load_dotenv()

db = build_vector_store()

# ✅ Gemini LLM
def get_llm():
    return ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",   # stable + lighter
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )


def run_rag(query: str, context: dict, mode="analysis"):
    docs = db.similarity_search(query, k=3)

    prompt = build_prompt(
        context=context,
        docs=docs,
        query=query,
        mode=mode
    )

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content