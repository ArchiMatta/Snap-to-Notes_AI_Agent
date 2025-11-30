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

        self.model = "models/gemini-2.0-flash"
        self.long_text_threshold = 3000

    def summarize_text(self, user_text: str, force: bool = False) -> dict:
        """
        force=True bypasses length limit for long workflows.
        """

        # ⛔ normal mode → length check
        if not force and len(user_text) > self.long_text_threshold:
            return {
                "status": "requires_approval",
                "details": "Text too long; requires long summary workflow",
                "length": len(user_text)
            }

        prompt = (
            "Summarize the following text into clear bullet points with key insights:\n\n"
            f"{user_text}"
        )

        result = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return {
            "status": "completed",
            "summary": result.text or ""
        }
