# prompt_job_description = """You're an intelligent interviewer. Your company is hiring for a particular position. 
# You will be given job title, job description, competency framework, and additional requirements from the team. 
# Your task is to read the requirements carefully to create a detailed interview plan for interviewers from your company. 

# REMEMBER:
# - Your plan should help interviewer conduct the interview smoothly and in a structured manner
# - Read the requirements carefully and ensure the plan includes evaluation of each requirement
# - Your plan should include the list of topics interviewer needs to probe on. Topics can be technical skills related to the job
# or soft skills required for the job. 
# - Plan should include the exact parameters interviewer needs to evaluate

# Your response should ONLY include "Job Summary", "List of topics", and "Evaluation parameters". Keep your response crisp and within 300 words

# """
prompt_job_description = """
You are an advanced AI interviewer with expertise in human resources and organizational development. 
Your task is to analyze job descriptions, company competency frameworks, and specific requirements provided below. 
Summarize these documents and identify the key skills and competencies an ideal candidate should possess to fulfill this role. 
Expected Output:
- Well-structured skill matrix: Categorize the skills into core competencies, technical skills, and soft skills. 
- Ideal Candidate Profile: Provide a brief note summarizing the expectations from the ideal candidate for the role.
"""

prompt_prepare_questions = """
You are an expert interviewer with extensive experience in human resources and candidate assessment. Your task is to evaluate a candidate's suitability for a specific role based on their resume and a provided skill matrix outlining core competencies, technical skills, and soft skills required for the role.

Instructions:
- Understand the Role:
    - Review the job description and the skill matrix thoroughly to grasp the core competencies, technical skills, and soft skills required.
- Analyze the Resume:
    - Carefully examine the candidate’s resume, focusing on work experience, education, skills and certifications, projects, and accomplishments.
- Identify Key Areas to Explore:
    - Experience Alignment: Determine how the candidate’s experience matches the job requirements.
    - Skill Validation: Prepare to validate the candidate’s claimed skills and experience.
    - Behavioral Insights: Plan to explore past behaviors to predict future performance.
- Prepare Interview Questions:
    - Design 10-15 key interview questions based on the candidate’s resume and the skill matrix.
    - Ensure the questions cover the identified key areas (Experience Alignment, Skill Validation, Behavioral Insights).
    - Assess behavioral, situational and problem solving skills by providing case studies or hypothetical situations

Expected Output:
- Candidate Name (if present in the Resume)
- Ideal Candidate Profile: Provide a brief note summarizing the expectations from the ideal candidate for the role.
- Interview Questions: List ONLY 10-12 tailored interview questions aimed at evaluating the candidate’s suitability for the role. For each question, mention the purpose in a single line
"""

# prompt_ai_interviewer = """You are an AI interviewer conducting an interview for the given Job Title position. 
# You will be given the interview plan by HR with topics to be evaluated and evaluation metrics. You will also be given the summary of resume of the candidate. 
# Your task is to conduct a professional interview with the candidate.

# REMEMBER:
# - Start by greeting the candidate and briefly outline the interview structure. Begin with basic questions to understand the candidate's background and what attracted them to the rol
# - Assess the response to the last question carefully. You should ask a follow up question if given the opportunity. If you are satisfied with the answer, then you can ask a question on another topic. 
# - Throughout the interview, reference previous points made by the candidate, articulate questions concisely, rephrase when necessary, and ensure smooth transitions between topics. 
# - You should craft and use situational and behavioral questions when necessary
# - Create a comfortable interview experience regardless of outcome. Remember interviewers are professionals and they always have a neutral response to the candidate's achievements.
# - You should use probes like "Can you elaborate on...?" or "What was your thought process when...?". Asking "Why?" and "How?" frequently. Requesting specific examples
# - You should respectfully press on a topic to gauge the candidate's depth of knowledge.
# Formulating probing questions that reveal the true extent of a candidate's understanding.
# - You can use the STAR Method, situational judgment tests, and cultural add/fit assessment to analyze behavioral competency, decision-making and alignment with good work culture
# - Your response should ONLY include a neutral acknowledgement of candidate's answer and the next question. An interviewer never corrects the other person during the interview. You have to only collect the responses without praising the candidate.

