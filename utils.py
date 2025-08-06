# utils.py

import re

def highlight_text(text, query):
    """Highlight query terms in the response text."""
    query_terms = query.lower().split()
    for term in query_terms:
        pattern = re.compile(rf"({re.escape(term)})", re.IGNORECASE)
        text = pattern.sub(r"**\1**", text)
    return text

def format_response(response):
    """Format response for better readability."""
    return response.strip().replace("\n", "\n\n")
