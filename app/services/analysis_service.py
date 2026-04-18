from app.core.config import settings
from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.document_service import DocumentService
from app.services.llm_service import LlmService


class AnalysisService:
    def __init__(self):
        self.document_service = DocumentService()
        self.llm_service = LlmService()

    def analyze(self, request: AnalyzeRequest) -> AnalyzeResponse:
        matched_documents = self.document_service.search_documents(request.query)
        used_fallback = False

        if not matched_documents and settings.FALLBACK_TO_ALL_DOCUMENTS:
            matched_documents = self.document_service.read_all_documents()
            used_fallback = True

        source_names = list(matched_documents.keys())

        key_findings = self._extract_key_findings(matched_documents)
        risks = self._extract_risks(matched_documents)
        open_questions = self._extract_open_questions(matched_documents)

        if not key_findings:
            key_findings.append("No key findings were extracted yet")

        if not risks:
            risks.append("No explicit risks were found in the matched documents")

        if not open_questions:
            open_questions.append("No open questions were found in the matched documents")

        summary = f"Analysis for query: {request.query}"
        if used_fallback:
            summary += " (fallback to all documents was used)"

        llm_result = self.llm_service.analyze(request.query, matched_documents)

        return AnalyzeResponse(
            summary=llm_result["summary"],
            key_findings=llm_result["key_findings"],
            risks=llm_result["risks"],
            open_questions=llm_result["open_questions"],
            sources=source_names
        )

    def _extract_key_findings(self, documents: dict[str, str]) -> list[str]:
        findings: list[str] = []

        for file_name, content in documents.items():
            for line in content.splitlines():
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                lowered_line = cleaned_line.lower()

                if "should" in lowered_line or "must" in lowered_line:
                    findings.append(f"{file_name}: {cleaned_line}")

        return findings

    def _extract_risks(self, documents: dict[str, str]) -> list[str]:
        risks: list[str] = []

        for file_name, content in documents.items():
            for line in content.splitlines():
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                lowered_line = cleaned_line.lower()

                if "risk" in lowered_line:
                    risks.append(f"{file_name}: {cleaned_line}")

        return risks

    def _extract_open_questions(self, documents: dict[str, str]) -> list[str]:
        questions: list[str] = []

        for file_name, content in documents.items():
            for line in content.splitlines():
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                lowered_line = cleaned_line.lower()

                if "question" in lowered_line:
                    questions.append(f"{file_name}: {cleaned_line}")

        return questions