from app.tools.tool_registry import ToolRegistry


class SimpleAgent:
    def __init__(self):
        self.registry = ToolRegistry()

    def handle(self, user_query: str) -> dict:
        lowered_query = user_query.lower()

        if "list" in lowered_query:
            tool = self.registry.get_tool("list_documents")
            return {
                "selected_tool": tool.name,
                "reason": "The query asks to list available documents.",
                "result": tool.run(),
            }

        if "search" in lowered_query or "find" in lowered_query:
            tool = self.registry.get_tool("search_documents")
            return {
                "selected_tool": tool.name,
                "reason": "The query asks to search or find relevant documents.",
                "result": tool.run(user_query),
            }

        if "read" in lowered_query:
            tool = self.registry.get_tool("read_document")
            file_name = user_query.split()[-1]
            return {
                "selected_tool": tool.name,
                "reason": "The query asks to read a specific document.",
                "result": tool.run(file_name),
            }

        return {
            "selected_tool": None,
            "reason": "No matching tool was found for the query.",
            "result": "I don't know which tool to use",
        }