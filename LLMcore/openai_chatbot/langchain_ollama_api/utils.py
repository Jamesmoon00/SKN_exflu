import os 
import boto3
import streamlit as st

@st.cache_data(show_spinner=False) # 데이터를 caching 처리 
def __set_openai_api_key():
  OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)
  TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY', None)

  if not OPENAI_API_KEY:
    ssm = boto3.client('ssm')
    # /TEST/CICD/STREAMLIT/OPENAI_API_KEY이걸 AWS parameter store의 이름에 그대로 적용해야 함!!!
    parameter = ssm.get_parameter(Name='/TEST/CICD/STREAMLIT/OPENAI_API_KEY', WithDecryption=True)
    # 여기에 env에 입력하는 API key를 넣으면 paramstore라는 AWS 서비스에서 적용되어 인식
    os.environ['OPENAI_API_KEY'] = parameter['Parameter']['Value']

  if not TAVILY_API_KEY:
    ssm = boto3.client('ssm')
    # /TEST/CICD/STREAMLIT/OPENAI_API_KEY이걸 AWS parameter store의 이름에 그대로 적용해야 함!!!
    parameter = ssm.get_parameter(Name='/MYAPP/LLMCORE/TAVILY', WithDecryption=True)
    # 여기에 env에 입력하는 API key를 넣으면 paramstore라는 AWS 서비스에서 적용되어 인식
    os.environ['TAVILY_API_KEY'] = parameter['Parameter']['Value']

def init_chatbot():
  __set_openai_api_key()

  if "messages" not in st.session_state:
    st.session_state.messages = []



