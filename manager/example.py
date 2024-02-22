import os
from openaimanager import OpenAIManager
from dotenv import load_dotenv
load_dotenv('.env')

# INITIALIZE AND SEND OPENAI KEY
OpenAIManager = OpenAIManager(os.getenv("OPENAI_KEY"))

# SETUP
OpenAIManager.setup(system_message="You are a helpful yet sassy assistant.", model="gpt-3.5-turbo-0125")

# TALK TO THE AI
response = OpenAIManager.say(message="Hello, how are you?")
print(response)

# SHOW & RESET HISTORY
history = OpenAIManager.show_history()
print(history)
OpenAIManager.reset_history()