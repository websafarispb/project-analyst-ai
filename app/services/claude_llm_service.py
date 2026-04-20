import json
from anthropic import Anthropic

from app.core.config import settings
from app.models.response_models import AnalyzeResponse


class ClaudeLlmService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def analyze(self, query: str, documents: dict[str, str]) -> AnalyzeResponse:
        prompt = self._build_prompt(query, documents)

        for attempt in range(2):
            try:
                response = self.client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=2000,
                    temperature=0,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    output_config={
                        "format": {
                            "type": "json_schema",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "summary": {"type": "string"},
                                    "key_findings": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    },
                                    "risks": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    },
                                    "open_questions": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    },
                                    "sources": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                    },
                                },
                                "required": [
                                    "summary",
                                    "key_findings",
                                    "risks",
                                    "open_questions",
                                    "sources",
                                ],
                                "additionalProperties": False,
                            },
                        }
                    },
                )

                if response.stop_reason in {"refusal", "max_tokens"}:
                    raise ValueError(
                        f"Claude did not return a usable structured response. stop_reason={response.stop_reason}"
                    )

                text = response.content[0].text
                parsed = json.loads(text)

                return AnalyzeResponse(**parsed)

            except Exception as error:
                print(f"Claude analyze attempt {attempt + 1} failed: {error}")

                if attempt == 1:
                    return AnalyzeResponse(
                        summary="Claude request failed, fallback response was used.",
                        key_findings=[],
                        risks=[],
                        open_questions=[],
                        sources=list(documents.keys()),
                    )

        return AnalyzeResponse(
            summary="Unexpected fallback response.",
            key_findings=[],
            risks=[],
            open_questions=[],
            sources=list(documents.keys()),
        )

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
- Analyze only the provided documents
- Extract key findings
- Extract risks
- Extract open questions
- Keep the summary concise
- Include the file names that contributed to the answer in "sources"
"""