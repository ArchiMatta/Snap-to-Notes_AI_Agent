import os
from .approval_handler import ApprovalHandler

class WorkflowManager:
    """Handles long workflow approvals + OCR + large text summarization."""

    def __init__(self, ocr_tool, summarizer_agent):
        self.approvals = ApprovalHandler()
        self.ocr_tool = ocr_tool
        self.agent = summarizer_agent
        self._pending_input = None

    def start_long_summary_workflow(self, input_value: str) -> dict:
        self._pending_input = input_value

        return self.approvals.request_approval(
            operation_name="long_summary",
            details=f"Processing: {input_value}"
        )

    def execute_long_summary(self, user_input=None) -> dict:
        """
        After approval → run OCR if file, or use raw text.
        Bypasses length limit (force=True).
        """

        target = user_input if user_input else self._pending_input
        if not target:
            return {"status": "no_pending_operation"}

        # CASE 1 — pasted text
        if not os.path.exists(target):
            extracted = target

        # CASE 2 — file → OCR
        else:
            extracted = self.ocr_tool.run(target)

        # ⛔ IMPORTANT → must force=True
        final = self.agent.summarize_text(extracted, force=True)

        self._pending_input = None

        return {
            "status": "completed",
            "summary": final.get("summary", "")
        }
