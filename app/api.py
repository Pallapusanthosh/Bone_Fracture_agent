from app.main import run_agent
from fastapi import FastAPI
from pydantic import BaseModel


from fastapi.responses import FileResponse
from app.Report import generate_pdf


app = FastAPI()

class AnalyzeRequest(BaseModel):
    body_part : str
    condition : str
    confidence : float = 0.0
    
    
@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = run_agent(
        body_part=request.body_part,
        condition=request.condition,
        confidence=request.confidence)
    return result
@app.post("/report")
def generate_report(data: AnalyzeRequest):
    result = run_agent(
        body_part=data.body_part,
        condition=data.condition,
        confidence=data.confidence
    )

    file_path = generate_pdf(result)

    return FileResponse(
        file_path,
        media_type='application/pdf',
        filename="fracture_report.pdf"
    )