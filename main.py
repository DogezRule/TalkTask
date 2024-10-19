import keyboard
from voice_recognition import get_voice_command
from nlp_processing import simplify_command
from web_automation import search_google

# Toggle flag to track listening state
is_listening = False

def handle_voice_command():
    global is_listening
    
    if not is_listening:
        # Start listening
        is_listening = True
        print("Voice command listening started...")
        command = get_voice_command()
        
        # Step 2: Print the captured command for debugging
        if command:
            print(f"Captured Command: {command}")  # Debug: Print the raw voice input

            # Step 3: Simplify the command
            simplified_command = simplify_command(command)
            print(f"Simplified Command: {simplified_command}")  # Debug: Print the simplified command

            # Step 4: Check if the action is "search"
            if simplified_command["action"] == "search":
                query = simplified_command["query"]
                if query:
                    print(f"Executing search for: {query}")  # Debug: Print the search query
                    result = search_google(query)
                    print(f"Search Result: {result}")  # Debug: Print the first search result
            else:
                print("No valid action identified in the command.")  # Debug: If no action is identified
        
    else:
        # Stop listening
        is_listening = False
        print("Voice command listening stopped.")

def main():
    print("Press 'Ctrl + ' to toggle voice command listening...")

    # Set up hotkey for Ctrl + ' (single quote key)
    keyboard.add_hotkey("ctrl+'", handle_voice_command)
    
    # Keep the program running and wait for ESC to exit
    print("Press ESC to exit the program.")
    keyboard.wait('esc')  # Wait for 'ESC' key to exit

if __name__ == "__main__":
    main()
