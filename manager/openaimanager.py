from openai import OpenAI

class OpenAIManager():
    def __init__(self, openai_key):
        self.chat_history = []
        
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
        
    def setup(self, system_message, model):
        self.model = model
        self.chat_history.append({"role": "system", "content": system_message})

    def say(self, message):
        try:
            self.chat_history.append({"role": "user", "content": message})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.chat_history
            )

            bot_message = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": bot_message})
            return bot_message
        
        except Exception as e:
            print(f"Error: {e}. Please ensure the setup is correct and the API is accessible.")
    
    def show_history(self):
        return self.chat_history
    
    def reset_history(self):
        self.chat_history = []

    def add_memory(self, memory):
        self.chat_history.append(memory)
    
    def remove_memory(self, memory):
        if memory in self.chat_history:
            self.chat_history.remove(memory)
        else:
            print("Failed to remove memory. Invalid memory data.\nTIP: Try running 'show_history' to see all memory data.")