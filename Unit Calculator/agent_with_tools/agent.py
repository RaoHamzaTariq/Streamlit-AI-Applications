import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from agent_with_tools.tools import Tools
from langchain_core.messages import HumanMessage

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

tools = Tools()
unit_converting_tools = [
    tools.convert_area,
    tools.convert_length,
    tools.convert_mass,
    tools.convert_temperature,
    tools.convert_time,
    tools.convert_volume
]

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)

llm_with_tools = llm.bind_tools(unit_converting_tools)


def tool_calling_agent(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}  # Append the new message

graph_builder : StateGraph = StateGraph(MessagesState)

graph_builder.add_node("tool_calling_agent", tool_calling_agent)
graph_builder.add_node("tools", ToolNode(unit_converting_tools))

graph_builder.add_edge(START, "tool_calling_agent")
graph_builder.add_conditional_edges("tool_calling_agent", tools_condition)
graph_builder.add_edge("tools", END) 
graph : CompiledStateGraph = graph_builder.compile()

messages = [HumanMessage(content="Convert 10 kg to pounds")]
result = graph.invoke({"messages":messages})
