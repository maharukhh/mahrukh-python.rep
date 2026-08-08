#  Sentiment Analysis Tool

A lexicon-based sentiment analyzer that classifies text as Positive, Negative, or Neutral, with basic negation handling (e.g. "not happy" correctly flips to negative).

## How It Works
1. Text is tokenized into lowercase words.
2. Each word is checked against built-in positive/negative word lists.
3. A simple negation check flips the polarity of the next sentiment word if preceded by a negation ("not", "never", "don't", etc.).
4. Word scores are summed; the final total decides Positive / Negative / Neutral.

## Requirements
- Python 3.x (standard library only — no installs needed)

Type any sentence and press Enter to see its sentiment label and score. Type `quit` to exit.

## Notes & Limitations
- This is a lexicon-based approach — it doesn't understand sarcasm, context, or words outside its built-in lists.
- For production use, a trained ML/transformer-based sentiment model would generalize far better; this demo prioritizes being fully offline and dependency-free.

## Possible Extensions
- Expand the word lists or load them from an external file.
- Add intensity modifiers ("very", "extremely") to weight scores.
- Swap in a trained scikit-learn classifier for better generalization.
