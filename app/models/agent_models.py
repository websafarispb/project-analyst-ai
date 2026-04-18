from pydantic import BaseModel


class AgentRequest(BaseModel):
    query: str


class AgentResponse(BaseModel):
    selected_tool: str | None
    reason: str
    result: str


class ToolInfo(BaseModel):
    name: str
    description: str