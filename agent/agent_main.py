from agent.smartnote_agent import SmartNoteAgent

def main():
    agent = SmartNoteAgent()

    print("\nSmartNote Multi-Turn Agent Ready!\n")
    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit"]:
            break

        response = agent.handle_user(user)
        print("\nSmartNote:", response, "\n")

if __name__ == "__main__":
    main()
