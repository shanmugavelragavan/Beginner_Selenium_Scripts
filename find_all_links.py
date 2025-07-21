# Find All Links on a Webpage 

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    # Open the target website
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Find all <a> tags (links)
    links = driver.find_elements(By.TAG_NAME, "a")
    print("Total links found:", len(links))

    # Print the first 10 link URLs
    for i, link in enumerate(links[:10]):
        print(f"Link {i+1}: {link.get_attribute('href')}")

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 