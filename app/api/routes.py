from fastapi import APIRouter

from app.models.request_models import AnalyzeRequest
from app.models.response_models import AnalyzeResponse
from app.services.analysis_service import AnalysisService

router = APIRouter()

analysis_service = AnalysisService()


@router.get("/")
def root():
    return {"message": "Project Analyst AI is running"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    return analysis_service.analyze(request)