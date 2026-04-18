# Project Analyst AI

Project Analyst AI is a Python-based AI assistant for analyzing project documents.

The application reads local project files, identifies relevant information, summarizes findings, highlights risks and open questions, and returns structured results.

## Goals

This project is a hands-on learning lab for practical AI engineering concepts:

- tool-based workflows
- structured output
- long-context handling
- summarization pipelines
- reliability and error handling
- orchestration patterns
- preparation for Claude-style agent architecture tasks

## Planned Features

- analyze local project documents
- generate summaries
- identify risks and unresolved questions
- compare documents
- search for specific topics across files
- return structured JSON responses
- support multi-step analysis flow

## Tech Stack

- Python
- FastAPI
- Pydantic

## Project Structure

```text
project-analyst-ai/
├── app/
├── documents/
├── tests/
├── README.md
└── requirements.txt
 ```

### Run local
```commandline
uvicorn app.main:app --reload
```