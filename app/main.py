import importlib.util
import os
from core.eko_core import load_tools
from core.llm import llm_groq
from alive_progress import alive_bar #type: ignore
import time
import inspect

def execute_function(tools, function_name, parameters):
    if function_name in tools:
        function_info = tools[function_name]
        function = function_info['function']
        sig = function_info['signature']

        # Map provided arguments to parameter names using the function's signature
        bound_args = sig.bind_partial(*parameters)
        bound_args.apply_defaults()

        return function(*bound_args.args, **bound_args.kwargs)
    else:
        raise ValueError(f"Function {function_name} not found in available tools.")

def main():
    available_tools = load_tools()
    print("Loaded tools:", available_tools)

    # Allow user to input query
    query = input("Enter your query: ")

    # Simulate processing with a spinner
    with alive_bar(title="Processing query") as bar:
        bar()

    response = llm_groq(model="llama-3.3-70b-versatile", query=query, available_functions=available_tools)

    print("LLM Response:", response)

    # Extract the function name and parameters from the response
    function_name = response['function_name']
    parameters = response['function_args']

    # Execute the function with the provided parameters
    result = execute_function(available_tools, function_name, parameters)
    print("Function Execution Result:", result)

if __name__ == "__main__":
    main()
