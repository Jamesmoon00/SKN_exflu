import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# 메인 화면 설정
st.title("Streamlit Multi-Page Application")

st.write("""
Welcome to the multi-page LLM application!
Use the sidebar to navigate between different pages.
""")

# Main Page
st.title("Main Page")
st.write("Welcome to the Main Page! Use the buttons below to navigate.")

col1, col2, _ = st.columns([1, 1, 3])

# 버튼으로 페이지 이동
with col1:
    if st.button("DB Data Search"):
        switch_page("DB_Data_Search")
with col2:
    if st.button("LLM Model"):
        switch_page("llm_model")