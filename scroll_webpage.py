# Automate Webpage Scrolling 

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()

try:
    # Scroll down by 100 pixels
    driver.execute_script("window.scrollBy(0, 100)")

    # Wait for an element and scroll it into view
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="standard-collection-wdgt"]/div/h2'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    # Scroll up by 100 pixels
    driver.execute_script("window.scrollBy(0, -100)")

    print("Scrolling actions completed!")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 