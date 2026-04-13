def build_prompt(context: dict, docs: list, query: str , confidence_hint: str) -> str:
    context_block = "\n".join(f"{k}: {v}" for k, v in context.items())
    knowledge_block = "\n\n".join(doc.page_content for doc in docs)

    return f"""
You are a medical assistant specialized in bone fractures.

IMPORTANT:
- Answer ONLY from the provided knowledge
- Keep it simple and medically accurate
- Separate normal symptoms and emergency signs


Detection Insight:
{confidence_hint}

Use this as supporting information only.
Do NOT decide severity based only on this.
Combine with medical knowledge.

Use this ONLY as supporting signal, NOT as final severity.
Severity must be based on medical reasoning.

USER CONTEXT:
{context_block}

RETRIEVED KNOWLEDGE:
{knowledge_block}

USER QUESTION:
{query}

Respond STRICTLY in this format:

Summary:
...

Symptoms:
- Pain
- Swelling
- Bruising
- Limited movement

Emergency Signs:
- Severe deformity
- Bone visible
- Loss of pulse

Treatment:
- ...

Precautions:
- ...

Recovery:
...
"""