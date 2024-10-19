

def simplify_command(command):

    if "search for" in command:
        search_query = command.split("search for")[-1].strip()
        return {"action": "search", "query": search_query}

    # Fallback if no action is recognized
    return {"action": None, "query": None}
