## Inspiration
Across the world, there are **43 million** blind people, **295 million** moderately to severely visually impaired people, and **2.2 billion** visually impaired people overall. Inspired by the prevalence of blindness and visual impairment, even directly in our schools and communities, we investigated the ability of this population to use computers. We found that people with blindness and visual impairment cannot use computers quickly, and those who can generally require expensive equipment. Thus, we wanted to create software where users can use their voices to control what their computers do, alleviating the limitations of blindness and visual impairment in computer usage and increasing accessibility to computers.

## What it does
TalkTask takes voice command with a shortcut and converts it into text. Then, it processes the command to find keywords such as "search." The words after that are used to query the browser. Then it opens Google Chrome, automatically searches the words you asked for, and reads out the first five options once searched.
## How we built it
We built it using Google Audio for voice recognition in our voice recognition Python script, which is first called when you press the command "control and the key for apostrophe" at the same time; then, once you push it to signify the end of your prompt, it turns it into text using Google Audio. Once we have that in text format, we start the automated Selenium Google browser and search for the prompt requested. Then, it reads out loud using pyttsx3 with the first five options the search engine gives. 
## Challenges we ran into
We struggled with appropriately recognizing the audio and ensuring the Selenium browser didn't close immediately after the search. 
## Accomplishments that we're proud of
We are proud of our conversion of keywords with "search for" with audio recognition  
## What we learned
We learned how to convert speech to text in Python while integrating with browsers by automating them.
## What's next for TalkTask
We want to go further by including AI to allow the user's voice to command their entire computer while integrating with all the software on their laptop, possibly using macros.
