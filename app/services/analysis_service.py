from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse


class AnalysisService:
    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        return AnalyzeResponse(
            summary=f"Analysis for query: {request.query}",
            key_findings=[
                "No real analysis yet",
                "This is the first placeholder response"
            ],
            risks=[
                "LLM integration is not implemented yet"
            ],
            open_questions=[
                "Which documents should be analyzed first?"
            ],
            sources=[]
        )