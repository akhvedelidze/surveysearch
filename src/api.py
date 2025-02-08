import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from newsresearch.crew import Newsresearch

app = FastAPI()

class ReportRequest(BaseModel):
    topic: str
    country: str

@app.post("/generate_report/")
def generate_report(request: ReportRequest):
    # Prepare inputs for the Newsresearch crew
    inputs = {
        "topic": request.topic,
        "country": request.country
    }

    # Kick off the CrewAI process
    Newsresearch().crew().kickoff(inputs=inputs)

    # Define the report file path
    report_filename = f"{request.country}_report.md"
    report_path = os.path.join(os.getcwd(), report_filename)

    # Check if the file was generated
    if not os.path.exists(report_path):
        raise HTTPException(status_code=500, detail=f"Report {report_filename} not found after generation.")

    # Return the file as a downloadable response
    return FileResponse(report_path, media_type="text/markdown", filename=report_filename)
