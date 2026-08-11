# Fake News Detector

Classifies news headlines as "Likely Real" or "Likely Fake" using a Naive Bayes classifier trained on a small built-in labeled toy dataset.

## How It Works
1. A tiny set of example headlines, labeled "Likely Real" or "Likely Fake," is defined in the script (real headlines are more neutral/factual in tone; fake examples use classic clickbait/sensationalist patterns).
2. Headlines are converted to TF-IDF vectors.
3. A Multinomial Naive Bayes classifier is trained on these vectors and labels.
4. New headlines you type are classified the same way, with a confidence score.

## Requirements
- Python 3.x
- scikit-learn (`pip install scikit-learn`)

Type a headline to classify it. Type `quit` to exit.

## ⚠️ Important Limitations
**This is an educational demonstration of the technique, not a production fact-checking tool.** With only 14 training examples, it has essentially memorized surface-level patterns (sensationalist wording like "shocking," "miracle," "secret") rather than learning to verify facts. It will **not** reliably classify real-world headlines it hasn't seen patterns like before. A real fake-news detection system needs:
- Tens of thousands of diverse, well-labeled training examples
- Source credibility signals (not just headline text)
- Cross-referencing with fact-checking databases/APIs
- Regular retraining as misinformation tactics evolve

## Possible Extensions
- Train on a real, large-scale labeled fake news dataset.
- Add source/domain credibility as a feature, not just headline text.
- Integrate with a real fact-checking API for verification, rather than relying on text patterns alone.
