# mcp_server/tools/summarize_block.py
import os
from google.genai import Client
from dotenv import load_dotenv

load_dotenv()

def summarize_block(paragraph: str):
    api_key = os.getenv("GOOGLE_API_KEY")
    client = Client(api_key=api_key)

    prompt = f"""
    Compress the following paragraph into 2-3 concise summary lines.

    PARAGRAPH:
    {paragraph}
    """

    res = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return {"summary": res.text}
