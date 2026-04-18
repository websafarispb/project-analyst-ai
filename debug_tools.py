from app.tools.list_documents_tool import ListDocumentsTool
from app.tools.search_documents_tool import SearchDocumentsTool


list_tool = ListDocumentsTool()
search_tool = SearchDocumentsTool()

print("Available documents:")
print(list_tool.run())

print("\nSearch result:")
print(search_tool.run("risks error handling"))