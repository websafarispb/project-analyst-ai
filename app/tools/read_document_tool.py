from app.services.document_service import DocumentService


class ReadDocumentTool:
    name = "read_document"
    description = "Reads and returns the full text content of a document by file name."

    def __init__(self):
        self.document_service = DocumentService()

    def run(self, file_name: str) -> str:
        return self.document_service.read_document(file_name)