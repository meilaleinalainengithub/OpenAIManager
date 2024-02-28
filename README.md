## OpenAiManager
- Auto Memorize Chat History
- Simple Chatting
- Handle Chat History & Bot Memory

# __init__(openai_key)
- Resets chat history
- Tries to login using OpenAI API key

# setup(system_message, model)
- Adds system message to the chat history
- Sets the AI model

# say(message)
- Formats the message to work with OpenAI
- Gets the response using the model and chat history
- Returns the response

# show_history()
- Returns chat history

# reset_history()
- Clears the history list

# add_memory(memory, role)
- Adds the string message as a string to the chat history

# remove_memory(memory, role)
- Checks if the string memory is in the chat history list
- Removes it from the chat history
