from app.models.request_models import AnalyzeRequest
from app.services.analysis_service import AnalysisService


class AnalyzeDocumentsTool:
    name = "analyze_documents"
    description = "Analyzes project documents and returns structured findings, risks, open questions, and sources for a user query."

    def __init__(self):
        self.analysis_service = AnalysisService()

    def run(self, query: str):
        request = AnalyzeRequest(query=query)
        return self.analysis_service.analyze(request)