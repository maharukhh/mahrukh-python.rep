"""
Speech Processing Tool (Speech-to-Text and Text-to-Speech)
-----------------------------------------------------------------
Two-way speech processing:
  - Text-to-Speech (TTS): speaks any typed text out loud (fully offline).
  - Speech-to-Text (STT): listens through your microphone and transcribes
    what you say (uses Google's free Web Speech API over the internet
    for recognition — requires an internet connection at runtime).

Requirements:
  pip install pyttsx3 SpeechRecognition pyaudio

  Note: pyaudio can be tricky to install on Windows via plain pip. If
  `pip install pyaudio` fails, try:
    pip install pipwin
    pipwin install pyaudio

Usage:
  python speech_processing.py
"""

import pyttsx3
import speech_recognition as sr


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "(Could not understand audio)"
    except sr.RequestError as e:
        return f"(Speech recognition service error: {e})"


def main():
    print("Speech Processing Tool")
    print("1) Text-to-Speech (type text, hear it spoken)")
    print("2) Speech-to-Text (speak into your mic, see it transcribed)")
    print("Type 'quit' to exit.\n")

    while True:
        choice = input("Choose 1 or 2: ").strip()
        if choice.lower() == "quit":
            break

        if choice == "1":
            text = input("Text to speak: ").strip()
            if text:
                text_to_speech(text)

        elif choice == "2":
            result = speech_to_text()
            print(f"  Transcribed: {result}\n")

        else:
            print("Please enter 1, 2, or 'quit'.\n")


if __name__ == "__main__":
    main()
