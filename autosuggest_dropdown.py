# Handle Auto-Suggestion Dropdown

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

try:
    # Find the auto-suggest input and type 'ind'
    autosuggest = driver.find_element(By.ID, "autosuggest")
    autosuggest.send_keys("ind")
    sleep(2)  # Wait for suggestions to load

    # Find all suggestion options
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print("Number of suggestions:", len(countries))

    # Click on 'India' if present
    for country in countries:
        if country.text == "India":
            country.click()
            break
    else:
        print("No matching country found!")

    # Verify the selection
    assert autosuggest.get_attribute("value") == "India"
    print("Successfully selected 'India' from suggestions.")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 