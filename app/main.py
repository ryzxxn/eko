from core.utils import load_tools, list_tools, execute_function
from core.llm.groq import invoke
from groq import Groq  # type:ignore
import os
from dotenv import load_dotenv  # type:ignore

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

loaded_tools = load_tools()

query = "search wikipedia about donald trump"

instruction = (
    f"You are an agent. You have access to the following functions and parameters associated with the functions. "
    f"Use this information to return a response with the correct keys for those functions."
)

response = invoke(llm=groq_client, query=query, tools=loaded_tools, instruction_prompt=instruction, model="llama-3.3-70b-specdec")

print("LLM Response:", response)

# List tools for reference
list_tools(loaded_tools)

# Execute the function based on the response
try:
    function_response = {'function_name': 'scrape_wikipedia', 'function_args': {'topic': 'GTA 6'}}
    result = execute_function(loaded_tools, function_response['function_name'], function_response['function_args'])
    print("Function Execution Result:", result)
except Exception as e:
    print("Error:", e)
