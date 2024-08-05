import streamlit as st
from openai import OpenAI
from config import openai_api_key
from prompts import prompt_job_description, prompt_prepare_questions
from utils.openai_response import get_openai_response_summary

with st.sidebar:
    system_prompt_summary = st.text_area("JD - System Prompt", value = prompt_job_description,key="jd_prompt")
    # system_prompt_questions = st.text_area("Questions - System Prompt", value = prompt_prepare_questions,key="question_prompt")
    # print(f"JD SYSTEM PROMPT: {system_prompt}")
   
st.title("📝 Interview Prep")
job_title = st.text_input("Job Title",value = "Product Manager", key="title")
jd_summary = ""

st.session_state.interview_questions = ""

job_description = st.text_area("Job Description",
value = """Job Title: Product Manager

Role Summary: We are seeking an enthusiastic Product Manager to join our team. This is an excellent opportunity for individuals at the early stage of their career to contribute to the full product life cycle and work on products that reach users worldwide.

Responsibilities:
- Manage the entire product line life cycle from strategic planning to tactical activities.
- Work closely with multiple teams to define product requirements.
- Develop product roadmaps to meet business targets.
- Analyze market trends and competition.
- Conduct usability studies and perform user research to understand user needs.
- Prioritize features and tasks for product development based on business and customer impact.
- Work with the sales and marketing teams to define the go-to-market strategy.

Requirements:
- Bachelor's degree in Business, Engineering, Computer Science, or related field.
- 0-3 years of experience in product management or a related field.
- Strong problem-solving skills and willingness to roll up one's sleeves to get the job.
- Excellent written and verbal communication skills.
- Skilled at working effectively with cross-functional teams in a matrix organization.
- Proficiency in web analytics tools and experience in data-driven decision making.""",
key="jd")

# competency_file = st.file_uploader("Upload a Competency framework (Optional)")

competency = st.text_area("Competency framework",key = "comp")

# option = st.selectbox(
#     "Type of interview",
#     ("Professional", "Behavioral", "Resume"))

extra_info = st.text_input(
    "Tell us more about your requirements",
    placeholder="eg.. should be able to work in a fast paced environment, should be able to lead a team",
)

# resume = st.text_area("Resume",key = "resume")

if job_description and extra_info and not openai_api_key:
    st.info("Please add your Open AI API key to continue.")

if st.button("Submit"):
    # if uploaded_file is not None:
    #     article = uploaded_file.read().decode()
    #     print(f"ARTICLE: {article}")

    # if competency_file is not None:
    #     competency = competency_file.read()
    #     print(f"COMPETENCY: {competency}")

    # client = anthropic.Client(api_key=anthropic_api_key)
    # response = client.completions.create(
    #     prompt=prompt,
    #     stop_sequences=[anthropic.HUMAN_PROMPT],
    #     model="claude-v1",  # "claude-2" for Claude 2 model
    #     max_tokens_to_sample=100,
    # )
    if competency:
        user_prompt = f"Job Title: {job_title}\nJob Description: {job_description}\n Some additional requirements by employer: {extra_info}"
    else:
        user_prompt = f"Job Title: {job_title}\nJob Description: {job_description}\n Here is a competency framework for your reference: {competency}\n Some additional requirements by employer: {extra_info}"

    # print(f"USER PROMPT: {user_prompt}")
    jd_summary = get_openai_response_summary(system_prompt_summary,user_prompt)
    st.write("### Job Requirements")
    st.write(jd_summary)

    # user_prompt_question = f"Job Title: {job_title}\nSkill Matrix expected for role: {jd_summary}\n Resume: {resume}"
    # st.write("### Prepararing Questions")
    # questions = get_openai_response_summary(system_prompt_questions,user_prompt_question)
    # st.write(questions)
    st.session_state.interview_questions = jd_summary

    # if st.button("Start Interview", type = "primary"):
    #     st.switch_page("AI_Interviewer.py")


