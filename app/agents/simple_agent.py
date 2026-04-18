from app.agents.agent_router import AgentRouter
from app.tools.tool_registry import ToolRegistry


class SimpleAgent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.router = AgentRouter()

    def handle(self, user_query: str) -> dict:
        routing_result = self.router.route(user_query)
        tool_name = routing_result["tool_name"]
        tool_input = routing_result["tool_input"]
        reason = routing_result["reason"]

        if not tool_name:
            return {
                "selected_tool": None,
                "reason": reason,
                "result": "I don't know which tool to use",
            }

        tool = self.registry.get_tool(tool_name)

        if not tool:
            return {
                "selected_tool": None,
                "reason": f"Tool '{tool_name}' was not found in registry.",
                "result": "Tool not found",
            }

        result = tool.run(**tool_input)

        return {
            "selected_tool": tool.name,
            "reason": reason,
            "result": str(result),
        }