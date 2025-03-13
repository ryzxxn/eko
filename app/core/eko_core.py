import importlib.util
import os
import inspect

def load_tools():
    folder_path = "app/tools"
    tools = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('_tool.py'):
            module_name = filename[:-3]  # Remove the '.py' extension
            module_path = os.path.join(folder_path, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr):
                    # Get the signature of the function
                    sig = inspect.signature(attr)
                    # Store the function and its signature
                    tools[attr_name] = {'function': attr, 'signature': sig}
    return tools

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
        sig = function_info['signature']

        if parameters is None:
            parameters = {}

        # Bind the provided parameters to the function's signature
        bound_args = sig.bind_partial(**parameters)
        bound_args.apply_defaults()

        return function(*bound_args.args, **bound_args.kwargs)
    else:
        raise ValueError(f"Function {function_name} not found in available tools.")