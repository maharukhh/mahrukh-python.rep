"""
Sentiment Analysis Tool
-------------------------
A lexicon-based sentiment analyzer that classifies text as Positive,
Negative, or Neutral by scoring words against built-in positive/negative
word lists (no external downloads or API keys needed).

"""

import re

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "wonderful", "fantastic",
    "love", "happy", "best", "awesome", "brilliant", "positive", "nice",
    "beautiful", "perfect", "enjoy", "enjoyed", "enjoying", "pleased",
    "delight", "delighted", "fun", "glad", "impressive", "outstanding",
    "superb", "terrific", "recommend", "recommended", "helpful", "kind",
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "horrible", "worst", "hate", "sad",
    "angry", "annoying", "poor", "disappointing", "disappointed",
    "negative", "ugly", "boring", "waste", "broken", "fail", "failed",
    "failure", "problem", "issue", "sucks", "useless", "slow", "rude",
    "frustrating", "frustrated", "regret", "unhappy",
}

NEGATIONS = {"not", "no", "never", "n't", "cannot", "cant", "dont", "don't"}


def tokenize(text):
    return re.findall(r"[a-zA-Z']+", text.lower())


def analyze(text):
    tokens = tokenize(text)
    score = 0
    negate_next = False

    for i, word in enumerate(tokens):
        if word in NEGATIONS:
            negate_next = True
            continue

        word_score = 0
        if word in POSITIVE_WORDS:
            word_score = 1
        elif word in NEGATIVE_WORDS:
            word_score = -1

        if word_score != 0 and negate_next:
            word_score *= -1

        score += word_score
        negate_next = False

    if score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return label, score


def main():
    print("Sentiment Analysis Tool")
    print("Type a sentence and press Enter (type 'quit' to exit).\n")
    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue
        label, score = analyze(text)
        print(f"  Sentiment: {label}  (score: {score})\n")


if __name__ == "__main__":
    main()
