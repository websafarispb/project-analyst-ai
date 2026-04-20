class Settings:
    DOCUMENTS_DIR = "documents"
    SEARCH_LIMIT = 3
    FALLBACK_TO_ALL_DOCUMENTS = True
    LLM_PROVIDER: str = "claude"
    ANTHROPIC_API_KEY: str = ""

settings = Settings()