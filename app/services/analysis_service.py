from app.core.config import settings
from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.document_service import DocumentService
from app.services.llm_service import LlmService
from app.tools.list_documents_tool import ListDocumentsTool
from app.tools.read_document_tool import ReadDocumentTool
from app.tools.search_documents_tool import SearchDocumentsTool


class AnalysisService:
    def __init__(self):
        self.list_documents_tool = ListDocumentsTool()
        self.search_documents_tool = SearchDocumentsTool()
        self.read_document_tool = ReadDocumentTool()
        self.document_service = DocumentService()
        self.llm_service = LlmService()

    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        matched_documents = self.search_documents_tool.run(request.query)
        used_fallback = False

        if not matched_documents and settings.FALLBACK_TO_ALL_DOCUMENTS:
            available_documents = self.list_documents_tool.run()
            matched_documents = {
                file_name: self.read_document_tool.run(file_name)
                for file_name in available_documents
            }
            used_fallback = True

        source_names = list(matched_documents.keys())

        llm_result = self.llm_service.analyze(request.query, matched_documents)

        summary = llm_result.summary
        if used_fallback:
            summary += " (fallback to all documents was used)"

        return AnalyzeResponse(
            summary=summary,
            key_findings=llm_result.key_findings,
            risks=llm_result.risks,
            open_questions=llm_result.open_questions,
            sources=source_names
        )