## Inspiration
Across the world, there are **43 million** blind people, **295 million** moderately to severely visually impaired people, and **2.2 billion** visually impaired people overall. Inspired by the prevalence of blindness and visual impairment, even directly in our schools and communities, we investigated the ability of this population to use computers. We found that people with blindness and visual impairment cannot use computers quickly, and those who can generally require expensive equipment. Thus, we wanted to create software where users can use their voices to control what their computers do, alleviating the limitations of blindness and visual impairment in computer usage and increasing accessibility to computers.

## What it does
TalkTask takes voice command input after a user activation of the program with hotkey Ctrl + ', converts it into text using the speech_recognition library in Python, processes the command to find keywords such as "search" using natural language processing (NLP) techniques, opens a browser (Google Chrome), and uses the keywords to query the search engine. It then automatically searches for the words identified using NLP and reads out the first five options once they are searched.

## How we built it
We built TalkTask in Python using the Python speech_recognition library for voice recognition in our voice recognition Python script, which is first called when a user presses the Ctrl + ' hotkey; then, natural language processing breaks down the voice input into a command and a query. Next, based on the command, we start the automated Selenium Google Chrome browser and search for the prompt requested. Using pyttsx3, TalkTask reads the first five options the search engine gives audibly.

## Challenges we ran into
Challenges faced included appropriately recognizing the audio and ensuring the Selenium browser didn't close immediately after the search. This was difficult to implement, but we solved the issue based on our research.

## Accomplishments that we're proud of
We are proud of our conversion of spoken text into keywords with audio recognition and natural language processing.

## What we learned
Multiple skills were learned throughout this project: converting speech to text in Python, processing text and recognizing patterns using natural language processing techniques, commanding and querying search engines by automating them to perform specific tasks, and converting text to speech in Python.

## What's next for TalkTask
We want to go further by including artificial intelligence to allow the user's voice to command various parts of their computer while integrating with all the software on their laptop, possibly using macros.
