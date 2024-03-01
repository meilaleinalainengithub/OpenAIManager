# OpenAiManager
## ChatManager
- Automatically store current chat history.
- Simple Chatting.
- Manually handle chat history.
- Automatically calculate tokens used.

### __init__(openai_key)
- Resets chat history
- Tries to login using OpenAI API key

### setup(system_message, model)
- Adds system message to the chat history
- Sets the AI model

### say(message)
- Formats the message to work with OpenAI
- Gets the response using the model and chat history
- Returns the response

### say_without_history(message)
- Gets the response using the model WITHOUT chat history
- Returns the response

### show_history()
- Returns chat history

### reset_history()
- Clears the history list

### add_memory(memory, role)
- Adds the string message as a string to the chat history

### remove_memory(memory, role)
- Checks if the string memory is in the chat history list
- Removes it from the chat history

### get_all_tokens()
- Gets current chats tokens used
- Returns tokens used

### get_string_tokens(message)
- Get string (message) tokens
- Returns tokens used

## ImageManager
- Generate Images with prefered model

### __init__(openai_key)
- Tries to login using OpenAI API key

### setup(model)
- Sets the AI model

### gen(message, size, quality, amount)
- Generates Images based off input (message)
- Specifies the image size (size)
- Specifies the image quality (quality)
- Generates 1-10 images (amount)

## SpeechManager
- Convert Text to Speech
- Convert Speech to Text

### __init__(openai_key)
- Tries to login using OpenAI API key

### setup(model)
- Sets the AI model

### TTS(voice, message, file_path)
- Converts Text (message) to Speech (voice)
- Creates audio file (file_path)

### STT(file_path)
- Opens file (file_path)
- Converts Speech to Text (model from setup)
- Returns Speech to Text