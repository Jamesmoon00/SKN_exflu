# TavilySearchResults 클래스를 langchain_community.tools.tavily_search 모듈에서 가져옵니다.
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor
import streamlit as st

@st.cache_resource # 객체를 caching 처리 
def get_client(model_id='gpt-4o-mini', temperature = 0):
    return ChatOpenAI(model = model_id, temperature=temperature)

def response_taviny_results(prompt):
    # TavilySearchResults 클래스의 인스턴스를 생성합니다
    # k=5은 검색 결과를 5개까지 가져오겠다는 의미입니다
    search = TavilySearchResults(k=3)

    # tools 리스트에 search와 retriever_tool을 추가합니다.
    tools = [search]

    # ChatOpenAI 클래스를 langchain_openai 모듈에서 가져옵니다.
    llm = get_client(model_id="gpt-4o-mini", temperature=0)

    # hub에서 prompt를 가져옵니다 - 이 부분을 수정할 수 있습니다!
    agent_prompt = hub.pull("hwchase17/openai-functions-agent")

    # OpenAI 함수 기반 에이전트를 생성합니다.
    # llm, tools, prompt를 인자로 사용합니다.
    agent = create_openai_functions_agent(llm, tools, agent_prompt)

    # AgentExecutor 클래스를 사용하여 agent와 tools를 설정하고, 상세한 로그를 출력하도록 verbose를 True로 설정합니다.
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

    response = agent_executor.invoke({"input": prompt})
    # print(f'taviny response = {response}')

    return response['output']