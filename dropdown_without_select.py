# Handle Dropdown without using Select Class

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in/")
driver.implicitly_wait(10)

try:
    # Click to open the dropdown menu
    dropdown_button = driver.find_element(By.XPATH, '//*[@id="account_dd"]/div[1]/span')
    dropdown_button.click()

    # Find all dropdown options
    options = driver.find_elements(By.XPATH, '//*[@id="account_dd"]/div[2]/ul/li')

    # Loop through and find "Show My Ticket"
    found = False
    for option in options:
        if option.text.strip() == "Show My Ticket":
            option.click()
            found = True
            break

    if found:
        print("Successfully Clicked 'Show My Ticket'")
    else:
        print("'Show My Ticket' option not found in dropdown.")

    time.sleep(3)
finally:
    # Close the browser
    driver.quit()
