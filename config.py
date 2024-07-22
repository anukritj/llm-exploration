import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ["openai_api_key"]
claude_api_key = os.environ["claude_api_key"]