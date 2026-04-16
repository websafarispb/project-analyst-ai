from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    summary: str
    key_findings: list[str]
    risks: list[str]
    open_questions: list[str]
    sources: list[str]