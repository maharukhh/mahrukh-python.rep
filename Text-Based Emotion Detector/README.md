# Text-Based Emotion Detector

Detects fine-grained emotions — Joy, Anger, Sadness, Fear, Surprise — in text using built-in emotion word lexicons, extending basic positive/negative sentiment analysis into multiple specific emotion categories.

## How It Works
1. Text is tokenized into lowercase words.
2. Each word is checked against five built-in emotion word lists (Joy, Anger, Sadness, Fear, Surprise).
3. Matches are tallied per emotion category.
4. The category with the most matches is reported as the "dominant emotion," alongside the full breakdown of all detected emotions.

## Requirements
- Python 3.x (standard library only — no installs needed)

Type a sentence to see its detected emotion(s). Type `quit` to exit.

## Notes & Limitations
- This is a lexicon-based approach — like the Sentiment Analysis Tool, it only recognizes emotion words in its built-in lists and doesn't understand context, sarcasm, or emotions expressed indirectly (without explicit emotion words).
- Text can trigger multiple emotion categories at once (e.g. "happy but nervous" detects both Joy and Fear) — this is intentional and reflects that real text often carries mixed emotions.

## Possible Extensions
- Expand the emotion lexicons or load them from an established emotion-lexicon dataset (e.g. NRC Emotion Lexicon).
- Add emotion intensity scoring, not just detection.
- Train a proper multi-label classifier on a labeled emotion dataset for better generalization.
