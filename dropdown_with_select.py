# Handle Dropdown Using Select Class 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    # Open the registration page
    driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Wait for the month dropdown to be present
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[contains(@name,'DOB_Month')]")
    ))

    # Create a Select object
    select_month = Select(month_dropdown)

    # Select by index (3rd option)
    select_month.select_by_index(2)
    # Select by value (July)
    select_month.select_by_value("07")
    # Select by visible text (October)
    select_month.select_by_visible_text("OCT")

    # Print all available options
    options = select_month.options
    print("Total options:", len(options))
    for option in options:
        print(option.text)

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 