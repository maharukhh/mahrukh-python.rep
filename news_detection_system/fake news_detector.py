import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score

print("Loading datasets...")

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = "FAKE"
true["label"] = "REAL"

data = pd.concat([fake, true])

# Shuffle data
data = data.sample(frac=1)

x = data["text"]
y = data["label"]

print("Splitting data...")

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("Converting text...")

vectorizer = TfidfVectorizer(stop_words="english")

x_train_vector = vectorizer.fit_transform(x_train)
x_test_vector = vectorizer.transform(x_test)

print("Training model...")

model = PassiveAggressiveClassifier(max_iter=1000)

model.fit(x_train_vector, y_train)

print("Testing accuracy...")

y_pred = model.predict(x_test_vector)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")

# User input
news = input("\nEnter news: ")

news_vector = vectorizer.transform([news])

result = model.predict(news_vector)

print("Prediction:", result[0])

input("Press Enter to exit...")