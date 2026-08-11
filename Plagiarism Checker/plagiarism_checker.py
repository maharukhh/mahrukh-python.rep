"""
Plagiarism / Text Similarity Checker
------------------------------------------
Compares two pieces of text and reports a similarity score using
TF-IDF vectors and cosine similarity — a common baseline technique for
detecting near-duplicate or paraphrased text.

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(text_a, text_b):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([text_a, text_b])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity


def interpret(similarity):
    if similarity > 0.8:
        return "Very high similarity — likely copied or near-identical"
    elif similarity > 0.5:
        return "Moderate similarity — possibly paraphrased"
    elif similarity > 0.2:
        return "Low similarity — some shared topic/wording"
    else:
        return "Very low similarity — largely different content"


def main():
    print("Plagiarism / Text Similarity Checker")
    print("Enter two texts to compare.\n")

    while True:
        text_a = input("Text A (or 'quit' to exit): ").strip()
        if text_a.lower() == "quit":
            break
        text_b = input("Text B: ").strip()
        if not text_a or not text_b:
            print("Both texts are required.\n")
            continue

        similarity = compute_similarity(text_a, text_b)
        print(f"\n  Similarity score: {similarity:.2f} (0 = completely different, 1 = identical)")
        print(f"  Interpretation: {interpret(similarity)}\n")


if __name__ == "__main__":
    main()
