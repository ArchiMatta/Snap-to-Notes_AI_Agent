# mcp_server/tools/extract_key_points.py
import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

def extract_key_points(text: str):
    api_key = os.getenv("GOOGLE_API_KEY")
    client = Client(api_key=api_key)

    prompt = f"""
    Extract the MOST IMPORTANT key points from this text.
    Return 5–7 bullet points max.

    TEXT:
    {text}
    """

    result = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return {"key_points": result.text}
