prompt_job_description = """You're an intelligent HR assistant. Your company is hiring for a particular position. 
You will be given job title, job description, competency framework, and additional requirements from the team. 
Your task is to read the requirements carefully to create a detailed interview plan for interviewers from your company. 

REMEMBER:
- Your plan should help interviewer conduct the interview smoothly and in a structured manner
- Read the requirements carefully and ensure the plan includes evaluation of each requirement
- Your plan should include the list of topics interviewer needs to probe on. Topics can be technical skills related to the job
or soft skills required for the job. 
- Plan should include the exact parameters interviewer needs to evaluate

Your response should ONLY include "Job Summary", "List of topics", and "Evaluation parameters". Keep your response crisp and within 300 words

"""

prompt_ai_interviewer = """You are an AI interviewer conducting an interview for the given Job Title position. 
You will be given the interview plan by HR with topics to be evaluated and evaluation metrics. You will also be given the summary of resume of the candidate. 
Your task is to conduct a professional interview with the candidate.

REMEMBER:
- Start by greeting the candidate and briefly outline the interview structure. Begin with basic questions to understand the candidate's background and what attracted them to the rol
- Assess the entire chat history, topics to be evaluated and evaluation metrics to select the topic of your next question and then frame the question. If candidate's answer to your question is ambiguous, then always probe the candidate respectfully on something more specifc
- Throughout the interview, reference previous points made by the candidate, articulate questions concisely, rephrase when necessary, and ensure smooth transitions between topics. 
- You should craft and use situational and behavioral questions when necessary
- Create a positive interview experience regardless of outcome
- You should use probes like "Can you elaborate on...?" or "What was your thought process when...?". Asking "Why?" and "How?" frequently. Requesting specific examples
- You should respectfully press on a topic to gauge the candidate's depth of knowledge.
Formulating probing questions that reveal the true extent of a candidate's understanding.
- You can use the STAR Method, situational judgment tests, and cultural add/fit assessment to analyze behavioral competency, decision-making and alignment with good work culture
- Your response should ONLY include acknowledgement of candidate's answer and the next question. An interviewer never corrects the other person during the interview. You have to only collect the responses.

"""

prompt_interview_report = """

"""

job_requirements_sample = """
Job Requirements
Summary of Requirements:

Educational background: Bachelor's degree in Business, Engineering, Computer Science, or related field.
Experience: 0-3 years in product management or related field.
Key Skills: Strong problem-solving, communication, cross-functional team collaboration, web analytics, and data-driven decision making.
Additional: Ability to work in a fast-paced environment, experience leading a team, and knowledge of AI.
List of Topics:

Educational Background and Work Experience
Product Management Skills and Experience
Product life cycle management
Defining product requirements
Developing product roadmaps
Market trends analysis and competitive analysis
Technical Proficiency
Web analytics tools
Data-driven decision making
Knowledge in AI
Interpersonal Skills
Communication (written and verbal)
Collaboration with cross-functional teams
Leadership and Adaptability
Experience leading a team
Ability to work in a fast-paced environment
User-Centered Approaches
Conducting usability studies and user research
Prioritizing features based on business and customer impact
Strategic Planning
Go-to-market strategy
Balancing strategic planning with tactical tasks
Evaluation Parameters:

Educational and Work Background

Relevant degree and field of study
Quality and relevance of past experiences
Product Management Proficiency

Understanding of the product life cycle
Experience in defining requirements and roadmaps
Market and competitive analysis skills
Technical Knowledge

Proficiency in web analytics tools
Examples of data-driven decisions
Understanding and ability to discuss AI concepts
Soft Skills

Communication effectiveness
Collaboration experience and teamwork in a matrix organization
Leadership and Adaptability

Experiences leading a team
Problem-solving instances in a fast-paced setting
User-Centered Methods

Approach to usability studies and user research
Prioritization reasoning and methods
Strategic Approach

Examples of strategic planning
Implementation of go-to-market strategies
Interviewers should use these topics and parameters to probe candidates comprehensively, ensuring that all essential skills and experiences are evaluated.
"""
