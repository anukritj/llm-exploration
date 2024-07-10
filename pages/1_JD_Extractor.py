import streamlit as st
from openai import OpenAI
from config import openai_api_key
from prompts import prompt_job_description
from utils.openai_response import get_openai_response_summary

with st.sidebar:
    system_prompt = st.text_area("JD - System Prompt", value = prompt_job_description,key="jd_summarizer")
    # print(f"JD SYSTEM PROMPT: {system_prompt}")
   
st.title("📝 Job Description Extractor")
uploaded_file = st.file_uploader("Upload a Job Description doc")
competency_file = st.file_uploader("Upload a Competency framework")
extra_info = st.text_input(
    "Tell us more about your requirements",
    placeholder="eg.. should be able to work in a fast paced environment",
    disabled=not uploaded_file,
)

if uploaded_file and extra_info and not openai_api_key:
    st.info("Please add your Open AI API key to continue.")

if st.button("Submit"):
    if uploaded_file is not None:
        article = uploaded_file.read().decode()
        print(f"ARTICLE: {article}")

    if competency_file is not None:
        competency = competency_file.read()
        print(f"COMPETENCY: {competency}")

    # client = anthropic.Client(api_key=anthropic_api_key)
    # response = client.completions.create(
    #     prompt=prompt,
    #     stop_sequences=[anthropic.HUMAN_PROMPT],
    #     model="claude-v1",  # "claude-2" for Claude 2 model
    #     max_tokens_to_sample=100,
    # )
    if competency_file is None:
        user_prompt = f"Here is the JD: {article}\n Some additional requirements by employer: {extra_info}"
    else:
        user_prompt = f"Here is the JD: {article}\n Here is the competency framework: {competency}\n Some additional requirements by employer: {extra_info}"

    msg = get_openai_response_summary(system_prompt,user_prompt)
    st.write("### Answer")
    st.write(msg)
