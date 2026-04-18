from fastapi import APIRouter

from app.agents.simple_agent import SimpleAgent
from app.models.agent_models import AgentRequest, AgentResponse
from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.analysis_service import AnalysisService

router = APIRouter()

analysis_service = AnalysisService()
simple_agent = SimpleAgent()


@router.get("/")
def root():
    return {"message": "Project Analyst AI is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analysis_service.analyze(request)


@router.post("/agent", response_model=AgentResponse)
def agent(request: AgentRequest):
    response = simple_agent.handle(request.query)

    return AgentResponse(
        selected_tool=response["selected_tool"],
        reason=response["reason"],
        result=response["result"],
    )