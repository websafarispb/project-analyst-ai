from app.agents.agent_router import AgentRouter
from app.tools.tool_registry import ToolRegistry


class SimpleAgent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.router = AgentRouter()

    def handle(self, user_query: str) -> dict:
        routing_result = self.router.route(user_query)
        tool_name = routing_result["tool_name"]
        reason = routing_result["reason"]

        if not tool_name:
            return {
                "selected_tool": None,
                "reason": reason,
                "result": "I don't know which tool to use",
            }

        tool = self.registry.get_tool(tool_name)

        if tool_name == "list_documents":
            result = tool.run()
        elif tool_name == "search_documents":
            result = tool.run(user_query)
        elif tool_name == "read_document":
            file_name = user_query.split()[-1]
            result = tool.run(file_name)
        else:
            return {
                "selected_tool": None,
                "reason": f"Tool '{tool_name}' is not supported yet.",
                "result": "Unsupported tool",
            }

        return {
            "selected_tool": tool.name,
            "reason": reason,
            "result": str(result),
        }