import openai # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

geminiLLM = openai.OpenAI(
    api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)