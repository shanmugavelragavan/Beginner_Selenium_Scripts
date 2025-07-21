# Take Screenshot of a Webpage 

from selenium import webdriver
import time
from datetime import datetime

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    # Open the registration page
    driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
    driver.maximize_window()

    # Wait for the page to load
    time.sleep(3)

    # Create a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_filename = f"screenshot_{timestamp}.png"

    # Take a screenshot and save it
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 