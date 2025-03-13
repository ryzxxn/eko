import json
from groq import Groq #type:ignore
import os
from dotenv import load_dotenv  #type:ignore
import instructor #type:ignore
import requests #type:ignore
from pydantic import BaseModel #type:ignore

load_dotenv()

class FunctionResponse(BaseModel):
    function_name: str
    function_args: dict[str, str | int | float]  # Use a dictionary for named arguments

def llm_groq(model: str, query: str, tools: list):
    """
    Get a structured response from the Groq LLM.

    Parameters:
    - model: str : The language model to use for generating the completion.
    - query: str : The user's query to respond to.
    - available_functions: dict : A dictionary of available functions.

    Returns:
    - dict : A structured JSON response with the function to execute and parameters.
    """
    client = instructor.from_groq(Groq(api_key=os.getenv("GROQ_API_KEY")), mode=instructor.Mode.JSON)

    # Include available functions in the system message
    functions_description = "\n".join([f"{name}: {func.__doc__}" for name, func in tools.items()])
    system_message = f"You are a helpful assistant. You have access to the following functions:\n{functions_description}"

    chat_completion: FunctionResponse = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model=model,
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
        response_model=FunctionResponse,
    )

    # Return a structured response
    response_content = {
        "function_name": chat_completion.function_name,
        "function_args": chat_completion.function_args
    }
    return response_content

# Example function definition
def send_to_discord(message: str, webhook_url: str):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'content': message
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    return response