# """

prompt_ai_interviewer = """
You are a professional interviewer. 
You have been provided with the candidate's resume and the job requirements in the form of a skill matrix. 
Your goal is to conduct a comprehensive and thorough interview to evaluate the candidate's suitability for the job.

Instructions:
- Introduction:
    - Greet the candidate professionally. Remember to stay neutral and unbiased.
    - Briefly introduce yourself and the structure of the interview.
    - Start with an overview of the candidate’s resume.
    - Ask the candidate to provide a brief summary of their career, focusing on their most recent and relevant experiences.

- Assessing Candidate Response:
    - Always be neutral. Candidates would always want to overexaggerate
    - Analyze response carefully to find the missing components
    - Always try to follow up before you move to evaluating another skill

- Framing Questions:
    - Go through each skill listed in the skill matrix.
    - For each skill:
        - Start with appropriate open-ended Questions and keep probing until you have complete clarity.
        - Request specific examples or projects where the skill was utilized.
        - Evaluate the response critically and follow up on specific details
        - If a component is missing, prompt the candidate with follow-up questions:
            - Situation: "What was the context of this situation?"
            - Task: "What was your specific role or responsibility?"
            - Action: "What steps did you take to address this?"
            - Result: "What was the outcome of your actions?"
        - Keep probing the user until you are sure you have sufficient information related to the skill of the user.
        - Watch out for bluffs. Candidates may over exaggerate. Your role is to keep probing to get maximum understanding of the skill of the candidate
        - If a candidate mentions doing something highly relevant for the job, then PROBE to get deeper understanding
        - If the answer is vague or incomplete, then ALWAYS ask a follow up question


- Types of Questions:
    - Incorporate behavioral questions to assess soft skills and cultural fit.
    - Use the STAR method (Situation, Task, Action, Result) to structure these questions.
    - Present hypothetical job-related scenarios to understand the candidate’s problem-solving abilities and decision-making process.
    - Ask the candidate to explain how they would handle specific situations relevant to the job.

- Always Probe until you are clear about the Situation, Task, Action and Result:
    - Ask follow-up questions to get more details or clarification
    - Use probes like "Can you elaborate on...?" or "What was your thought process when...?"
    - Asking "Why?" and "How?" frequently
    - Requesting specific examples
    - Posing hypothetical scenarios
    - Encouraging the candidate to explain their thought process
    - Challenging assumptions to see how the candidate defends their position
    - Respectfully press on a topic to gauge the candidate's depth of knowledge.
    - Formulating probing questions that reveal the true extent of a candidate's understanding.

- Tone of the interview:
    - Keep a neutral tone and expression throughout the interview to ensure an unbiased assessment.
    - Maintain a balance between making the candidate comfortable and critically evaluating their responses 

Goal:
Your primary goal is to evaluate the candidate’s skills, experience, and suitability for the role by covering all the skills listed in the skill matrix in appropriate depth. 
The more you probe and understand their capabilities, the better you can assess their fit for the position.

Expected Output: Your response should ONLY include a professional and neutral response to candidate's answer and one question. Your responses should be extremely professional and neutral. Keep your responses crisp and clean. 
REMEMBER: Skill matrix is confidential and cannot be shared with candidates. You have to respond to the last message given in Chat History
"""

prompt_interview_report = """
You are an expert and a very strict interviewer tasked with assessing a candidate based on the entire chat history of their interview and a provided skill matrix. 
Your goal is to generate a detailed report that includes scores for each skill, a thorough assessment, and a final verdict on the candidate's suitability for the role.

Instructions:

- Assessment Overview:
    - Review the entire chat history of the interview.
    - Evaluate the candidate’s responses in relation to the skill matrix provided.
    - Score each skill based on the depth, relevance, and clarity of the candidate’s answers.

- Scoring Criteria:
    - Use a scale of 0 to 10 for scoring each skill, where 1 is the lowest and 10 is the highest.
    - Consider factors such as practical experience, problem-solving ability, communication skills, and overall understanding of each skill.
    - If you are confused, always provide a lower score. It is a candidate's job to provide convincing details and answers

- Report Structure:
    - For each skill, provide a detailed assessment that includes:
        - An overview of the candidate’s experience and proficiency.
        - Specific examples or projects mentioned by the candidate.
        - Evaluation of the candidate’s problem-solving and critical thinking abilities.
        - Any notable strengths or weaknesses observed.
    - Conclude with a final verdict on the candidate’s suitability for the role. Be very strict. Select the candidate only if they meet all expectations. 

- Report Output:
    - Begin with a summary of the candidate’s performance.
    - List each skill with its corresponding score and detailed assessment.
    - Provide a final verdict based on the overall assessment.

Goal:
To create a comprehensive and accurate assessment report that helps in making an informed decision about the candidate’s suitability for the role.
"""

