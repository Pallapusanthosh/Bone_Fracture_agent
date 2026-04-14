import re
from  app.rag.rag_chain import run_rag

def build_query(body_part, condition):
    return f"What are symptoms, treatment, precautions and recovery for {body_part} {condition}?"

def run_report(body_part, condition , confidence=0.7):
    if condition == "no fracture":
        return {
            "status": "No fracture detected",
            "advice": "If pain persists, consult a doctor"
        }

    # 1. Build Query
    query = build_query(body_part, condition)

    # 2. Build Context
    context = {
        "body_part": body_part,
        "condition": condition,
        "confidence": confidence,
        "confidence_hint": get_confidence_hint(confidence)
    }

    # 3. Run RAG
    result = run_rag(query, context, mode="report")

    # 4. Format Output
    return format_output(result)

def run_agent(body_part, condition , confidence=0.7):
    print("Running agent with:", body_part, condition)
    if condition == "no fracture":
        return {
            "status": "No fracture detected",
            "advice": "If pain persists, consult a doctor"
        }
    query = build_query(body_part, condition)
    confidence_hint = get_confidence_hint(confidence)
    
    context = {
        "body_part": body_part,
        "condition": condition,
        "confidence": confidence,
        "confidence_hint": confidence_hint
    }

    result = run_rag(query, context, mode="analysis")

    return format_output(result)

def extract_section(text, section):
    pattern = rf"{section}:\s*(.*?)(\n[A-Z][a-z]+:|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def extract_severity(text):
    content = extract_section(text, "Severity")
    return content



def extract_list(text, section):
    content = extract_section(text, section)
    return [line.strip("- ").strip() for line in content.split("\n") if line.strip()]
def format_output(text):
    return {
        "summary": extract_section(text, "Summary"),
        "severity": extract_severity(text),
        "symptoms": extract_list(text, "Symptoms"),
        "emergency": extract_list(text, "Emergency Signs"),
        "treatment": extract_list(text, "Treatment"),
        "precautions": extract_list(text, "Precautions"),
        "recovery": extract_section(text, "Recovery"),
    }
def get_confidence_hint(conf):
    if conf >= 0.8:
        return "fracture clearly visible in scan"
    elif conf >= 0.5:
        return "possible fracture but not very clear"
    else:
        return "fracture detection is uncertain"
def run_chat(query, body_part=None, condition=None):
    context = {
        "body_part": body_part or "unknown",
        "condition": condition or "unknown"
    }

    response = run_rag(query, context, mode="chat")

    return {
        "question": query,
        "answer": response
    }