class ApprovalHandler:
    """
    Handles human approval before long-running operations continue.
    """

    def __init__(self):
        self.pending_approval = None  # store operation + metadata

    def request_approval(self, operation_name, details):
        """
        Store an operation and return approval request message.
        """
        self.pending_approval = {
            "operation": operation_name,
            "details": details
        }

        return {
            "status": "awaiting_approval",
            "message": f"Operation '{operation_name}' requires approval.",
            "details": details
        }

    def approve(self):
        """
        Approve pending operation.
        """
        if not self.pending_approval:
            return {"status": "no_pending_operation"}

        operation = self.pending_approval
        self.pending_approval = None

        return {
            "status": "approved",
            "operation": operation["operation"],
            "details": operation["details"]
        }

    def reject(self):
        """
        Reject pending operation.
        """
        self.pending_approval = None
        return {"status": "rejected"}