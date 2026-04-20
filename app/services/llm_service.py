from app.core.config import settings
from app.services.claude_llm_service import ClaudeLlmService
from app.services.fake_llm_service import FakeLlmService


class LlmService:
    def __init__(self):
        if settings.LLM_PROVIDER == "claude":
            self.provider = ClaudeLlmService()
        else:
            self.provider = FakeLlmService()

    def analyze(self, query: str, documents: dict[str, str]):
        return self.provider.analyze(query, documents)