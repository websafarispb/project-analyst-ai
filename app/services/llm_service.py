class LlmService:
    def analyze(self, query: str, documents: dict[str, str]) -> dict:
        key_findings = []
        risks = []
        open_questions = []

        for file_name, content in documents.items():
            for line in content.splitlines():
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                lowered_line = cleaned_line.lower()

                if "should" in lowered_line or "must" in lowered_line:
                    key_findings.append(f"{file_name}: {cleaned_line}")

                if "risk" in lowered_line:
                    risks.append(f"{file_name}: {cleaned_line}")

                if "question" in lowered_line:
                    open_questions.append(f"{file_name}: {cleaned_line}")

        if not key_findings:
            key_findings.append("No key findings were extracted yet")

        if not risks:
            risks.append("No explicit risks were found in the matched documents")

        if not open_questions:
            open_questions.append("No open questions were found in the matched documents")

        return {
            "summary": f"LLM-style analysis for query: {query}",
            "key_findings": key_findings,
            "risks": risks,
            "open_questions": open_questions,
        }