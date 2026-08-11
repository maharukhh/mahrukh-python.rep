"""
Fake News / Misinformation Detector (Educational Demo)
-------------------------------------------------------------
Classifies news headlines as "Likely Real" or "Likely Fake" using a
Naive Bayes classifier trained on a small built-in labeled toy dataset.

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

TRAIN_TEXTS = [
    "Scientists confirm new vaccine reduces hospitalization rates in trial",
    "Local government approves budget for new public transit line",
    "Central bank raises interest rates to combat inflation",
    "University researchers publish peer-reviewed study on climate change",
    "Company reports quarterly earnings in line with analyst expectations",
    "City council votes to fund new school infrastructure projects",
    "Doctors recommend regular exercise to reduce heart disease risk",
    "You won't believe this one weird trick doctors don't want you to know",
    "Secret government cover-up revealed shocking truth about aliens",
    "This miracle cure eliminates all diseases overnight, doctors furious",
    "Celebrity secretly replaced by clone, insider claims",
    "Drink this every morning to lose 20 pounds in one week guaranteed",
    "Shocking: scientists hiding the truth about flat earth for decades",
    "Billionaire reveals secret trick to make millions overnight for free",
]

TRAIN_LABELS = [
    "Likely Real", "Likely Real", "Likely Real", "Likely Real",
    "Likely Real", "Likely Real", "Likely Real",
    "Likely Fake", "Likely Fake", "Likely Fake", "Likely Fake",
    "Likely Fake", "Likely Fake", "Likely Fake",
]


def build_model():
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(TRAIN_TEXTS)
    model = MultinomialNB()
    model.fit(X, TRAIN_LABELS)
    return vectorizer, model


def classify(headline, vectorizer, model):
    X = vectorizer.transform([headline])
    prediction = model.predict(X)[0]
    confidence = max(model.predict_proba(X)[0])
    return prediction, confidence


def main():
    print("Fake News Detector (educational demo — see docstring for limitations)")
    print("Type a headline to classify it (type 'quit' to exit).\n")

    vectorizer, model = build_model()

    while True:
        headline = input("> ").strip()
        if headline.lower() == "quit":
            break
        if not headline:
            continue
        label, confidence = classify(headline, vectorizer, model)
        print(f"  Prediction: {label}  (confidence: {confidence:.2f})\n")


if __name__ == "__main__":
    main()
