##   Custom Tools
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_exaone_api.model import creat_chat_model

import random

@tool("upper_case", return_direct=True)
def to_lower_case(input:str) -> str:
  """Returns the input as all upper case."""
  return input.upper() #.lower()

@tool("random_number", return_direct=True)
def random_number_maker(input:str) -> str:
    """Returns a random number between 0-100."""
    return random.randint(0, 100)

# @tool("taviny_searcher", return_direct=True)
# def response_taviny_results(input: str) -> str:
#     """Tavily 검색 엔진을 사용하여 최신 정보를 검색하는 도구입니다."""
#     # TavilySearchResults 클래스의 인스턴스를 생성합니다
#     search = TavilySearchResults()
#     result = search.run(input)
#     return result

    # llm = creat_chat_model(model_id="gpt-4o-mini", temperature=0)
    # # 에이전트 프롬프트를 가져옵니다
    # agent_prompt = hub.pull("hwchase17/openai-functions-agent")
    # # 에이전트를 생성합니다
    # agent = create_openai_functions_agent(llm, tools=[search], prompt=agent_prompt)

    # # 에이전트 실행기를 생성합니다
    # agent_executor = AgentExecutor(agent=agent, tools=[search], verbose=False)
    # print("------------------------------------------------------")
    # print(agent_executor)
    # # 에이전트를 실행하고 응답을 받습니다
    # response = agent_executor.run(input)
    # print(response)
    # # 응답을 반환합니다
    # return response

# tools
def get_langgraph_tools():
    return [to_lower_case, random_number_maker]