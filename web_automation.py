from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search_google(query):
    try:
        # Path to ChromeDriver (if it's not in PATH, specify the full path)
        # Example: driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

        # Open Google
        driver.get("http://www.google.com")
        print("Chrome opened successfully.")

        # Find the search box and input the query
        search_box = driver.find_element("name", "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the results to load
        time.sleep(2)

        # Get the first search result
        first_result = driver.find_element("xpath", "//h3").text
        print(f"First result: {first_result}")
        
        # Keep the browser open
        i = input("Press Enter to close the browser...")  # Keep browser open until user input
        if i == "":
            driver.quit()  # Close the browser after the user presses Enter
        
        return first_result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
