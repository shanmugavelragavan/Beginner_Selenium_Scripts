# Locators | ID , Partial link text , 
# link text , Class Name , NAME , 
# TAG_NAME , XPATH , CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Print page details
print("Title:", driver.title)
print("Current URL:", driver.current_url)

# Filling the form
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Hii I am")
driver.find_element(By.NAME, "email").send_keys("Shanmugavel@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234567890")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[name='bday']").send_keys("12-12-2000")

drop_down = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
drop_down.select_by_visible_text("Female")
drop_down.select_by_index(0)
# (OR)
# drop_down.select_by_value("value")

# Submitting the form
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Validating success message
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
message = "Success" in success_message
assert message, "Success message not found"
print("Form submitted successfully:", message)

# Handling another text input field (Enter & Clear)
text_input = driver.find_element(By.XPATH, "(//input[@type='text'])[3]")
text_input.send_keys("Shanmugavel")
time.sleep(1)
text_input.clear()

time.sleep(3)
driver.quit()
