from langchain.agents import create_openai_functions_agent
from langchain_last_mini.model import creat_chat_model
from langchain_last_mini.langgraph.tools import get_langgraph_tools
from langchain_last_mini.prompt import pull_langgraph_prompt, create_prompt

# agent_runnable
def create_openai_langgraph_agent():
    llm = creat_chat_model(model_id="gpt-4o-mini", streaming=True)
    tools = get_langgraph_tools()
    prompt = create_prompt()
    return create_openai_functions_agent(llm, tools, prompt) # 이게 agent-scratchpad를 필요로 하는 함수여서 프롬프트에 agent-scratchpad가 무조건 들어가야 함