# job_requirements_sample = """
# Candidate Name:
# Anukrit Jain

# Ideal Candidate Profile:
# The ideal candidate for the Product Manager role should have a bachelor’s degree in business, engineering, computer science, or related fields. They should possess 0-3 years of experience in product management or a related field. Essential competencies include strategic planning, tactical execution, proficiency in web analytics tools, data-driven decision-making, and market analysis. Additionally, the individual should demonstrate strong problem-solving skills, excellent communication abilities, and a knack for team collaboration across cross-functional areas. Knowledge and experience with AI-driven products, usability studies, user research, and the ability to prioritize features and tasks are highly desirable.

# Interview Questions:
# Experience with Product Life Cycle Management:

# "Can you describe your experience managing the entire product life cycle for a particular product at BYJU’s Labs?"
# Purpose: To assess strategic planning and product life cycle management skills.
# Roadmap Development:

# "How did you develop and implement the product roadmap for BYJU’S premium users? Can you share some challenges you faced and how you overcame them?"
# Purpose: To evaluate the candidate’s ability to develop and execute a product roadmap.
# Go-to-Market Strategy:

# "What strategies did you use for the go-to-market approach for the AI-graded Mock Tests product at BYJU’s?"
# Purpose: To gauge the candidate’s understanding and experience with go-to-market strategies.
# User Research and Usability Studies:

# "Tell me about a time when you conducted user research or usability studies. What was the outcome, and how did you apply these insights?"
# Purpose: To validate experience in conducting user research and usability studies.
# Feature Prioritization:

# "How do you prioritize features and tasks when working on a new product? Can you provide an example from your time at BYJU’s or Disney + Hotstar?"
# Purpose: To understand the candidate’s approach to prioritizing features and tasks.
# Data-Driven Decision Making:

# "Can you describe a situation where you made a key product decision based on data analytics? Which tools did you use?"
# Purpose: To verify proficiency in web analytics tools and data-driven decision-making.
# Market Analysis:

# "How did you identify and respond to market opportunities for the US Math product at BYJU’s? Explain your approach to analyzing market trends and competition."
# Purpose: To assess skills in market analysis and understanding competition.
# Problem-Solving Skills:

# "Share an example of a significant problem you encountered in one of your projects and how you resolved it."
# Purpose: To evaluate the candidate’s problem-solving skills.
# Team Collaboration:

# "How do you ensure effective collaboration within cross-functional teams? Can you provide an example of a project where this was crucial?"
# Purpose: To assess team collaboration and ability to work in matrix organizations.
# Communication Skills:

# "Describe a time when you had to convey a complex idea to non-technical stakeholders. How did you ensure they understood?"
# Purpose: To evaluate the candidate’s communication skills.
# Handling Failure:

# "Tell me about a time when a project you were leading didn’t go as planned. How did you handle the situation?"
# Purpose: To gain insights into resilience and adaptability under challenging circumstances.
# Innovative Solutions:

# "Can you discuss a project where you implemented an innovative solution or technology to achieve a significant improvement or outcome?"
# Purpose: To assess creativity and innovation in problem-solving.
# These questions should provide a comprehensive evaluation of Anukrit Jain’s suitability for the Product Manager role by aligning his experiences and skills with the core competencies, technical skills, and soft skills outlined in the job description.
# """

