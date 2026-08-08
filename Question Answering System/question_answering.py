"""
Question Answering System (Extractive, Retrieval-Based)
--------------------------------------------------------------
Given a passage of text and a question, finds and returns the sentence
from the passage most likely to contain the answer, using TF-IDF
similarity between the question and each sentence (no external model
downloads needed).

Requirements:
  pip install scikit-learn

Usage:
  python question_answering.py
"""

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SAMPLE_PASSAGE = """
The Great Wall of China is a series of fortifications that were built
across the historical northern borders of ancient Chinese states. It
was constructed to protect against invasions from various nomadic
groups. Construction began as early as the 7th century BC, with major
sections built during the Ming Dynasty between 1368 and 1644. The wall
stretches over 13,000 miles in total, including all its branches. It
is one of the most impressive architectural feats in human history and
attracts millions of tourists every year.
"""


def split_sentences(text):
    text = text.replace("\n", " ").strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if s.strip()]


def answer_question(passage, question):
    sentences = split_sentences(passage)
    if not sentences:
        return "No passage loaded."

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(sentences + [question])

    question_vector = vectors[-1]
    sentence_vectors = vectors[:-1]

    similarities = cosine_similarity(question_vector, sentence_vectors)[0]
    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score == 0:
        return "I couldn't find a relevant answer in the passage."
    return sentences[best_index]


def main():
    print("Question Answering System (extractive, TF-IDF based)")
    print("A sample passage about the Great Wall of China is loaded by default.")
    print("Type 'passage' to enter your own passage, or ask a question directly.")
    print("Type 'quit' to exit.\n")

    passage = SAMPLE_PASSAGE

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if text.lower() == "passage":
            print("Paste your passage (single line):")
            passage = input("Passage: ").strip() or SAMPLE_PASSAGE
            print("Passage updated.\n")
            continue
        if not text:
            continue

        answer = answer_question(passage, text)
        print(f"  Answer: {answer}\n")


if __name__ == "__main__":
    main()
