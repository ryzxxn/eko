import subprocess
import os

def execute_code(file_path: str):
    """
    Execute a JavaScript or Python file based on the file extension.

    Parameters:
    - file_path: str : The path to the file to execute.

    Returns:
    - str : The output of the file execution.
    """
    try:
        # Determine the file extension
        _, file_extension = os.path.splitext(file_path)

        # Choose the appropriate interpreter based on the file extension
        if file_extension == '.js':
            interpreter = 'node'
        elif file_extension == '.py':
            interpreter = 'python'
        else:
            print("Unsupported file extension. Only .js and .py files are supported.")
            return None

        # Run the file using the appropriate interpreter
        result = subprocess.run([interpreter, file_path], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the file: {e}")
        print(f"Error output: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"{interpreter} is not installed or not found in the system PATH.")
        return None