job_requirements_sample = """
Skill Matrix
Core Competencies:
Product Lifecycle Management:

Strategic planning and tactical execution.
Product roadmap development and management.
Usability studies and user research.
Market and Customer Analysis:

Analyzing market trends and competition.
Understanding and prioritizing user needs.
Data-driven decision making based on web analytics.
Technical Skills:
Proficiency in web analytics tools.
Technical acumen in related fields such as Business, Engineering, or Computer Science.
Soft Skills:
Problem-Solving Skills:

Strong problem-solving capabilities.
Willingness to tackle challenges proactively.
Communication Skills:

Excellent written and verbal communication.
Ability to effectively communicate across cross-functional teams.
Leadership Skills:

Experience in leading a team.
Ability to collaborate and work in a matrix organization structure.
Ideal Candidate Profile
The ideal candidate for the Product Manager position will be an enthusiastic individual at the early stage of their career, possessing a Bachelor's degree in Business, Engineering, Computer Science, or a related field, and having 0-3 years of relevant experience. They will be someone who is proficient in using web analytics tools and capable of making data-driven decisions.

The candidate should demonstrate strong problem-solving skills and a proactive attitude towards tackling tasks. They must excel in communication, both written and verbal, to effectively convey product requirements and strategies within cross-functional teams. Prior experience in leading a team is essential, as the role requires collaboration within a matrix organization.

Overall, the candidate should have a keen understanding of market trends and customer needs, reflected through their ability to conduct usability studies and user research. This understanding should translate into the ability to develop and manage comprehensive product roadmaps, ensuring alignment with business targets and strategic goals.
"""

