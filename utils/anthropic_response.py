import anthropic
from config import claude_api_key


def get_anthropic_response_chat(system_prompt,chat_history,job_requirements, resume, key):
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
    print("CLAUDE 3.5 SONNET")
    print(f"SYSTEM PROMPT: {system_prompt}")

    return response.content[0].text

def get_anthropic_response_summary(prompt,user, key):

    client = anthropic.Client(api_key=claude_api_key)
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user}
    ]

    response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=messages)
    print("CLAUDE 3.5 SONNET")
    
    return response.content[0].text