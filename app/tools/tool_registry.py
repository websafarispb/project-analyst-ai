from app.tools.analyze_documents_tool import AnalyzeDocumentsTool
from app.tools.list_documents_tool import ListDocumentsTool
from app.tools.read_document_tool import ReadDocumentTool
from app.tools.search_documents_tool import SearchDocumentsTool


class ToolRegistry:
    def __init__(self):
        self.tools = {
            ListDocumentsTool.name: ListDocumentsTool(),
            SearchDocumentsTool.name: SearchDocumentsTool(),
            ReadDocumentTool.name: ReadDocumentTool(),
            AnalyzeDocumentsTool.name: AnalyzeDocumentsTool(),
        }

    def get_tool(self, tool_name: str):
        return self.tools.get(tool_name)

    def list_tools(self) -> list[dict[str, str]]:
        return [
            {
                "name": tool.name,
                "description": tool.description
            }
            for tool in self.tools.values()
        ]