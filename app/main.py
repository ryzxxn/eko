import importlib.util
import os
from core.eko_core import load_tools, execute_function
from core.llm.groq_llm import llm_groq
from alive_progress import alive_bar  # type: ignore
import time
import inspect

def main():
    available_tools = load_tools()
    # print("Loaded tools:", available_tools)

    while True:
        # Allow user to input query
        query = input("Enter your query (or type 'exit' to quit): ")

        if query.lower() == 'exit':
            print("Exiting...")
            break  # Exit the loop if the user types 'exit'

        # Simulate processing with a spinner
        with alive_bar(title="Processing query") as bar:
            bar()

        response = llm_groq(model="llama-3.3-70b-versatile", query=query, tools=available_tools)

        print("LLM Response:", response)
        print("Response Type:", type(response))

        # Check if response is a dictionary and contains required keys
        if isinstance(response, dict) and 'function_name' in response and 'function_args' in response:
            function_name = response['function_name']
            parameters = response['function_args']

            # Execute the function with the provided parameters
            result = execute_function(available_tools, function_name, parameters)
            print("Function Result:", result)
        else:
            print("Error: Invalid response structure")

if __name__ == "__main__":
    main()