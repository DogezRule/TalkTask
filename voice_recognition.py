import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    try:
        with sr.Microphone() as source:
            print("Microphone is active. Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Optional: reduce background noise
            print("Listening for your command...")
            audio = recognizer.listen(source)
            print("Audio captured, processing...")

            # Try recognizing the voice using Google Speech Recognition
            command = recognizer.recognize_google(audio)
            print(f"Captured Command: {command}")
            return command
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
