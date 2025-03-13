from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Optional
from pydantic import BaseModel

# Pydantic model for credentials
class Credentials(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None

# Corrected function signature with proper argument types
def open_chrome_agent(*, url: str, credentials: Optional[Credentials]=None, action: Optional[str] = None):
    # Set up Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # Optional: Maximize the window

    # Path to your chromedriver (you may need to download it and provide the correct path)
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to Amazon
        driver.get(url)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))

        # Now you can read the page content every time it loads
        page_source = driver.page_source  # Get the entire HTML of the page
        print("Page source after loading:")
        print(page_source)  # You can also perform regex or string matching to check specific data in the page.

        # If you want to check specific data like the title or text
        page_title = driver.title
        print(f"Page Title: {page_title}")

        # For example, wait until the "Sign in" button is present and print out its text
        sign_in_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nav-link-accountList"))
        )
        print(f"Sign in button text: {sign_in_button.text}")

        # Now perform the sign-in action
        sign_in_button.click()

        # Wait for the sign-in page to load and extract data again
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@data-nav-ref='nav_signin']")))
        print("Sign-in page loaded.")

        # More reading logic can be added here for every page load

        # Example action: Find the "Create Account" button and click it
        create_account_link = driver.find_element(By.XPATH, "//a[@data-nav-ref='nav_signin']")
        create_account_link.click()

        # Wait for the signup page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))

        # Once the page loads, extract the content again
        page_source = driver.page_source  # Get the entire HTML again
        print("Page source after clicking 'Create Account':")
        print(page_source)

    except Exception as e:
        print(f"An error occurred: {e}")

