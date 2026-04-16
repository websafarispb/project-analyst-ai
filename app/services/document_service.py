from pathlib import Path


class DocumentService:
    def __init__(self, documents_dir: str = "documents"):
        self.documents_path = Path(documents_dir)

    def list_documents(self) -> list[str]:
        if not self.documents_path.exists():
            return []

        return sorted(
            [
                file_path.name
                for file_path in self.documents_path.iterdir()
                if file_path.is_file()
            ]
        )

    def read_document(self, file_name: str) -> str:
        file_path = self.documents_path / file_name

        if not file_path.exists() or not file_path.is_file():
            raise FileNotFoundError(f"Document '{file_name}' was not found")

        return file_path.read_text(encoding="utf-8")

    def read_all_documents(self) -> dict[str, str]:
        documents: dict[str, str] = {}

        for file_name in self.list_documents():
            documents[file_name] = self.read_document(file_name)

        return documents