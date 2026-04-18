from pydantic import BaseModel


class AgentRequest(BaseModel):
    query: str


class ToolInfo(BaseModel):
    name: str
    description: str


class ToolScoreInfo(BaseModel):
    tool_name: str
    score: int
    searchable_text: str


class AgentResponse(BaseModel):
    selected_tool: str | None
    reason: str
    result: str
    score: int
    tool_input: dict
    available_tools: list[ToolInfo]
    scoring_details: list[ToolScoreInfo]