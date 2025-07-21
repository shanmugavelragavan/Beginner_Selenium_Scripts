# Handle UI Controls: Checkboxes, Radio Buttons, Visibility 

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Handle checkboxes
    checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
    print("Number of checkboxes:", len(checkboxes))
    for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2":
            checkbox.click()
            assert checkbox.is_selected()
            print("Checkbox 'option2' selected.")
            break

    # Handle radio buttons
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
    radio_buttons[2].click()
    assert radio_buttons[2].is_selected()
    print("Radio button 3 selected.")

    # Check visibility of a text box
    displayed_text = driver.find_element(By.ID, "displayed-text")
    assert displayed_text.is_displayed()
    print("Text box is displayed.")

    # Hide the text box
    driver.find_element(By.ID, "hide-textbox").click()
    assert not displayed_text.is_displayed()
    print("Text box is now hidden.")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 