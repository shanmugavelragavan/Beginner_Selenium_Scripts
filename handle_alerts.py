# Handle Different Types of Alerts 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def handle_simple_alert(driver):
    driver.find_element(By.ID, "alertexamples").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Simple Alert Text:", alert.text)
    alert.accept()

def handle_confirmation_alert(driver):
    driver.find_element(By.ID, "confirmexample").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Confirmation Alert Text:", alert.text)
    alert.dismiss()

def handle_prompt_alert(driver):
    driver.find_element(By.ID, "promptexample").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Prompt Alert Text:", alert.text)
    alert.send_keys("Shanmugavel")
    alert.accept()

def main():
    driver = webdriver.Chrome()
    driver.get("http://testpages.herokuapp.com/styled/alerts/alert-test.html")
    driver.maximize_window()
    driver.implicitly_wait(3)
    try:
        handle_simple_alert(driver)
        handle_confirmation_alert(driver)
        handle_prompt_alert(driver)
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
    finally:
        driver.quit()

if __name__ == "__main__":
    main() 