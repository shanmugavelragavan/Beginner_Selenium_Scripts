# Handle Radio Buttons 

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    # Open the registration page
    driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Locate radio buttons
    male_radio = driver.find_element(By.XPATH, "//input[@value='m']")
    female_radio = driver.find_element(By.XPATH, "//input[@value='f']")

    # Click on Female option
    female_radio.click()

    # Print selection and state
    print("Is Female selected:", female_radio.is_selected())
    print("Is Female enabled:", female_radio.is_enabled())
    print("Is Female displayed:", female_radio.is_displayed())
    print("Is Male selected:", male_radio.is_selected())

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 