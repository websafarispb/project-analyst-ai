class AgentRouter:
    def route(self, user_query: str) -> dict:
        lowered_query = user_query.lower()

        if "list" in lowered_query:
            return {
                "tool_name": "list_documents",
                "reason": "The query asks to list available documents."
            }

        if "search" in lowered_query or "find" in lowered_query:
            return {
                "tool_name": "search_documents",
                "reason": "The query asks to search or find relevant documents."
            }

        if "read" in lowered_query:
            return {
                "tool_name": "read_document",
                "reason": "The query asks to read a specific document."
            }

        return {
            "tool_name": None,
            "reason": "No matching tool was found for the query."
        }