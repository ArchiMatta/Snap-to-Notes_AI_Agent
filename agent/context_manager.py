class ContextManager:
    """
    Combines memory + new user input to generate
    a context-rich prompt for the model.
    """

    def __init__(self, memory_manager):
        self.memory = memory_manager

    def build_prompt(self, user_input: str) -> str:
        past_context = self.memory.get_context()

        prompt = f"""
You are SmartNote, a multi-turn intelligent summarizer.

The user may ask follow-ups. Use past memory when helpful.

### MEMORY ###
{past_context}

### USER INPUT ###
{user_input}

### INSTRUCTIONS ###
- Use memory if the user refers to "previous summary", "continue", "improve", "add more", etc.
- Provide clear, structured output.
"""

        return prompt
