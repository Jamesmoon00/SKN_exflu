from openai_chatbot.langchain_last_mini.constant import CHATBOT_ROLE, CHATBOT_MESSAGE
from openai_chatbot.langchain_last_mini.prompt import create_message
from openai_chatbot.langchain_last_mini.chat import response_from_langchain, response_from_runnable_lambda, response_from_runnable_parallel, response_from_langgraph
import streamlit as st
from openai_chatbot.langchain_last_mini.utils import init_chatbot
from streamlit_extras.switch_page_button import switch_page

page = st.sidebar.selectbox(
    "Select a page",
    ["llm_main_page", "llm model test ver", "backend connection test"],  # "Select a page" 옵션 제거
    index=1  # langchain_agent를 기본 선택값으로 설정
)

init_chatbot()

st.title("Chat Bot final mini")

# ... existing code ...

# 메세지를 저장 
# messages = {"role":"", "content":""}
#   role -> user(사용자) / assistant(AI)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 저장한 메세지를 화면에 표현 
for message in st.session_state.messages:
    if message[CHATBOT_MESSAGE.role.name] in CHATBOT_ROLE.__members__:
        with st.chat_message(message[CHATBOT_MESSAGE.role.name]):
            st.markdown(message[CHATBOT_MESSAGE.content.name])

# 사용자 입력
prompt = st.chat_input("입력해주세요")
# 사용자 입력이 있다면,
if prompt:
    message = create_message(role=CHATBOT_ROLE.user, prompt=prompt)
    
    if message:
        # 화면에 표현
        with st.chat_message(CHATBOT_ROLE.user.name):
            st.write(prompt)
        # st.session_state.messages.append({"role" : "user", "content": prompt})
        # 챗봇 답변 
        with st.chat_message(CHATBOT_ROLE.assistant.name):
            # assistant_response = response_from_llm(prompt)
            # st.markdown(assistant_response)
            assistant_response = st.write(response_from_langgraph(prompt=prompt, message_history=st.session_state.messages))
            # st.session_state.messages.append({"role": "assistant", "content": assistant_response})
