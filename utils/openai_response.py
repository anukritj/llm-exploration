from openai import OpenAI
from config import openai_api_key

# Define a function to get the response from OpenAI's GPT-3
def get_openai_response_chat(prompt,chat_history):

    client = OpenAI(api_key=openai_api_key)
    chat_history_str = ""
    for chat in chat_history:
        chat_history_str += chat['role'] + ":" + chat['content'] + "\n"

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": chat_history_str}
    ]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=messages)
    
    return response.choices[0].message.content

def get_openai_response_summary(prompt,user):

    client = OpenAI(api_key=openai_api_key)
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user}
    ]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=messages)
    
    return response.choices[0].message.content

