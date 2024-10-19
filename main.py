import threading
import keyboard
from voice_recognition import get_voice_command
from nlp_processing import simplify_command
from web_automation import search_google

# Toggle flag to track listening state
is_listening = False
recognition_thread = None
captured_command = None  # This will hold the captured voice command

def handle_voice_command():
    global is_listening, recognition_thread, captured_command

    if not is_listening:
        # Start listening
        is_listening = True
        print("Voice command listening started...")

        # Start a separate thread for voice recognition so it doesn't block the main thread
        recognition_thread = threading.Thread(target=capture_command)
        recognition_thread.start()

    else:
        # Stop listening and process the command
        is_listening = False
        print("Voice command listening stopped.")
        
        # Process the captured command
        if captured_command:
            print(f"Captured Command: {captured_command}")  # Debugging line to ensure the command was captured

            # Simplify and process the command
            simplified_command = simplify_command(captured_command)
            print(f"Simplified Command: {simplified_command}")

            if simplified_command["action"] == "search":
                query = simplified_command["query"]
                if query:
                    print(f"Executing search for: {query}")
                    result = search_google(query)
                    print(f"Search Result: {result}")
            else:
                print("No valid action identified in the command.")
        else:
            print("No command captured.")

def capture_command():
    global captured_command
    # Capture the voice command
    captured_command = get_voice_command()

def main():
    print("Press 'Ctrl + ' to toggle voice command listening...")

    # Set up hotkey for Ctrl + ' (single quote key)
    keyboard.add_hotkey("ctrl+'", handle_voice_command)

    # Keep the program running and wait for ESC to exit
    print("Press ESC to exit the program.")
    keyboard.wait('esc')  # Wait for 'ESC' key to exit

if __name__ == "__main__":
    main()
