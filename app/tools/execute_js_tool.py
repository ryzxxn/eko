import subprocess

def execute_js_(file_path:str):
    """
    Execute a JavaScript file using Node.js.

    Parameters:
    - file_path: str : The path to the JavaScript file to execute.

    Returns:
    - str : The output of the JavaScript file execution.
    """
    try:
        # Run the JavaScript file using Node.js
        result = subprocess.run(['node', file_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the JavaScript file: {e}")
        print(f"Error output: {e.stderr}")
        return None
    except FileNotFoundError:
        print("Node.js is not installed or not found in the system PATH.")
        return None
