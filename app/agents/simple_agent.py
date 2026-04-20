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
        score = routing_result["score"]
        scoring_details = routing_result["scoring_details"]
        available_tools = self.registry.list_tools()

        if not tool_name:
            return {
                "selected_tool": None,
                "reason": reason,
                "result": "I don't know which tool to use",
                "score": score,
                "tool_input": tool_input,
                "available_tools": available_tools,
                "scoring_details": scoring_details,
            }

        tool = self.registry.get_tool(tool_name)

        if not tool:
            return {
                "selected_tool": None,
                "reason": f"Tool '{tool_name}' was not found in registry.",
                "result": "Tool not found",
                "score": score,
                "tool_input": tool_input,
                "available_tools": available_tools,
                "scoring_details": scoring_details,
            }

        raw_result = tool.run(**tool_input)

        if hasattr(raw_result, "model_dump"):
            result = raw_result.model_dump()
        else:
            result = raw_result

        return {
            "selected_tool": tool.name,
            "reason": reason,
            "result": result,
            "score": score,
            "tool_input": tool_input,
            "available_tools": available_tools,
            "scoring_details": scoring_details,
        }