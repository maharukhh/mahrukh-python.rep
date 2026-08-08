# AI Story Generator (Markov Chain)

Generates original, semi-coherent short text (story-style by default, but works on any source text) by learning word-transition probabilities from a source text using a Markov chain.

## How It Works
1. The source text is broken into overlapping word sequences of a fixed length ("order" — 2 words by default), each mapped to the word that follows it in the source.
2. To generate new text, the process starts from a random position in the source, then repeatedly looks up "what word tends to follow this pair of words?" and picks one at random from the learned options.
3. This produces text that mimics the *style and local word patterns* of the source, without simply copying it verbatim, though it doesn't understand meaning or long-range coherence.

## Files
- `story_generator.py` — the Markov chain builder, text generator, a default sample story, and an interactive CLI loop.

## Requirements
- Python 3.x (standard library only — no installs needed)


## Notes & Limitations
- Generated text can wander or lose coherence over longer passages — Markov chains only "remember" the last few words, not the overall plot or meaning.
- Output quality depends heavily on the source text: longer, richer source text produces more varied and interesting generated text; short source text tends to just loop back on itself.

## Possible Extensions
- Let the user adjust the Markov chain "order" (higher = more coherent but less creative, lower = more creative but less coherent).
- Add poem-specific formatting (line breaks, rhyme-aware word choice).
- Swap in a real LLM API call for genuinely coherent, meaningful generated text.
