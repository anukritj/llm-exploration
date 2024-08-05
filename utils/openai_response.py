from openai import OpenAI
# from config import openai_api_key

# Response from OpenAI's GPT-4
def get_openai_response_chat(prompt,chat_history,job_requirements, resume, key):

    client = OpenAI(api_key=key)
    chat_history_str = ""
    for chat in chat_history:
        chat_history_str += chat['role'] + ":" + chat['content'] + "\n"

    user=f"Here is the chat history: {chat_history_str}\nInterview Prep Notes: {job_requirements}\nCandidate resume: {resume}"
    # print(f"CHAT HISTORY: {chat_history_str}")
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user}
    ]

    response = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages=messages)
    
    return response.choices[0].message.content

def get_openai_response_summary(prompt,user, key):

    client = OpenAI(api_key=key)
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user}
    ]

    response = client.chat.completions.create(
    model="gpt-4o-2024-05-13",
    messages=messages)
    
    return response.choices[0].message.content

