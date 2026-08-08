"""
Text Classification Tool
----------------------------
Classifies short text snippets into categories (Sports, Technology,
Politics, Entertainment) using a Naive Bayes classifier trained on a
small built-in labeled dataset (no external downloads needed).

Requirements:
  pip install scikit-learn

Usage:
  python text_classification.py
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

TRAIN_TEXTS = [
    "The team won the championship game last night in overtime",
    "The striker scored a hat trick in the football match",
    "Basketball playoffs are heating up this season",
    "The coach announced a new training regimen for the players",
    "A new smartphone was released with a faster processor",
    "Scientists developed a new AI model for image recognition",
    "The startup launched a new app for productivity",
    "Engineers unveiled a breakthrough in battery technology",
    "The senator proposed a new bill on healthcare reform",
    "Elections results show a close race between the candidates",
    "The government announced new economic policies today",
    "Parliament debated the new immigration law for hours",
    "The movie premiere attracted celebrities from around the world",
    "A popular singer released a surprise new album",
    "The award show celebrated the best films of the year",
    "The actor discussed his upcoming role in a new blockbuster",
]

TRAIN_LABELS = [
    "Sports", "Sports", "Sports", "Sports",
    "Technology", "Technology", "Technology", "Technology",
    "Politics", "Politics", "Politics", "Politics",
    "Entertainment", "Entertainment", "Entertainment", "Entertainment",
]


def build_model():
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(TRAIN_TEXTS)
    model = MultinomialNB()
    model.fit(X, TRAIN_LABELS)
    return vectorizer, model


def classify(text, vectorizer, model):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    confidence = max(probabilities)
    return prediction, confidence


def main():
    print("Text Classification Tool")
    print("Categories: Sports, Technology, Politics, Entertainment")
    print("Type a sentence to classify it (type 'quit' to exit).\n")

    vectorizer, model = build_model()

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue
        label, confidence = classify(text, vectorizer, model)
        print(f"  Predicted category: {label}  (confidence: {confidence:.2f})\n")


if __name__ == "__main__":
    main()
