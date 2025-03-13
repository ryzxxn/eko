from datetime import datetime

def get_current_datetime():
    """
    Get the current date and time.

    Returns:
    - str : A string representing the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    # Get the current date and time
    now = datetime.now()

    # Format the date and time as a string
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    return current_datetime

# Example usage
if __name__ == "__main__":
    current_datetime = get_current_datetime()
    print("Current Date and Time:", current_datetime)
