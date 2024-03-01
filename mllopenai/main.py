from openai import OpenAI
import tiktoken

class ChatManager():
    def __init__(self, openai_key: str):
        self.chat_history = []
        self.raw_history = []
        
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
        
    def setup(self, system_message: str, model: str):
        self.model = model
        self.chat_history.append({"role": "system", "content": system_message})
        self.raw_history.append(system_message)

    def say(self, message: str):
        try:
            self.chat_history.append({"role": "user", "content": message})
            self.raw_history.append(message)

            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.chat_history
            )

            bot_message = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": bot_message})
            self.raw_history.append(bot_message)
        
            enc = tiktoken.get_encoding("cl100k_base")
            assert enc.decode(enc.encode(self.raw_history)) == self.raw_history
            enc = tiktoken.encoding_for_model(self.model)
            print(enc)
        
            return bot_message
        except Exception as e:
            print(f"Error: {e}. Please ensure the setup is correct and the API is accessible.")
    
    def say_without_memory(self, message: str):
        try:
            self.raw_history.append(message)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message
            )

            bot_message = response.choices[0].message.content

            enc = tiktoken.get_encoding("cl100k_base")
            assert enc.decode(enc.encode(self.raw_history)) == self.raw_history
            enc = tiktoken.encoding_for_model(self.model)
            print(enc)

            return bot_message
        
        except Exception as e:
            print(f"Error: {e}. Please ensure the setup is correct and the API is accessible.")
    
    def show_history(self) -> str:
        return self.chat_history
    
    def reset_history(self) -> str:
        self.chat_history = []

    def add_memory(self, memory: str, role: str):
        '''Types:\n
        user: the person interacting with the AI\n
        assistant: the AI itself\n
        system: the AI's context for the conversation and how to act'''
        memory = ({"role": role, "content": memory})
        self.chat_history.append(memory)
        self.raw_history.append(memory)

        enc = tiktoken.get_encoding("cl100k_base")
        assert enc.decode(enc.encode(self.raw_history)) == self.raw_history
        enc = tiktoken.encoding_for_model(self.model)
        print(enc)
    
    def remove_memory(self, memory: str, role: str):
        '''Types:\n
        user: the person interacting with the AI\n
        assistant: the AI itself\n
        system: the AI's context for the conversation and how to act'''
        if memory in self.chat_history:
            memory = ({"role": role, "content": memory})
            self.chat_history.remove(memory)
        else:
            print("Failed to remove memory. Invalid memory data.\nTry running 'show_history' to see all memory data.")

    def get_all_tokens(self):
        enc = tiktoken.get_encoding("cl100k_base")
        assert enc.decode(enc.encode(self.raw_history)) == self.raw_history
        enc = tiktoken.encoding_for_model(self.model)
        return enc
    
    def get_string_tokens(self, message):
        enc = tiktoken.get_encoding("cl100k_base")
        assert enc.decode(enc.encode(message)) == message
        enc = tiktoken.encoding_for_model(self.model)
        return enc

class ImageManager():
    def __init__(self, openai_key: str):
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
        
    def setup(self, model: str):
        self.model = model

    def gen(self, message: str, size: int, quality: str, amount: int):
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
    def __init__(self, openai_key: str):
        try:
            self.client = OpenAI(api_key=openai_key)
        except Exception:
            print("OpenAI key invalid. Please check the path to your key.")
    
    def setup(self, model: str):
        self.model = model

    def TTS(self, voice: str, message: str, file_path: str):
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
       

    def STT(self, file_path: str):
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