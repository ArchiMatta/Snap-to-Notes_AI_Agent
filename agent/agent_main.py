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

    last_extracted_text = None  # store OCR text for long workflow

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        is_file = os.path.exists(user_input)

        # -----------------------------------------------------------
        # CASE 1 — FILE INPUT → OCR
        # -----------------------------------------------------------
        if is_file:
            extracted_text = ocr_tool.run(user_input)
            last_extracted_text = extracted_text  # save for workflow + memory
            agent.memory_manager.add_to_memory(extracted_text)

            print("\n[Extracted Text via OCR]\n", extracted_text[:450], "...\n")

            response = agent.summarize_text(extracted_text)

        # -----------------------------------------------------------
        # CASE 2 — NORMAL TEXT INPUT
        # -----------------------------------------------------------
        else:
            agent.memory_manager.add_to_memory(user_input)
            response = agent.summarize_text(user_input)

        # -----------------------------------------------------------
        # LONG WORKFLOW TRIGGER
        # -----------------------------------------------------------
        if response.get("status") == "requires_approval":
            print("SmartNote:", response["details"])

            req = workflow_manager.start_long_summary_workflow("long_summary")
            print("SmartNote:", req["message"])

            approval = input("Type 'approve' to continue, 'reject' to cancel: ").strip().lower()

            if approval == "approve":
                workflow_manager.approvals.approve()

                # FIX: pass EXTRACTED TEXT (not file path)
                long_text = last_extracted_text if is_file else user_input

                final = workflow_manager.execute_long_summary(long_text)

                print("\nSmartNote: Long workflow finished.\n")
                print(final.get("summary", "[No summary found]"))

            else:
                workflow_manager.approvals.reject()
                print("SmartNote: Operation cancelled.")

            continue

        # -----------------------------------------------------------
        # SHORT SUMMARY
        # -----------------------------------------------------------
        print("\nSmartNote:", response.get("summary", "[No summary found]"))


if __name__ == "__main__":
    main()
