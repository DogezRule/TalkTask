from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_google(query):
    # Ensure ChromeDriver is installed and in PATH
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    
    # Search for the query
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Get the first search result
    first_result = driver.find_element("xpath", "//h3").text
    print("First result: ", first_result)
    
    # Wait for user input to manually close the browser
    input("Press Enter to close the browser...")
    driver.quit()  # Manually close the browser when the user presses Enter
    
    return first_result
