from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3 

engine = pyttsx3.init()

def search_google(query):
    try:
        # Open Chrome using the ChromeDriver
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
        driver.get("http://www.google.com")
        print("Chrome opened successfully.")

        # Find the search box and input the query
        search_box = driver.find_element("name", "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(2)

        # Find all results (usually under <h3> tags)
        results = driver.find_elements("xpath", "//h3")

        # Print the first 5 results
        print(f"Top 5 search results for '{query}':")
        text = ""
        for i, result in enumerate(results[:5], 1):  # Get the first 5 results
            print(f"{i}. {result.text}")
            text += f"Result {i}. {result.text}. "
        engine.say(text)
        engine.runAndWait()
        
        # Keep the browser open
        input("Press Enter to close the browser...")  # Keep browser open until user input
        driver.quit()  # Close the browser after the user presses Enter

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
