# mcp_server/tools/google_search.py

def google_search(query: str):
    """
    Mock Google search tool.
    Replace later with SERPAPI, Bing, or Google API.
    """

    return {
        "query": query,
        "results": [
            {"title": "Result 1", "snippet": "Sample snippet 1"},
            {"title": "Result 2", "snippet": "Sample snippet 2"},
        ]
    }
