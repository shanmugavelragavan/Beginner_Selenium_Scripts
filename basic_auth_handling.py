# Handle Basic HTTP Authentication 

from selenium import webdriver

# Credentials and URL
username = "admin"
password = "admin"
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    driver.get(url)
    print("Authentication successful!")
except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 