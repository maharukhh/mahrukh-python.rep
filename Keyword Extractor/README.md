# Keyword Extractor

Extracts the most important keywords from a document using TF-IDF scoring against a small built-in background corpus.

## How It Works
1. Your input text is combined with a small set of generic "background" sentences (about weather, sports, food, etc.) covering unrelated topics.
2. TF-IDF vectorization scores each word in your text by how frequent it is *in your text* relative to how common it is *across the background corpus* — words that are distinctive to your text score higher than generic/common words.
3. The highest-scoring words are returned as the extracted keywords.

## Requirements
- Python 3.x
- scikit-learn (`pip install scikit-learn`)

Paste a paragraph of text to see its top keywords. Type `quit` to exit.

## Notes & Limitations
- Keyword quality depends partly on the background corpus — a tiny 8-sentence corpus is used here for simplicity, so results are reasonable but not as refined as a system using a large reference corpus.
- Works best on paragraphs with enough distinctive vocabulary (very short inputs may not surface strong keywords).

## Possible Extensions
- Swap in a much larger background corpus (e.g. Wikipedia sample sentences) for more accurate scoring.
- Add multi-word keyphrase extraction (not just single words) using n-grams.
- Try the RAKE algorithm as an alternative extraction method.
