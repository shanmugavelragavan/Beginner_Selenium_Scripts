# Open Browser, Print Title, and Minimize 

from selenium import webdriver

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
try:
    # Open YouTube
    driver.get("https://www.youtube.com/")
    driver.maximize_window()

    # Print the page title
    print("Page Title:", driver.title)

    # Minimize the window
    driver.minimize_window()

except Exception as e:
    print("Error:", e)
finally:
    driver.quit() 