from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3
import threading
import queue  # Import queue for thread-safe communication

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Create a queue to manage the text-to-speech commands
speech_queue = queue.Queue()

# Function to speak the text using pyttsx3, running in the main thread
def speak_text_from_queue():
    while True:
        # Block until there's something to speak
        text = speech_queue.get()
        if text is None:  # We can use 'None' as a signal to exit the loop if needed
            break
        engine.say(text)
        engine.runAndWait()  # Run and wait for the speech engine to finish speaking
        speech_queue.task_done()

# Function to add text to the speech queue (can be called from any thread)
def speak_text(text):
    speech_queue.put(text)

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

        # Prepare and say the first 5 results
        print(f"Top 5 search results for '{query}':")
        text = ""
        for i, result in enumerate(results[:5], 1):  # Get the first 5 results
            print(f"{i}. {result.text}")
            text += f"Result {i}. {result.text}. "

        # Queue the results for speaking
        speak_text(text)

        # Allow user to press Enter to close the browser while the engine speaks
        input("Press Enter to close the browser...")  # Keeps browser open until user presses Enter
        driver.quit()  # Close the browser after the user presses Enter

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

