import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from src.newsresearch.crew import Newsresearch

# If the module path still causes issues, uncomment the following line:
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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

    return {
        "message": f"Report generation for topic '{request.topic}' in '{request.country}' started successfully."
    }

