from langchain_core.agents import AgentFinish
from langgraph.prebuilt.tool_executor import ToolExecutor
from langchain_last_mini.langgraph.tools import get_langgraph_tools 
from langchain_last_mini.langgraph.agent import create_openai_langgraph_agent
from langchain_core.messages import trim_messages, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_last_mini.model import creat_chat_model
from langchain_last_mini.langgraph.state import AgentState
from langchain_last_mini.taviny.taviny import response_taviny_results
# 트리머 설정 함수
def set_trimmer():
    return trim_messages(strategy="last", max_tokens=50, token_counter=len)

# 모델을 호출하는 함수
def call_model(state):
    # print(state)
    # 필요 시 메시지를 트리밍
    trimmed_messages = set_trimmer().invoke(state["chat_history"])
    print("--------------")
    print(trimmed_messages)
    # 시스템 프롬프트와 메시지 설정
    messages = [SystemMessage(content="You are a helpful assistant. Answer all questions to the best of your ability.")] + trimmed_messages
    # print(messages)
    # print(f'save_response 111111 = {state}')
    # 모델 호출
    # agent_outcome = creat_chat_model().invoke(messages)
    # print(f'save_response 22222 = {state}')
    # 상태 업데이트
    # state["agent_outcome"] = agent_outcome
    print(f'save_response 33333 = {state}')
    try:
        state["chat_history"].append({'role': 'assistant', 'content': state['agent_outcome'].return_values['output']}) 
    except:
        state["chat_history"].append({'role': 'assistant', 'content': state['agent_outcome']}) 
    return state

# 에이전트를 실행하는 함수
def run_agent(state):
    agent_outcome = create_openai_langgraph_agent().invoke(state)
    state["agent_outcome"] = agent_outcome
    # 사용자 메시지를 메모리에 추가
    state["chat_history"].append({'role': 'user', 'content': state["input"]})
    
    return state

# 도구를 실행하는 함수
def execute_tools(state):
    agent_action = state['agent_outcome']
    output = ToolExecutor(get_langgraph_tools()).invoke(agent_action)
    state["intermediate_steps"] = [(agent_action, str(output))]
    return state

# 검색을 하는 함수
def go_web_search(state):
    state["agent_outcome"] = response_taviny_results(state["input"])
    # state["agent_outcome"] = app.invoke({"input": state["input"]})
    # print(state)
    # print(f'go_web_search_state = {state}')
    return state

def is_response_adequate(state):
    response = state["agent_outcome"]
    # print(f'is_response_adequate = {state}')
    # 간단한 검증 로직: 응답이 없거나 "모르겠습니다" 등의 패턴이 포함된 경우 부적절하다고 판단
    inadequate_responses = ["모르", "알 수 없", "죄송하"]
    if not response or any(phrase in response.return_values['output'] for phrase in inadequate_responses):
        # print("----------------")
        return "use_search"
    else:
        return "final_response"


# 메시지 분기 함수
def should_continue(state):
    if isinstance(state['agent_outcome'], AgentFinish):
        return "end"
    else:
        return "continue"