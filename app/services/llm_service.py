class LlmService:
    def analyze(self, query: str, documents: dict[str, str]) -> dict:
        return {
            "summary": f"[LLM] Simulated analysis for query: {query}",
            "key_findings": [
                "LLM-based findings are not implemented yet"
            ],
            "risks": [
                "LLM integration is currently a stub"
            ],
            "open_questions": [
                "How should LLM prompts be designed?"
            ]
        }
