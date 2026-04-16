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

        key_findings: list[str] = []
        risks: list[str] = []
        open_questions: list[str] = []

        for file_name, content in matched_documents.items():
            lines = content.splitlines()

            for line in lines:
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                lowered_line = cleaned_line.lower()

                if "risk" in lowered_line:
                    risks.append(f"{file_name}: {cleaned_line}")

                if "question" in lowered_line:
                    open_questions.append(f"{file_name}: {cleaned_line}")

                if "should" in lowered_line or "must" in lowered_line:
                    key_findings.append(f"{file_name}: {cleaned_line}")

        if not key_findings:
            key_findings.append("No key findings were extracted yet")

        if not risks:
            risks.append("No explicit risks were found in the matched documents")

        if not open_questions:
            open_questions.append("No open questions were found in the matched documents")

        return AnalyzeResponse(
            summary=f"Analysis for query: {request.query}",
            key_findings=key_findings,
            risks=risks,
            open_questions=open_questions,
            sources=source_names
        )