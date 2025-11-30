import os
from agent.smartnote_agent import SmartNoteAgent
from mcp_server.runtime.operations.workflow_manager import WorkflowManager
from mcp_server.tools.ocr_tool import OCRTool
from dotenv import load_dotenv

load_dotenv()

def main():
    print("SmartNote Multi-Turn Agent Ready!\n")

    agent = SmartNoteAgent()
    tesseract_cmd = os.getenv("TESSERACT_CMD")
    ocr_tool = OCRTool(tesseract_cmd)

    workflow_manager = WorkflowManager(ocr_tool, agent)

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        is_file = os.path.exists(user_input)

        # For files: OCR first
        if is_file:
            extracted = ocr_tool.run(user_input)
            response = agent.summarize_text(extracted)
        else:
            response = agent.summarize_text(user_input)

        # Long workflow trigger
        if response.get("status") == "requires_approval":
            print("SmartNote:", response["details"])

            req = workflow_manager.start_long_summary_workflow(user_input)
            print("SmartNote:", req["message"])

            approval = input("Type 'approve' to continue, 'reject' to cancel: ").strip().lower()

            if approval == "approve":
                workflow_manager.approvals.approve()
                final = workflow_manager.execute_long_summary(user_input)

                print("\nSmartNote: Long workflow finished.\n")
                print(final.get("summary", "[No summary found]"))

            else:
                workflow_manager.approvals.reject()
                print("SmartNote: Operation cancelled.")
            continue

        # Short summary
        print("\nSmartNote:", response.get("summary", "[No summary found]"))

if __name__ == "__main__":
    main()
