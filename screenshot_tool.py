import pyautogui #type: ignore

def take_screenshot():
    filename="screenshot.png"
    # Take screenshot and save it to the file
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

# Example usage
take_screenshot("my_screenshot.png")
