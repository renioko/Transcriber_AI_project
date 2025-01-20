import os
from dotenv import load_dotenv

import openai

class Transformer:
    @staticmethod
    def load_api_key() -> str:
        """Loads api key from the environment."""
        load_dotenv()
        openai.api_key = os.getenv('OPEN_API_KEY')
        if not openai.api_key:
            raise ValueError("OPEN_API_KEY not found")
        return openai.api_key
    
    def __init__(self) -> None:
        pass

class Transcribed(Transformer):
    """Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text."""

    def __init__(self, inputfile: str) -> None:
        try:
            super().load_api_key()
        except ValueError as e:
            print(e)
        self.inputfile = inputfile
   
    def transcribe_audio(self) -> None:
        """Transcribes the given audio file and prints the text."""
        try:
            with open(self.inputfile, 'rb') as audio_file:
                transcription = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format='text'
        )
            print(transcription)
        except Exception as e:
            print(f'Failed transcription: {e}')
        # ubgrade: mmozna wybrac print, save into a file or return

def main():
    filename = "C:\\Users\\renio\\Documents\\Recordings\\Text to transcribe2.mp3"
    try:
        transcribed = Transcribed(filename)
        transcribed.transcribe_audio()
    except ValueError:
        print("Please set the API key in your environment and try again.")

if __name__ == '__main__':
    main()