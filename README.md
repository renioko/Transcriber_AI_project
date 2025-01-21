# Transcriber_AI_Project

The Transcriber_AI_Project is a collection of Python scripts designed for transcribing audio files to text. It uses various methods, including the OpenAI Whisper API and direct HTTP requests.

## Table of Contents

- [Transcriber\_AI\_Project](#transcriber_ai_project)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Transcription using OpenAI Whisper](#transcription-using-openai-whisper)
    - [Shorter script with OpenAI Whisper](#shorter-script-with-openai-whisper)
    - [Transcription using HTTP and the requests library](#transcription-using-http-and-the-requests-library)
  - [Usage Examples](#usage-examples)
    - [Requirements](#requirements)
    - [License](#license)
    - [Contact](#contact)

## Description

This project was created to provide flexible audio transcription options. It offers different approaches, allowing users to choose the method that best suits their needs.

## Features

*   Transcribes audio files (mp3, mp4, mpeg, mpga, wav, webm) to text.
*   Uses the OpenAI Whisper API for high-quality transcription.
*   Offers an alternative transcription method using direct HTTP requests (i.e for educational purposes). (Maybe in the future will be added option to use alternative urls)
*   Option to save transcriptions to a file.
*   Command-line argument support (optional, depending on the implementation).

## Getting Started
Ready to transcribe your audio files? Here's a quick guide to get you started:

1. Set up your environment: Make sure you have Python 3.x installed on your system.
2. Clone the repository: Use git clone https://github.com/renioko/Transcriber_AI_project to clone the project code.
3. Install dependencies: Refer to the "Installation" section for specific libraries needed based on your chosen transcription method.
4. Choose your script: Decide whether you want to use OpenAI Whisper (Transcriber2.0.py or Transcriber.py) or the HTTP-based method (transcriber_http.py).
5. Prepare your audio file: Ensure your audio file is in a supported format (mp3, mp4, mpeg, mpga, wav, webm).
6. Run the script: Follow the command-line instructions provided in the "Usage" section for the chosen script. 
7. Replace path_to_audio_file with the actual path to your audio file. Optionally, provide an -o argument and a path to save the transcription as a text file.
8. 
By following these steps, you should be able to successfully transcribe your audio files using the Transcriber_AI_Project.

## Installation
1.  Clone the repository:

    ```bash
    git clone https://github.com/renioko/Transcriber_AI_project
    ```

2.  Navigate to the project directory:

    ```bash
    cd Project-Transcriber
    ```

3.  Install the required libraries (depending on the method used):

    *   For transcription with OpenAI Whisper:

        ```bash
        pip install openai python-dotenv
        ```

    *   For transcription with HTTP and `requests`:

        ```bash
        pip install requests
        ```

## Usage
...

## Transcription using OpenAI Whisper

Ensure you have set your OpenAI API key in the `OPEN_API_KEY` environment variable. Create a `.env` file in the project directory and add the following:

```
OPEN_API_KEY=your_api_key
```

Then, run the script:

```bash
python Transcriber2.py "path_to_audio_file" [-o path_to_output_file]
```
For example:

Bash
```
python Transcriber2.0.py audio.mp3 -o "file to transcription.txt"
```

### Shorter script with OpenAI Whisper
Running this script is similar to the full script, but it may offer fewer configuration options.

Bash
```
python Transcriber.py "path_to_audio_file"
```

### Transcription using HTTP and the requests library
Run the script:

Bash
```
python http_script_name.py path_to_audio_file [-o path_to_output_file]
```
For example:

Bash
```
python transcriber_http.py audio.mp3 -o transcription.txt
```
## Usage Examples
Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text.
If you want to save your transcription into a file - use Transcriber2.py - then add output file name in command line. Otherwise your transcription will be printed out.

If you just want to see a quic transcription go for Transcriber.py

Transcriber_HTTP.py - I wrote it to see check possibility for using requests library for transcriptions. Use it if you cannot download openai library. 

### Requirements
Python 3.x
The libraries listed in the Installation section.
For OpenAI Whisper transcription: An OpenAI API key.
For HTTP transcription: Access to a transcription API.

### License
MIT License
If you like to use my code just please let me know - I'd love to see how you improve it :-)

### Contact
email: renatta.gasior@gmail.com
GitHub: https://github.com/renioko
