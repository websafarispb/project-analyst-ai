from app.agents.simple_agent import SimpleAgent

agent = SimpleAgent()

print(agent.handle("list documents"))
print("\n---\n")

print(agent.handle("find risks"))
print("\n---\n")

print(agent.handle("read requirements.md"))