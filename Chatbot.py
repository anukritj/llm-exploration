from openai import OpenAI
import streamlit as st
from config import openai_api_key
from prompts import prompt_ai_interviewer
from utils.openai_response import get_openai_response

with st.sidebar:
    system_prompt = st.text_area("AI Interviewer - System Prompt", value = prompt_ai_interviewer,key="chatbot_system_prompt")

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    
    # messages = [
    #     {"role": "system", "content": system_prompt},
    #     {"role": "user", "content": st.session_state.messages}
    # ]

    # client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    msg = get_openai_response(system_prompt,st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
