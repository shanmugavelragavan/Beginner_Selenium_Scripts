# Handle Multiple Windows/Tabs 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
driver.get("https://www.naukri.com")
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)
    # Click a link that opens a new window/tab
    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="trending-naukri-wdgt"]/div/div[1]/a[2]/span')))
    link.click()

    # Store the parent window handle
    parent_window = driver.current_window_handle
    print("Parent Window Handle:", parent_window)

    # Get all window handles
    all_windows = driver.window_handles

    # Loop through all open windows
    for handle in all_windows:
        driver.switch_to.window(handle)
        print("Window Title:", driver.title)
        if handle != parent_window:
            driver.close()  # Close child windows

    # Switch back to the parent window
    driver.switch_to.window(parent_window)

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 