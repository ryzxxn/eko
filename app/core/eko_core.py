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