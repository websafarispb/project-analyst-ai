from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.document_service import DocumentService


class AnalysisService:
    def __init__(self):
        self.document_service = DocumentService()

    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        matched_documents = self.document_service.search_documents(request.query)
        source_names = list(matched_documents.keys())

        if not matched_documents:
            return AnalyzeResponse(
                summary=f"No relevant documents found for query: {request.query}",
                key_findings=[
                    "The search did not find matching documents"
                ],
                risks=[],
                open_questions=[
                    "Should we fall back to analyzing all documents when no matches are found?"
                ],
                sources=[]
            )

        return AnalyzeResponse(
            summary=f"Analysis for query: {request.query}",
            key_findings=[
                f"Found {len(matched_documents)} relevant documents",
                "Simple keyword-based retrieval is now implemented"
            ],
            risks=[
                "Search is still very basic and may miss semantically relevant documents"
            ],
            open_questions=[
                "Should search use better ranking in the next version?"
            ],
            sources=source_names
        )