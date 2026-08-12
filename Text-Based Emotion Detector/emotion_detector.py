"""
Text-Based Emotion Detector
--------------------------------
Detects fine-grained emotions (Joy, Anger, Sadness, Fear, Surprise) in
text using built-in emotion lexicons — a multi-class extension of basic
positive/negative sentiment analysis. No external downloads needed.

Usage:
  python emotion_detector.py
"""

import re

EMOTION_LEXICON = {
    "Joy": {
        "happy", "joyful", "excited", "delighted", "cheerful", "glad",
        "pleased", "thrilled", "content", "elated", "wonderful", "great",
        "love", "fun", "laugh", "smile", "grateful",
    },
    "Anger": {
        "angry", "furious", "annoyed", "irritated", "mad", "rage",
        "outraged", "hate", "resent", "frustrated", "hostile", "bitter",
    },
    "Sadness": {
        "sad", "unhappy", "depressed", "down", "gloomy", "heartbroken",
        "miserable", "sorrow", "grief", "lonely", "hopeless", "crying",
    },
    "Fear": {
        "afraid", "scared", "terrified", "anxious", "nervous", "worried",
        "frightened", "panic", "dread", "uneasy", "fearful",
    },
    "Surprise": {
        "surprised", "shocked", "astonished", "amazed", "stunned",
        "unexpected", "startled", "wow", "unbelievable",
    },
}


def tokenize(text):
    return re.findall(r"[a-zA-Z']+", text.lower())


def detect_emotions(text):
    tokens = set(tokenize(text))
    scores = {}

    for emotion, words in EMOTION_LEXICON.items():
        matched = tokens & words
        if matched:
            scores[emotion] = len(matched)

    return scores


def main():
    print("Text-Based Emotion Detector")
    print("Detects: Joy, Anger, Sadness, Fear, Surprise")
    print("Type a sentence (type 'quit' to exit).\n")

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue

        scores = detect_emotions(text)
        if not scores:
            print("  No strong emotion detected (neutral or unrecognized words).\n")
            continue

        dominant = max(scores, key=scores.get)
        print(f"  Dominant emotion: {dominant}")
        print(f"  All detected: {scores}\n")


if __name__ == "__main__":
    main()
