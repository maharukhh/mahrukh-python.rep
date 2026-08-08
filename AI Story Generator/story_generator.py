"""
AI Story/Poem Generator (Markov Chain)
--------------------------------------------
Generates original, semi-coherent short text (story-style or poem-style)
by learning word-transition probabilities from a source text using a
Markov chain — a classic, fully offline text-generation technique with
no external model downloads needed.

Usage:
  python story_generator.py
"""

import random
import re

DEFAULT_SOURCE = """
Once upon a time, in a quiet village surrounded by tall mountains, there
lived a young inventor named Mira. Mira loved building strange machines
out of scrap metal and old clocks. Every night, she would climb to the
rooftop and watch the stars, dreaming of a machine that could fly. One
evening, a shooting star fell near the old oak tree at the edge of the
village. Mira ran through the dark forest, her lantern swinging wildly,
until she found a strange glowing stone. She carried it home and began
to build. Weeks passed, and the villagers whispered about the strange
sounds coming from her workshop. Finally, on a cold winter night, Mira's
machine roared to life, lifting her high above the mountains, past the
clouds, toward the stars she had always dreamed of reaching.
"""


def build_markov_chain(text, order=2):
    words = re.findall(r"\S+", text)
    chain = {}
    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        next_word = words[i + order]
        chain.setdefault(key, []).append(next_word)
    return chain, words


def generate_text(chain, words, order=2, length=80):
    if not chain:
        return ""

    start_index = random.randint(0, len(words) - order - 1)
    current = tuple(words[start_index:start_index + order])
    result = list(current)

    for _ in range(length - order):
        options = chain.get(current)
        if not options:
            # jump to a new random starting key to keep generating
            current = random.choice(list(chain.keys()))
            options = chain.get(current, [])
            if not options:
                break
        next_word = random.choice(options)
        result.append(next_word)
        current = tuple(result[-order:])

    return " ".join(result)


def main():
    print("AI Story/Poem Generator (Markov chain, offline)")
    print("A default short-story source text is loaded.")
    print("Type 'source' to paste your own source text, or 'generate' to create new text.")
    print("Type 'quit' to exit.\n")

    source_text = DEFAULT_SOURCE
    order = 2

    while True:
        command = input("> ").strip()
        if command.lower() == "quit":
            break
        if command.lower() == "source":
            print("Paste your source text (single line):")
            new_text = input("Source: ").strip()
            if new_text:
                source_text = new_text
                print("Source text updated.\n")
            continue
        if command.lower() == "generate":
            length = 80
            chain, words = build_markov_chain(source_text, order=order)
            generated = generate_text(chain, words, order=order, length=length)
            print(f"\n{generated}\n")
            continue

        print("Unknown command. Type 'source', 'generate', or 'quit'.\n")


if __name__ == "__main__":
    main()
