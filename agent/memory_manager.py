class MemoryManager:
    def __init__(self):
        self.memory = ""

    def add_to_memory(self, text: str):
        self.memory += "\n" + text

    def get_memory(self):
        return self.memory.strip()

    def clear(self):
        self.memory = ""
