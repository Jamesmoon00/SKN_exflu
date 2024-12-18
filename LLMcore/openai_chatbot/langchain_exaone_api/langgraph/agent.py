from langchain.agents import create_openai_functions_agent
from langchain_exaone_api.model import creat_chat_model
from langchain_exaone_api.langgraph.tools import get_langgraph_tools
from langchain_exaone_api.prompt import pull_langgraph_prompt, create_prompt

# agent_runnable
def create_openai_langgraph_agent(tools, llm=None):
    llm = llm
    tools = tools,
    prompt = create_prompt()
    return create_openai_functions_agent(llm, tools, prompt) # 이게 agent-scratchpad를 필요로 하는 함수여서 프롬프트에 agent-scratchpad가 무조건 들어가야 함