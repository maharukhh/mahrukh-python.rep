# Text Classification Tool

Classifies short text snippets into one of four categories — Sports, Technology, Politics, Entertainment — using a Naive Bayes classifier trained on a small built-in labeled dataset.

## How It Works
1. A small set of example sentences, each labeled with its category, is defined directly in the script.
2. Text is converted into TF-IDF vectors (numerical representations weighting important words).
3. A Multinomial Naive Bayes classifier is trained on these vectors and labels.
4. New text you type is vectorized the same way and classified, with a confidence score from the model's predicted probabilities.

## Files
- `text_classification.py` — training data, TF-IDF + Naive Bayes pipeline, and an interactive CLI loop.

## Requirements
- Python 3.x
- scikit-learn (`pip install scikit-learn`)


Type any sentence to see its predicted category and confidence. Type `quit` to exit.

## Notes & Limitations
- The training set is intentionally tiny (16 examples) for a self-contained demo — real-world classification needs a much larger, more diverse labeled dataset to generalize well.
- Confidence scores reflect the model's certainty given its limited training data, not real-world accuracy.

## Possible Extensions
- Load a larger labeled dataset (e.g. a news headlines CSV) instead of the hardcoded examples.
- Add more categories.
- Try a different classifier (Logistic Regression, SVM) and compare performance.