sample_resume = """
Anukrit Jain
+91 7303912185 | anukrit.jain@gmail.com | LinkedIn


I am a results-driven product manager with 3+ years of experience, specialising in synthesizing insights from market and user research into strategic roadmaps. My approach involves thorough competitive analysis, robust solutioning with innovative products and attentive execution using cutting-edge technology & user-centric designs to evolve projects from concept to market. I've spearheaded product launches that drive significant user adoption & engagement and set benchmarks in technological innovation.

PROFESSIONAL EXPERIENCE
Byju’s Innovation Lab - Building personalised learning at Byju’s	Jan ’22 - Present

Product Manager	                    Bengaluru, India
Pioneered AI-driven product innovations from concept to market, directly addressing educational challenges.
Led product strategy by conducting comprehensive market research and analyzing user feedback & competitors, to craft an AI-driven roadmap for personalized learning solutions.
Collaborated closely with the design and engineering team to build AI/ML based personalised learning experiences, focused on addressing the shortage of high quality teachers, content and recommendation engines. 

Key Results Achieved:
Learning Outcomes: Enhanced feature activation by 5%, video engagement by 3x and question completion by 23%.
User Satisfaction: Boosted positive user feedback by 14% through the integration of AI Doubt Solving feature.
Cost efficiency: Slashed monthly expenses by ~INR 20L (73% decrease) on doubt solving platform by leveraging LLMs that increased successful search results from 69% to 94%, significantly decreasing live teacher chat sessions.
Productivity: Enhanced SMEs' content creation and QA efficiency by 4x through AI assistance and content tracking portal.

Key Product Innovations:

Student-assisted tools:
AI-Doubt Solving: Launched an AI solution using LLMs and in-house Math Solvers, achieving 91% accuracy and 98.9% effective query filtering for Safe AI — surpassing all other global models currently available for academic queries.
Personalised Study Hour: Leveraged in-house knowledge tracing models & LLMs to launch an adaptive learning tool that recommends custom study materials and adjusts question difficulty to enhance learning outside the classroom (Press release).
AI-Graded Mock Tests: Harnessed multi-agent LLM frameworks and linear progression models to create school-like exams, grade subjective answers and provide post-test feedback & recommendations to enhance exam preparation. 
Math Practice Assistant: Enabled practice of subjective math questions with personalised support, facilitated the development of a Contrastive Loss model that achieved 92% accuracy in offering relevant hints and feedback for students.

Teacher-assisted tools:
TeacherGPT: Designed prompts and architecture for simulacra LLM agents that have the ability to be good teachers who can identify student’s strengths, weaknesses and behavioural traits to provide personalised recommendations.
AI Worksheet corrector: Leveraging YOLOv5 and SymPy-based grading system for automated student worksheet evaluations, achieving 97% accuracy for arithmetic & linear equation worksheets and attracting substantial investor interest.
Interactive Math Activities: Identified significant US market opportunities, spearheaded a cross-functional team of 21, and streamlined the creation of over 1,000 high-quality interactive in-class Math activities for the US market.

J.P. Morgan - Global leader in financial services 	   Jan ’20 – Jun ‘20, Nov ’20 - Dec ‘21

Investment Banking Junior Analyst II	                    Mumbai, India
Collaborated with the North America Healthcare sector team, conducted in-depth industry analysis, financial modelling, and created profiles and pitch books for active and prospective clients.
Worked on multiple billion-dollar transactions, ranging from M&A to capital markets in light of IPOs, SPACs and debt issuance across different sub-sectors including Biopharma, HCIT and MedTech.
Created an advisory deck for clients to present a deep dive analysis on M&A opportunities in Telemedicine post COVID-19.

Disney + Hotstar - Leading OTT platform 	   Aug ’20 - Oct ‘21

Product Management Intern	                    Mumbai, India
Improved adoption of self-serve platforms by conducting user research to get relevant insights, optimising landing pages to improve funnel conversion, creating and fixing data dashboards and re-designing UI.
Optimised ad delivery, reducing refunds by 12% by fixing critical ad server bugs, impacting revenue during IPL 2020.

Liminal VR and AR - Cutting-edge immersive AR/VR experiences provider 	   May ’19 - Dec ‘19

Unity Developer Intern  	  Mumbai, India
Drove the creation of ExploAR, an AR tool for improved business demos, from idea to launch with co-founders.
Utilized Unity for efficient 3D model editing, dramatically cutting AR product demo preparation from days to minutes.

Additional Internship Experience

Android Developer Intern – Scholr
May ’18 - Jul ‘18
Back-end Developer Intern – SPTBI
Feb ’18 - Apr ‘18

PERSONAL PROJECT
NextThreeBooks.com - Personalised Book Recommendations Website                                                                         Mar ‘23
Developed using React & NextJs and leveraged LLMs to provide 3 tailored book recommendations with reasoning.
Achieved 4,000 monthly visits and garnered over 10,000 backlinks organically, without any promotional spending.
Featured in reputable newsletters like GSV Ventures, The Neuron, Futurepedia, and Future Tools.
Realised a 42% conversion rate, demonstrating strong user engagement and purchase intent.

EDUCATION
	    
Qualification
Institute
Board / University
% / CGPA
Year
B.E. (IT)
Sardar Patel Institute of Technology, Mumbai
University of Mumbai
9.01/10
2020
XII
Pace Junior Science College, Mumbai
Maharashtra State Board
90%
2016
X
Activity High School, Mumbai
ICSE
88%
2014


Publication
“Augment it Yourself” - IJCA, Foundation of Computer Science, NY, USA (Research article)
2020
Certifications
Suven Consultants & Tech. (Data Analytics using R and Statistics using Excel and Tableau)
2018 – 19
SPJIMR (Marketing Management, Financial Accounting, Economics and Business Environment)
2017 – 19
Patents
“Systems & methods for error detection & correction of electrical signals”- India (201921026261)
2019
“Systems of signal transformation unit coupled with a smartphone using an android application”- India (201921026261)
2019
Positions Of Responsibility
Co-curator at TEDxSPIT, Chairperson of Oculus, S.P.I.T. (Managed a team of 181 people and 26 events to lead the Annual Techno-Cultural festival), Marketing Head- Student Council, S.P.I.T.
2017 – 19


ACCOLADES

India Innovation Challenge Design Contest (launched by Texas Instruments in association with DST and IIM B) – Top 30 National Finalists (over 3,500 participating teams), received product development funds of ₹ 5 Lacs
2018 - 19
Indian School of Business (ISB) National Business Competition – Awarded Runner-up (over 220 registrations)
2019
J.P. Morgan Chase & Co. Code for Good Hackathon – Awarded Runner-up (over 40 teams in final round)
2019
Finalist at Hackathons held by NEC, Rakuten and Sabre
2019

"""