from load_api_key import load_api_key
import openai
import sys

"""Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text."""

def load_and_and_transcript_audio(filename: str) -> None:
    """loads audio file, connects with whisper, 
    transcribes audio file into a text and prints it"""
    load_api_key()
    with open(filename, 'rb') as audio_file:
        transcription = openai.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format='text'
)
    print(transcription)


def main():

    if len(sys.argv) > 2:
        filename = sys.argv[1]
    else:
        filename = "C:/Users/renio/Documents/Recordings/Text-to-transcribe.mp3"

    load_and_and_transcript_audio(filename)

if __name__ == '__main__':
    main()




