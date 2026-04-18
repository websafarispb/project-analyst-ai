from app.services.document_service import DocumentService


class ListDocumentsTool:
    name = "list_documents"
    description = "Returns the list of available document file names."

    def __init__(self):
        self.document_service = DocumentService()

    def run(self) -> list[str]:
        return self.document_service.list_documents()