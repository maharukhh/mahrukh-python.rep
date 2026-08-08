# Speech Processing Tool (Speech-to-Text and Text-to-Speech)

A two-way speech tool: type text and have it spoken aloud (Text-to-Speech), or speak into your microphone and see it transcribed to text (Speech-to-Text).

## How It Works
1. **Text-to-Speech (TTS)** uses `pyttsx3`, which runs fully offline using your operating system's built-in speech engine (SAPI5 on Windows).
2. **Speech-to-Text (STT)** uses the `SpeechRecognition` library with your microphone as the audio source, sending the recorded audio to Google's free Web Speech API for transcription (this part requires an active internet connection at runtime).

## Requirements
- Python 3.x
- `pip install pyttsx3 SpeechRecognition pyaudio`
```

## Usage
```bash
python speech_processing.py
```
Choose `1` for Text-to-Speech (type text, hear it spoken) or `2` for Speech-to-Text (speak into your mic after "Listening..." appears). Type `quit` to exit.

## Notes & Limitations
- Speech-to-Text requires a working microphone and an internet connection (it calls Google's free recognition API).
- Text-to-Speech voice/quality depends on your OS's installed speech voices.
- Background noise can affect transcription accuracy; the tool does a brief ambient-noise calibration before listening.

## Possible Extensions
- Add support for multiple languages in STT (`recognize_google(audio, language="ur-PK")`, etc.).
- Let the user choose a specific TTS voice or adjust pitch/rate interactively.
- Save transcribed text to a file automatically.
