from openai import OpenAI
import streamlit as st
from config import openai_api_key
from prompts import prompt_ai_interviewer
from utils.openai_response import get_openai_response_chat
from prompts import job_requirements_sample, prompt_interview_report

with st.sidebar:
    # st.text_area("AI Interviewer - System Prompt", value = prompt_ai_interviewer,key="chatbot_system_prompt")
    # st.text_area("Resume",key="resume")
    # st.text_area("Job Requirements",value = job_requirements_sample, key="requirements")
    system_prompt = st.text_area("AI Interviewer - System Prompt", value = prompt_ai_interviewer,key="chatbot_system_prompt")
    resume = st.text_area("Resume",key="resume")
    requirements = st.text_area("Interview Prep",value = job_requirements_sample, key="requirements")
    # questions = st.text_input("Interview Questions", value = 10, key = "questions")


st.title("💬 AI Interviewer")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi! Let me know if we can start the interview"}]
    # msg = get_openai_response_chat(system_prompt,st.session_state.messages, requirements)
    # st.session_state.messages.append({"role": "assistant", "content": msg})
    # st.chat_message("assistant").write(msg)

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = get_openai_response_chat(system_prompt,st.session_state.messages, requirements, resume)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

if st.button("Generate Report"):
    user = "Chat History: "
    report = get_openai_response_chat(prompt_interview_report,st.session_state.messages, requirements, resume)
    st.session_state.messages.append({"role": "assistant", "content": report})
    st.chat_message("assistant").write(report)

