# NLP Text Summarizer

from collections import Counter
import re

text = input("Enter a paragraph:\n")

# Split text into sentences
sentences = re.split(r'(?<=[.!?]) +', text)

# Count word frequencies
words = re.findall(r'\w+', text.lower())
word_freq = Counter(words)

# Score each sentence
sentence_scores = {}

for sentence in sentences:
    score = 0
    for word in re.findall(r'\w+', sentence.lower()):
        score += word_freq[word]
    sentence_scores[sentence] = score

# Get top 2 sentences
summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

print("\n=== Summary ===")
for sentence in summary:
    print(sentence)
    
input("\nPress Enter to exit...")