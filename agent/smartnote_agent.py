import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

class SmartNoteAgent:
    """A lightweight ADK-style agent for summarization."""

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Missing GOOGLE_API_KEY in .env")

        self.client = Client(api_key=api_key)
        self.model = "models/gemini-2.5-flash"

    def summarize_text(self, user_text: str) -> str:
        """Summarize text using Gemini."""

        prompt = f"""
        You are SmartNote. Summarize the following text
        into clean bullet points with key takeaways.

        TEXT:
        {user_text}
        """

        result = self.client.models.generate_content(
    model=self.model,
    contents=prompt
)

        return result.text
