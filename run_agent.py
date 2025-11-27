from agent.smartnote_agent import SmartNoteAgent

if __name__ == "__main__":
    agent = SmartNoteAgent()

    user_input = input("Enter text to summarize:\n\n")

    summary = agent.summarize_text(user_input)

    print("\n=== SUMMARY ===\n")
    print(summary)
