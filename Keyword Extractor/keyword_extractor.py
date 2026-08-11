"""
Keyword/Topic Extractor
----------------------------
Extracts the most important keywords from a document using TF-IDF
scoring against a small built-in reference corpus (no external
downloads needed).

"""

from sklearn.feature_extraction.text import TfidfVectorizer

# A small generic background corpus so TF-IDF has something to compare against.
BACKGROUND_CORPUS = [
    "The weather today is sunny with a light breeze across the city.",
    "Stock markets rose slightly after the latest earnings reports.",
    "The recipe calls for flour, sugar, eggs, and a pinch of salt.",
    "Local schools announced a new schedule for the upcoming semester.",
    "The football match ended in a dramatic last-minute goal.",
    "Researchers published a new study on renewable energy sources.",
    "The museum's new exhibit features ancient artifacts from Egypt.",
    "Traffic was heavy on the highway due to ongoing construction.",
]


def extract_keywords(text, top_n=8):
    documents = BACKGROUND_CORPUS + [text]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    feature_names = vectorizer.get_feature_names_out()
    doc_vector = matrix[-1].toarray()[0]

    scored = list(zip(feature_names, doc_vector))
    scored = [pair for pair in scored if pair[1] > 0]
    scored.sort(key=lambda pair: pair[1], reverse=True)

    return [word for word, score in scored[:top_n]]


def main():
    print("Keyword/Topic Extractor (TF-IDF based)")
    print("Paste a paragraph of text (type 'quit' to exit).\n")

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue

        keywords = extract_keywords(text)
        if keywords:
            print(f"  Top keywords: {', '.join(keywords)}\n")
        else:
            print("  No strong keywords found — try a longer passage.\n")


if __name__ == "__main__":
    main()
