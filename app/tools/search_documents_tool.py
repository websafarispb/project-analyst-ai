from app.services.document_service import DocumentService


class SearchDocumentsTool:
    name = "search_documents"
    description = "Searches project documents for relevant information, including risks, issues, or specific topics based on a user query."

    def __init__(self):
        self.document_service = DocumentService()

    def run(self, query: str) -> dict[str, str]:
        return self.document_service.search_documents(query)