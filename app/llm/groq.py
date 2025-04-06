import os
import openai # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

groqLLM = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)