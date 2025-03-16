import json
from groq import Groq  # type:ignore
import os
from dotenv import load_dotenv  # type:ignore
import instructor  # type:ignore
from pydantic import BaseModel  # type:ignore
import inspect

load_dotenv()

class Credentials(BaseModel):
    email: str
    password: str
    phonenumber: str

class FunctionResponse(BaseModel):
    function_name: str
    function_args: dict[str, str | int | float | Credentials]  # Use a dictionary for named arguments

def invoke(llm, model: str, instruction_prompt: str, query: str, tools: dict):
    """
    Get a structured response from the Groq LLM.

    Parameters:
    - llm_client: The LLM client instance to use for generating the completion.
    - model: str : The language model to use for generating the completion.
    - instruction_prompt: str : The instruction prompt to guide the LLM's response.
    - query: str : The user's query to respond to.
    - tools: dict : A dictionary of available functions.

    Returns:
    - dict : A structured JSON response with the function to execute and parameters.
    """
    client = instructor.from_groq(llm, mode=instructor.Mode.JSON)

    # Include available functions in the system message
    system_message = (
        f"You are an agent. You have access to the following functions and parameters associated with the functions. "
        f"Use this information to return a response with the correct keys for those functions:\n{tools}\n\n"
        f"Instruction: {instruction_prompt}"
    )

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
        max_completion_tokens=200,
        top_p=1,
        stop=None,
        stream=False,
        response_model=FunctionResponse,
    )

    # Ensure that the response is in dictionary format
    response_content = {
        "function_name": chat_completion.function_name,
        "function_args": chat_completion.function_args
    }

    print(response_content)
    return response_content
