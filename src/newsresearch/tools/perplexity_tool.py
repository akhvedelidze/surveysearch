import os
import requests
from crewai_tools import tool

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

@tool
def sonar_reasoning_tool(query: str) -> str:
    """
    Query the Sonar Reasoning Model from Perplexity AI.
    """
    url = "https://api.perplexity.ai/chat/completions"  # Replace with actual endpoint if different
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "model": "sonar_reasoning"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code} - {response.text}"
