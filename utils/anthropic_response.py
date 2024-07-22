import anthropic
from config import claude_api_key


def get_anthropic_response_chat(system_prompt,chat_history,job_requirements, resume):
    client = anthropic.Client(api_key=claude_api_key)
    chat_history_str = ""
    for chat in chat_history:
        chat_history_str += chat['role'] + ":" + chat['content'] + "\n"

    user_prompt=f"Here is the chat history: {chat_history_str}\nInterview Prep Notes: {job_requirements}\nCandidate resume: {resume}"

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature = 0,
        system= system_prompt,
        messages=[
            {"role": "user", "content": user_prompt},
        ]
    )

    response.choices[0].message.content

def get_anthropic_response_summary(prompt,user):

    client = anthropic.Client(api_key=claude_api_key)
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user}
    ]

    response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=messages)
    
    return response.choices[0].message.content