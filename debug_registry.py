from app.tools.tool_registry import ToolRegistry


registry = ToolRegistry()

print("Registered tools:")
print(registry.list_tools())

search_tool = registry.get_tool("search_documents")
print("\nSearch tool result:")
print(search_tool.run("risks error handling"))