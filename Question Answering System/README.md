# Question Answering System (Extractive, Retrieval-Based)

Given a passage of text and a question, finds and returns the sentence from the passage most likely to contain the answer, using TF-IDF similarity between the question and each sentence.

## How It Works
1. The passage is split into individual sentences.
2. Both the question and every sentence are converted into TF-IDF vectors.
3. Cosine similarity is computed between the question vector and each sentence vector.
4. The sentence with the highest similarity score is returned as the "answer" — this is an **extractive** QA approach (it finds an existing sentence, rather than generating a new answer).

## Requirements
- Python 3.x
- scikit-learn (`pip install scikit-learn`)


A sample passage about the Great Wall of China is loaded by default. Ask a question directly, or type `passage` to load your own text first. Type `quit` to exit.

## Notes & Limitations
- This is **extractive** QA (it returns the most relevant existing sentence), not **generative** QA (it doesn't compose a new, precise answer from scattered facts).
- Because it relies on shared vocabulary between the question and the passage, it can miss answers phrased very differently from the question (e.g. synonyms it doesn't recognize).

## Possible Extensions
- Highlight the specific answer span within the returned sentence, not just the whole sentence.
- Add support for multiple passages/documents (a mini search engine).
- Swap in a transformer-based extractive QA model for more precise, span-level answers.
