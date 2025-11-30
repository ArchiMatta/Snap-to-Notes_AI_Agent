import os
from dotenv import load_dotenv
from google.genai import Client
from agent.memory_manager import MemoryManager

load_dotenv()

class SmartNoteAgent:
    """Summarization agent with memory + approval triggers."""

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Missing GOOGLE_API_KEY in .env")

        self.client = Client(api_key=api_key)
        self.model = "models/gemini-2.0-flash"
        self.long_text_threshold = 3000

        # 🔥 ADD THIS
        self.memory_manager = MemoryManager()

    def summarize_text(self, user_text: str, force: bool = False) -> dict:

        # Save every message to memory (multi-turn)
        self.memory_manager.add_to_memory("USER: " + user_text)

        if not force and len(user_text) > self.long_text_threshold:
            return {
                "status": "requires_approval",
                "details": "Text too long; requires long summary workflow",
                "length": len(user_text)
            }

        # Use conversation history to answer follow-up questions
        full_context = (
            "Conversation history:\n"
            f"{self.memory_manager.get_memory()}\n\n"
            "Now answer based only on the ABOVE history.\n"
            "Provide the improved/updated summary if asked.\n"
            "Response:\n"
        )

        prompt = full_context + user_text

        result = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        final_text = result.text or ""

        # Store AI response too
        self.memory_manager.add_to_memory("ASSISTANT: " + final_text)

        return {
            "status": "completed",
            "summary": final_text
        }
