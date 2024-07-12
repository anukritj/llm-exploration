from openai import OpenAI
import streamlit as st
from config import openai_api_key
from prompts import prompt_ai_interviewer
from utils.openai_response import get_openai_response_chat
from prompts import job_requirements_sample

with st.sidebar:
    # st.text_area("AI Interviewer - System Prompt", value = prompt_ai_interviewer,key="chatbot_system_prompt")
    # st.text_area("Resume",key="resume")
    # st.text_area("Job Requirements",value = job_requirements_sample, key="requirements")
    system_prompt = st.text_area("AI Interviewer - System Prompt", value = prompt_ai_interviewer,key="chatbot_system_prompt")
    resume = st.text_area("Resume",key="resume")
    requirements = st.text_area("Job Requirements",value = job_requirements_sample, key="requirements")
    questions = st.text_input("Interview Questions", value = 10, key = "questions")


st.title("💬 AI Interviewer")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = get_openai_response_chat(system_prompt,st.session_state.messages, resume, requirements, questions)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
