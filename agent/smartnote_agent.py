import os
from dotenv import load_dotenv
from google.genai import Client

from agent.memory_manager import MemoryManager
from agent.context_manager import ContextManager
from agent.summarizer import Summarizer

load_dotenv()

class SmartNoteAgent:
    """Multi-turn SmartNote agent with memory + context"""

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Missing GOOGLE_API_KEY in .env")

        self.client = Client(api_key=api_key)
        self.model = "models/gemini-2.5-flash"

        # NEW DAY-2 MODULES
        self.memory = MemoryManager(max_memory=5)
        self.context = ContextManager(self.memory)
        self.summarizer = Summarizer()

    def handle_user(self, user_text: str) -> str:
        """Main orchestrator for multi-turn flow."""

        # Build contextual prompt
        prompt = self.context.build_prompt(user_text)

        # LLM call
        result = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        answer = result.text

        # Add to memory
        self.memory.add_turn(user_text, answer)

        return answer
