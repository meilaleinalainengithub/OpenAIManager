from openai import OpenAI

class ChatManager():
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

    def add_memory(self, memory, role):
        '''Types:\n
        user: the person interacting with the AI\n
        assistant: the AI itself\n
        system: the AI's context for the conversation and how to act'''
        memory = ({"role": role, "content": memory})
        self.chat_history.append(memory)
    
    def remove_memory(self, memory, role):
        '''Types:\n
        user: the person interacting with the AI\n
        assistant: the AI itself\n
        system: the AI's context for the conversation and how to act'''
        if memory in self.chat_history:
            memory = ({"role": role, "content": memory})
            self.chat_history.remove(memory)
        else:
            print("Failed to remove memory. Invalid memory data.\nTIP: Try running 'show_history' to see all memory data.")

class ImageManager():
    def __init__(self, openai_key):
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
        
    def setup(self, model):
        self.model = model

    def gen(self, message, size, quality, amount):
        '''Sizes:\n
        1024x1024\n1024x1792\n\n1792x1024\n\n
        Qualities:\n
        standard\nhd\n\n
        Amount: 1-10'''

        try:
            response = self.client.images.generate(
                model=self.model,
                prompt=message,
                size=size,
                quality=quality,
                n=amount,
            )

            image = response.data[0].url
            return image
        
        except Exception as e:
            print(f"Error: {e}. Please ensure the setup is correct and the API is accessible.")

class SpeechManager():
    def __init__(self, openai_key):
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
    
    def setup(self, model):
        self.model = model

    def TTS(self, voice, message, file_path):
        '''Voices:\n
        Male: Echo, Onyx\n
        Female: Nova, Shimmer\n
        Neutral: Alloy, Fable'''

        response = self.client.audio.speech.create(
            model=self.model,
            voice=voice,
            input=message
        )

        try:
            with open(file_path, "wb") as file:
                file.write(response.content)
        except Exception as e:
            print(f"Error: {e}. Please ensure your file is accessible.")
       

    def STT(self, file_path):
        '''Supported File Paths:\n
        Audio: MP3, WAV, MPGA, M4A\n
        Video: MP4, WEBM, MPEG'''
        try:
            audio_file = open(file_path, "rb")

            transcription = self.client.audio.transcriptions.create(
            model=self.model, 
            file=audio_file, 
            response_format="text"
            )

            return transcription.text
        except Exception as e:
            print(f"Error: {e}. Please ensure your file is accessible and under 25mb")