##      Define the graph
from langgraph.graph import END, StateGraph
from langchain_openai_api.langgraph.state import AgentState
from langchain_openai_api.langgraph.nodes import run_agent, execute_tools, should_continue, call_model, go_web_search, is_response_adequate
from langgraph.checkpoint.memory import MemorySaver

# lang-graph structure
def create_graph_structure():
    workflow = StateGraph(AgentState)
    workflow.set_entry_point("agent")
    workflow.add_node("agent", run_agent)
    workflow.add_node("action", go_web_search)
    workflow.add_node("memory_node", call_model)
    workflow.add_conditional_edges(
        "agent",
        is_response_adequate,
        {
            "use_search": "action",
            "final_response": "memory_node"
        }
    )
    workflow.add_edge('action', 'memory_node')
    workflow.add_edge("memory_node", END)
    return workflow

# app
def set_workflow_to_app():   # really this is the graph.
    # Add simple in-memory checkpointer
    memory = MemorySaver()
    return create_graph_structure().compile(checkpointer=memory)    # to be like an app in here