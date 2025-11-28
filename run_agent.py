from agent.agent_main import SmartNoteAgent

if __name__ == "__main__":
    agent = SmartNoteAgent()

    text = input("Enter text:\n\n")
    response = agent.run(text)

    print("\n=== FINAL OUTPUT ===\n")
    print(response)
