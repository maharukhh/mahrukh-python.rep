# Machine Translation Tool (Dictionary-Based Demo)

A simple word-for-word English ↔ Urdu translator using a built-in dictionary lookup — a lightweight, fully offline demonstration of the core idea behind lookup-based translation.

## How It Works
1. Input text is split into individual words.
2. Each word is looked up (case-insensitively, punctuation-stripped) in a built-in English→Urdu (or Urdu→English) dictionary.
3. Matched words are replaced with their translation; unmatched words are left as-is.
4. Words are rejoined into an output string.

## Requirements
- Python 3.x (standard library only — no installs needed)

Type `en` to translate English→Urdu, `ur` for Urdu→English, then type text to translate. Type `quit` to exit.

## Notes & Limitations
- This is a **word-by-word dictionary lookup**, not real machine translation — it doesn't handle grammar, word order, idioms, or context, and only recognizes the ~35 words in its built-in dictionary.
- Real machine translation systems (like Google Translate) use neural sequence-to-sequence models trained on millions of sentence pairs; this demo exists purely to illustrate the *concept* of lookup-based translation with zero dependencies.

## Possible Extensions
- Expand the dictionary significantly, or load it from a CSV/JSON file.
- Add more language pairs.
- Swap in a real translation API (e.g. Google Translate API) for actual accurate translation.
