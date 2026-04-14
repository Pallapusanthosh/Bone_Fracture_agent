from app.main import run_report
from app.main import run_agent
from app.main import run_chat
from app.main import run_report
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from fastapi.responses import FileResponse
from app.Report import generate_pdf


app = FastAPI()

class AnalyzeRequest(BaseModel):
    body_part : str
    condition : str
    confidence : float = 0.0
    
class ChatRequest(BaseModel):
    question: str
    body_part: str = "unknown"
    condition: str = "unknown"


@app.post("/chat")
def chat(data: ChatRequest):
    result = run_chat(
        query=data.question,
        body_part=data.body_part,
        condition=data.condition
    )
    return result

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = run_agent(
        body_part=request.body_part,
        condition=request.condition,
        confidence=request.confidence)
    return result
@app.post("/report")
def generate_report(data: AnalyzeRequest):
    result = run_report(
        body_part=data.body_part,
        condition=data.condition,
        confidence=data.confidence
    )

    file_path = generate_pdf(result)

    return FileResponse(
        file_path,
        media_type='application/pdf',
        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )