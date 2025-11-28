# agent/agent_main.py

from agent.summarizer import Summarizer
from mcp_server.tools.extract_key_points import extract_key_points
from mcp_server.tools.google_search import google_search
from mcp_server.tools.summarize_block import summarize_block

class SmartNoteAgent:

    def __init__(self):
        self.summarizer = Summarizer()

    def run(self, user_text: str):
        """Orchestrates: extract → search → compress → final summary"""

        # Step 1 — extract key points
        extracted = extract_key_points(user_text)

        # Step 2 — run a search on 1 key point
        search_term = extracted["key_points"].split("\n")[0]
        search_results = google_search(search_term)

        # Step 3 — compress the full block
        compressed = summarize_block(user_text)

        # Step 4 — fuse everything
        final = f"""
=== KEY POINTS ===
{extracted["key_points"]}

=== SEARCH INSIGHTS ===
{search_results}

=== COMPRESSED OVERVIEW ===
{compressed["summary"]}
        """

        return final
