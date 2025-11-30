# mcp_server/runtime/operations/workflow_manager.py

from mcp_server.runtime.operations.approval_handler import ApprovalHandler

class WorkflowManager:
    """
    Manages long-running operations like long summaries.
    Handles approval → execution sequence.
    """

    def __init__(self, ocr_tool, agent):
        self.ocr_tool = ocr_tool
        self.agent = agent

        # FIX HERE (ApprovalManager → ApprovalHandler)
        self.approvals = ApprovalHandler()

    def start_long_summary_workflow(self, file_or_text):
        """
        Step 1 — Ask for approval
        """
        return self.approvals.request_approval(
            "long_summary",
            {"target": file_or_text}
        )

    def execute_long_summary(self, file_or_text):
        """
        Step 2 — Perform long summary after user approves
        """

        # If this is a file → OCR first
        if isinstance(file_or_text, str) and file_or_text.endswith((".png", ".jpg", ".jpeg")):
            try:
                extracted_text = self.ocr_tool.run(file_or_text)
            except Exception as e:
                return {"status": "error", "message": str(e)}
        else:
            extracted_text = file_or_text

        # Force = True → bypass length check
        final = self.agent.summarize_text(extracted_text, force=True)
        return final
