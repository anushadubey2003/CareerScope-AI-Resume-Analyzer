from fastapi import FastAPI, File, UploadFile
from app.parser import parse_resume
from app.scorer import generate_feedback
import uvicorn

app = FastAPI(title="CareerScope – AI Resume Analyzer")

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...)):
    contents = await file.read()
    resume_data = parse_resume(contents)
    score, feedback = generate_feedback(resume_data)
    return {
        "score": score,
        "feedback": feedback,
        "parsed": resume_data
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
