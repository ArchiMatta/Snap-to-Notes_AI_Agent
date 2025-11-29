from .approval_handler import ApprovalHandler

class WorkflowManager:
    """
    Orchestrates long-running tool operations with approval flow.
    """

    def __init__(self, extract_tool, summarize_tool):
        self.approvals = ApprovalHandler()
        self.extract_tool = extract_tool
        self.summarize_tool = summarize_tool

    def start_long_summary_workflow(self, file_path):
        """
        Start: ask user for approval because summarizing a large file takes time.
        """

        approval_request = self.approvals.request_approval(
            operation_name="long_summary",
            details=f"Summarize large file: {file_path}"
        )

        return approval_request

    def execute_long_summary(self, file_path):
        """
        After approval → run extraction → summarization.
        """

        extracted_text = self.extract_tool.run(file_path)
        summary = self.summarize_tool.run(extracted_text)

        return {
            "status": "completed",
            "summary": summary
        }
