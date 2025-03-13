import os
import subprocess

def start_calculator(calculation: str = None):
    """
    Start the calculator app and optionally perform a calculation.

    Parameters:
    - calculation: str : A mathematical expression to evaluate.
    """
    # Detect the operating system
    current_os = os.name

    try:
        if calculation:
            # Evaluate the calculation using Python
            result = eval(calculation)
            print(f"Calculation Result: {result}")

        # Start the calculator app based on the operating system
        if current_os == 'nt':  # Windows
            subprocess.run(['calc.exe'])
        elif current_os == 'posix':  # Unix-based systems (Linux, macOS)
            if os.path.exists('/usr/bin/gnome-calculator'):
                subprocess.run(['gnome-calculator'])
            else:
                print("GNOME Calculator is not installed. Please install it using 'sudo apt-get install gnome-calculator'.")
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error starting calculator or performing calculation: {e}")