# Plagiarism Checker

Compares two pieces of text and reports a similarity score (0 to 1) using TF-IDF vectors and cosine similarity — a common baseline technique for detecting near-duplicate or paraphrased text.

## How It Works
1. Both input texts are converted into TF-IDF vectors (numerical representations weighting distinctive words).
2. Cosine similarity is computed between the two vectors, producing a score from 0 (completely different) to 1 (identical).
3. The score is translated into a plain-language interpretation (very high / moderate / low / very low similarity).

## Requirements
- Python 3.x
- scikit-learn (`pip install scikit-learn`)

Enter Text A, then Text B, to see their similarity score. Type `quit` to exit.

## Notes & Limitations
- TF-IDF + cosine similarity catches word-overlap-based similarity well, but can miss cleverly paraphrased plagiarism that uses entirely different wording for the same ideas (it measures word usage overlap, not deep semantic meaning).
- For semantic (meaning-based) similarity rather than word-overlap similarity, sentence embedding models perform noticeably better.

## Possible Extensions
- Swap in sentence embeddings (e.g. via `sentence-transformers`) for meaning-based rather than word-overlap-based similarity.
- Add support for comparing entire documents/files rather than pasted text.
- Highlight the specific overlapping phrases between the two texts.
