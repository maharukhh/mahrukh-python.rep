Fake News Detection System
A simple machine learning project that detects whether a news article is FAKE or REAL using Python and NLP.

Tech Used
Python
Pandas
Scikit-learn
TF-IDF Vectorizer
Passive Aggressive Classifier

Dataset
Fake.csv → Fake news
True.csv → Real news
Must contain a text column

How to Run
pip install pandas scikit-learn
python fake news_detector.py

Working
Loads dataset
Converts text to features (TF-IDF)
Trains ML model
Predicts FAKE or REAL news
