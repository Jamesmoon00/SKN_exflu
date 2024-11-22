import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Main Application Page")

st.markdown("""page select""")

col1, col2 = st.columns(2)

with col1:
    if st.button("llm model test ver"):
        switch_page("llm_model")

with col2:
    if st.button("backend connection test"):
        switch_page("connection_test")
        
page = st.sidebar.selectbox(
    "Select a page",
    ["llm_main_page", "llm model test ver", "backend connection test"],  # "Select a page" 옵션 제거
    index=0  # langchain_agent를 기본 선택값으로 설정
)

if page == "home":
    switch_page("streamlit_main_page")
elif page == "llm model test ver":
    switch_page("llm_model")
elif page == "backend connection test":
    switch_page("connection_test")