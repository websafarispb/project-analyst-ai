from app.models.response_models import AnalyzeResponse

class FakeLlmService:
    def analyze(self, query: str, documents: dict[str, str]) -> AnalyzeResponse:
        prompt = self._build_prompt(query, documents)

        raw_response = self._simulate_llm_response(query, documents)

        return AnalyzeResponse(**raw_response)

    def _build_prompt(self, query: str, documents: dict[str, str]) -> str:
        docs_text = ""

        for file_name, content in documents.items():
            docs_text += f"\n---\nFILE: {file_name}\n{content}\n"

        return f"""
You are an AI system that analyzes project documents.

User query:
{query}

Documents:
{docs_text}

Instructions:
- Extract key findings
- Extract risks
- Extract open questions
- Return structured JSON

Output format:
{{
  "summary": "...",
  "key_findings": ["..."],
  "risks": ["..."],
  "open_questions": ["..."]
}}
"""

    def _simulate_llm_response(self, query: str, documents: dict[str, str]) -> dict:
        key_findings = []
        risks = []
        open_questions = []

        for file_name, content in documents.items():
            for line in content.splitlines():
                cleaned = line.strip()
                if not cleaned:
                    continue

                lower = cleaned.lower()

                if "should" in lower or "must" in lower:
                    key_findings.append(f"{file_name}: {cleaned}")

                if "risk" in lower:
                    risks.append(f"{file_name}: {cleaned}")

                if "question" in lower:
                    open_questions.append(f"{file_name}: {cleaned}")

        return {
            "summary": f"LLM-style analysis for query: {query}",
            "key_findings": key_findings or ["No findings"],
            "risks": risks or ["No risks found"],
            "open_questions": open_questions or ["No open questions"],
            "sources": list(documents.keys())
        }
