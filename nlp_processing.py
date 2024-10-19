# nlp_processing.py
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def simplify_command(command):
    # Process the command with spaCy NLP
    doc = nlp(command.lower())
    
    # Simplify: Find the search query after "search for"
    if "search for" in command:
        search_query = command.split("search for")[-1].strip()
        return {"action": "search", "query": search_query}

    # Fallback if no action is recognized
    return {"action": None, "query": None}
