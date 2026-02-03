# LangChain

[**LangChain**](https://docs.langchain.com/oss/python/langchain/short-term-memory) é um framework de código aberto com uma arquitetura de agentes pré-construída e integrações para qualquer modelo. Fornece uma arquitetura de agente pré-construída e integrações de modelos para ajudar você a começar rapidamente e incorporar LLMs em seus agentes e aplicativos de forma integrada.

---

```python
# pip install -qU langchain "langchain[anthropic]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-5-20250929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```