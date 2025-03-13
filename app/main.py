import importlib.util
import os
from core.eko_core import load_tools, execute_function
from core.llm.groq_llm import llm_groq
from alive_progress import alive_bar #type: ignore
import time
import inspect


def main():
    available_tools = load_tools()
    # print("Loaded tools:", available_tools)

    # Allow user to input query
    query = input("Enter your query: ")

    # Simulate processing with a spinner
    with alive_bar(title="Processing query") as bar:
        bar()

    response = llm_groq(model="llama-3.3-70b-versatile", query=query, tools=available_tools)

    print("LLM Response:", response)

    # Extract the function name and parameters from the response
    function_name = response['function_name']
    parameters = response['function_args']

    # Execute the function with the provided parameters
    result = execute_function(available_tools, function_name, parameters)
    print(result)

if __name__ == "__main__":
    main()
