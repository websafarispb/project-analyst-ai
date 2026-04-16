from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.document_service import DocumentService


class AnalysisService:
    def __init__(self):
        self.document_service = DocumentService()

    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        documents = self.document_service.read_all_documents()
        source_names = list(documents.keys())

        return AnalyzeResponse(
            summary=f"Analysis for query: {request.query}",
            key_findings=[
                f"Loaded {len(documents)} documents for analysis",
                "Real document reading is now implemented"
            ],
            risks=[
                "LLM integration is not implemented yet"
            ],
            open_questions=[
                "How should relevant documents be selected for each query?"
            ],
            sources=source_names
        )