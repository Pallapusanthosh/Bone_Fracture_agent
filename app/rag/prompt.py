def build_prompt(context: dict, docs: list, query: str, mode="analysis") -> str:
    context_block = "\n".join(f"{k}: {v}" for k, v in context.items())
    knowledge_block = "\n\n".join(doc.page_content for doc in docs)

    if mode == "chat":
        print("chat_prompt")
        return f"""
You are a medical assistant specialized in bone fractures.

Answer the user's question clearly and simply.

IMPORTANT:
- Be helpful and concise
- Use medical knowledge
- If unsure, say "Consult a doctor"

USER CONTEXT:
{context_block}

RETRIEVED KNOWLEDGE:
{knowledge_block}

USER QUESTION:
{query}

Answer:
"""

    if mode == "analysis":
        print("analysis_prompt")
        return f"""
    You are a medical assistant specialized in bone fractures.

    IMPORTANT:
        - Answer ONLY from provided knowledge
        - Keep structured format

    USER CONTEXT:
    {context_block}

    RETRIEVED KNOWLEDGE:
    {knowledge_block}

    USER QUESTION:
    {query}

    Respond STRICTLY in structured format:
    ...
    """ 

    if mode == "report":
        print("report_prompt")
        return f"""
        You are a medical assistant specialized in bone fractures and now you are trying to help the expert or doctor by generatinga report based on context given 
        make it easily understandble and precise.

        and make sure in the result you have to give the 
        1. Summary
        2. Severity
        3. Symptoms
        4. Emergency Signs
        5. First Aid
        6. Treatment
        7. Recovery
        8. Risk Factors & Complications
        9. When to Seek Immediate Care
        10. AI Confidence & Notes
        11. Disclaimer

        IMPORTANT:
            - Answer ONLY from provided knowledge
            - Keep structured format

        USER CONTEXT:
        {context_block}

        RETRIEVED KNOWLEDGE:
        {knowledge_block}

        USER QUESTION:
        {query}

        Respond STRICTLY in structured format:
        ...
        """     
   