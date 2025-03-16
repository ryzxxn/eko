import os
import importlib.util
import inspect
import json

def load_tools():
    folder_path = "app/tool"
    tools = []

    # Iterate over each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('_tool.py'):
            module_name = filename[:-3]  # Remove the '_tool.py' extension
            module_path = os.path.join(folder_path, filename)

            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Iterate over each attribute in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr):
                    # Get the signature of the function
                    sig = inspect.signature(attr)
                    parameters = []

                    # Extract parameter names and types
                    for param in sig.parameters.values():
                        param_info = {
                            "name": param.name,
                            "type": str(param.annotation) if param.annotation != inspect.Parameter.empty else "Unknown",
                            "default": param.default if param.default != inspect.Parameter.empty else None
                        }
                        parameters.append(param_info)

                    # Store the function and its parameters in the list
                    tools.append({
                        'name': attr_name,
                        'function': attr,
                        'parameters': parameters
                    })

    # Convert the list of tools to a dictionary for easier access
    tools_dict = {tool['name']: tool for tool in tools}
    return tools_dict

def list_tools(tools):
    """
    Print the details of each tool, including its name and parameters.

    Parameters:
    - tools: dict : A dictionary of available tools with their signatures.
    """
    for tool in tools.values():
        print(f'- {tool["name"]} -')
        print("Parameters:")

        # Iterate over each parameter of the tool
        for param in tool["parameters"]:
            # Extract parameter details
            name = param["name"]
            param_type = param["type"]
            default = param["default"]

            # Print parameter details
            print(f"  - {name}: {param_type}")
            if default is not None:
                print(f"    Default: {default}")

def execute_function(tools, function_name, parameters=None):
    """
    Execute a function with the given parameters.

    Parameters:
    - tools: dict : A dictionary of available functions with their signatures.
    - function_name: str : The name of the function to execute.
    - parameters: dict : The parameters to pass to the function. Defaults to None.

    Returns:
    - The result of the function execution.
    """
    if function_name in tools:
        function_info = tools[function_name]
        function = function_info['function']
        sig = inspect.signature(function)

        if parameters is None:
            parameters = {}

        # Bind the provided parameters to the function's signature
        bound_args = sig.bind_partial(**parameters)
        bound_args.apply_defaults()

        return function(*bound_args.args, **bound_args.kwargs)
    else:
        raise ValueError(f"Function {function_name} not found in available tools.")
