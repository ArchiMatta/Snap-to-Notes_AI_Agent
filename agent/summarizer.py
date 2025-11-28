# agent/summarizer.py
import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

class Summarizer:
    """Main summarizer that orchestrates tool calls."""

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Missing GOOGLE_API_KEY in .env")

        self.client = Client(api_key=api_key)
        self.model = "models/gemini-flash-latest"

    def summarize(self, text: str) -> str:
        """Base model summarization."""
        prompt = f"""
        Summarize this text in clean structured bullet points.

        TEXT:
        {text}
        """

        res = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return res.text
