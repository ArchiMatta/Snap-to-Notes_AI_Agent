from mcp_server.runtime.operations.workflow_manager import WorkflowManager
from mcp_server.tools.extract_text import ExtractTextTool
from mcp_server.tools.create_docx import DocxTool

extract_tool = ExtractTextTool()
summarize_tool = DocxTool()  # placeholder summarizer or your real LUT

workflow = WorkflowManager(extract_tool, summarize_tool)
