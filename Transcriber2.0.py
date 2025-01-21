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
   
    def transcribe_audio(self, output_file: str=None) -> str:
        """Transcribes the given audio file and returns text.
        //prints the text or saves it to a file.//"""
        try:
            with open(self.inputfile, 'rb') as audio_file:
                transcription = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format='text'
        )
            return transcription

        except FileNotFoundError:
            print("Audio file not found.")
        except openai.OpenAIError as e:
            print(f"Problem with OpenAI, transcription failed: {e}")
        except Exception as e:
            print(f'Failed transcription: {e}')

def transcription_handling(transcription: str, output_file: str=None) -> None:
    """ Saves transcription into a file if path given, else prints transcription."""
        
    if output_file:
        try:
            with open(output_file, 'w') as writer:
                writer.write(transcription) # (transcription.text) ?
            print("Transcription saved.")
        except FileNotFoundError:
            print("Error, output file not found. Please enter correct path.")
    else:
        print(f"Transcription: {transcription}")

def main():
    # filename = "C:\\Users\\renio\\Documents\\Recordings\\Text to transcribe2.mp3"
    filename = input("Enter path to audio: ")

    try:
        transcribed = Transcribed(filename)
        text = transcribed.transcribe_audio()
    except ValueError:
        print("Please set the API key in your environment and try again.")

    transcription_handling(text, output_file=None)

if __name__ == '__main__':
    main()

        # ubgrade: choose to print, save into a file or return - maybe with click library