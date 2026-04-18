from pathlib import Path

from app.core.config import settings


class DocumentService:
    def __init__(self, documents_dir: str = settings.DOCUMENTS_DIR):
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

    def search_documents(self, query: str, limit: int = settings.SEARCH_LIMIT) -> dict[str, str]:
        documents = self.read_all_documents()
        query_words = [self._normalize_word(word) for word in query.split() if word.strip()]

        scored_documents: list[tuple[str, str, int]] = []

        for file_name, content in documents.items():
            content_words = [self._normalize_word(word) for word in content.lower().split()]
            score = sum(1 for word in query_words if word in content_words)

            if score > 0:
                scored_documents.append((file_name, content, score))

        scored_documents.sort(key=lambda item: item[2], reverse=True)

        result: dict[str, str] = {}
        for file_name, content, _score in scored_documents[:limit]:
            result[file_name] = content

        return result

    def _normalize_word(self, word: str) -> str:
        normalized = word.lower().strip(".,!?():;\"'")

        if normalized.endswith("s") and len(normalized) > 3:
            normalized = normalized[:-1]

        return normalized