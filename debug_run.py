from app.models.request_models import AnalyzeRequest
from app.services.analysis_service import AnalysisService

service = AnalysisService()
request = AnalyzeRequest(query="risks error handling")
#request = AnalyzeRequest(query="database sharding kubernetes")

result = service.analyze(request)

print(result)