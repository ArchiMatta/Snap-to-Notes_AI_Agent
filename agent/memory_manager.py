class MemoryManager:
    """
    Simple memory engine for multi-turn conversation.
    Stores last N user messages + agent responses.
    """

    def __init__(self, max_memory=5):
        self.max_memory = max_memory
        self.history = []

    def add_turn(self, user_msg: str, agent_msg: str):
        self.history.append({"user": user_msg, "agent": agent_msg})

        # keep only last N turns
        if len(self.history) > self.max_memory:
            self.history.pop(0)

    def get_context(self) -> str:
        """Return memory as a formatted context block."""
        if not self.history:
            return ""

        formatted = []
        for turn in self.history:
            formatted.append(f"User: {turn['user']}\nAssistant: {turn['agent']}")

        return "\n\n".join(formatted)
