from app.tools.tool_registry import ToolRegistry


class AgentRouter:
    def __init__(self):
        self.registry = ToolRegistry()

    def route(self, user_query: str) -> dict:
        query_words = self._normalize_text(user_query).split()
        tools = self.registry.list_tools()

        best_tool = None
        best_score = 0
        scoring_details = []

        for tool in tools:
            searchable_text = self._normalize_text(
                f"{tool['name']} {tool['description']}"
            )

            score = sum(1 for word in query_words if word in searchable_text)

            scoring_details.append({
                "tool_name": tool["name"],
                "score": score,
                "searchable_text": searchable_text
            })

            if score > best_score:
                best_score = score
                best_tool = tool

        if not best_tool or best_score == 0:
            return {
                "tool_name": None,
                "tool_input": {},
                "reason": "No matching tool was found for the query.",
                "score": 0,
                "scoring_details": scoring_details
            }

        return {
            "tool_name": best_tool["name"],
            "tool_input": self._build_tool_input(best_tool["name"], user_query),
            "reason": f"Selected tool '{best_tool['name']}' based on query-to-tool description matching.",
            "score": best_score,
            "scoring_details": scoring_details
        }

    def _build_tool_input(self, tool_name: str, user_query: str) -> dict:
        if tool_name == "list_documents":
            return {}

        if tool_name == "search_documents":
            return {"query": user_query}

        if tool_name == "read_document":
            file_name = user_query.split()[-1]
            return {"file_name": file_name}

        if tool_name == "analyze_documents":
            return {"query": user_query}

        return {}

    def _normalize_text(self, text: str) -> str:
        return text.lower().strip()