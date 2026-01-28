#import threading
from collections.abc import Sequence
from typing import Annotated, TypedDict
#from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph, add_messages
from langgraph.graph.state import RunnableConfig
from langgraph.graph.message import Messages
from rich import print
from rich.markdown import Markdown

#def reducer(a: Messages, b: Messages) -> Messages:
    #print("> reducer")
    #return add_messages(a, b)

# 1 - Definição de state
class AgentState(TypedDict):
    #messages: Annotated[Sequence[BaseMessage], reducer]
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 2 - Definição de nodes
def call_llm_node(state: AgentState) -> AgentState:
    llm_result = AIMessage("Hello back at you!")
    return {"messages": [llm_result]}

# 3 - Definição do StateGraph
builder = StateGraph(
    AgentState, context_schema=None, input_schema=AgentState, output_schema=AgentState
)

# 4 - Adicionando nodes ao StateGraph
builder.add_node("call_llm", call_llm_node)
builder.add_edge(START, "call_llm")
builder.add_edge("call_llm", END)

# 5 - Compilando grafo
graph = builder.compile()

# 6 - Executando o grafo
if __name__ == "__main__":
    human_message = HumanMessage("Hello there!")
    result = graph.invoke({"messages": [human_message]})
    print(result)