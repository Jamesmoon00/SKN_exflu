import streamlit as st
import requests
from langchain_last_mini.constant import CHATBOT_ROLE, CHATBOT_MESSAGE
from langchain_last_mini.prompt import create_message
from langchain_last_mini.chat import response_from_langgraph
from langchain_last_mini.utils import init_chatbot
from streamlit_extras.switch_page_button import switch_page

# 백엔드 URL 설정
BACKEND_URL = "https://backdocsend.jamesmoon.click/blog/add"

# 페이지 타이틀 및 버튼
st.title("LLM Model")
col1, col2, _ = st.columns([1, 1, 3])

with col1:
    if st.button("Main Page"):
        switch_page("main")

with col2:
    if st.button("DB Data Search"):
        switch_page("DB_Data_Search")

st.write("LLM model에 적절한 키워드를 입력하세요")

# 로딩 스피너 표시
with st.spinner("페이지를 로드하는 중입니다..."):
    init_chatbot()  # 챗봇 초기화 작업

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
            # print(f'message = {st.session_state.messages[-1]['content']}')

st.write("### 결과 저장하기")
with st.expander("결과 저장하기", expanded=False):  # expanded=False로 기본적으로 접힘 상태
    with st.form("save_form"):
        title = st.text_input("제목을 입력하세요", "챗봇 대화 결과")
        product_id = st.number_input("상품 ID", value=1, step=1)
        is_ad = st.selectbox("광고 여부", [0, 1], format_func=lambda x: "아니오" if x == 0 else "예")
        uploaded_image = st.file_uploader("이미지 업로드 (선택)", type=["jpg", "png", "jpeg"])

        submitted = st.form_submit_button("결과 저장")
        if submitted:
            try:
                if st.session_state.messages:
                    # 마지막 챗봇 응답 내용 가져오기
                    last_response = st.session_state.messages[-1]['content'].strip()

                    # multipart/form-data 전송 준비
                    files = {
                        "title": (None, title),
                        "content": (None, last_response),
                        "product_id": (None, str(int(product_id))),
                        "is_ad": (None, str(int(is_ad)))
                    }

                    # 이미지 파일이 있으면 Content-Type을 명시하고 추가
                    if uploaded_image:
                        files["image"] = (uploaded_image.name, uploaded_image.read(), uploaded_image.type)

                    # 백엔드로 POST 요청
                    response = requests.post(BACKEND_URL, files=files)

                    # 응답 처리
                    if response.status_code == 200:
                        response_data = response.json()
                        st.success(f"저장 성공: {response_data.get('message')}, Post ID: {response_data.get('post_id')}")
                    else:
                        st.error(f"저장 실패: {response.status_code}, {response.text}")
                else:
                    st.warning("저장할 챗봇 답변이 없습니다.")
            except Exception as e:
                st.error(f"오류 발생: {e}")