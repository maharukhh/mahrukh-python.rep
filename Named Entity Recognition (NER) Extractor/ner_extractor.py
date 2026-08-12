"""
Named Entity Recognition (NER) Extractor (Rule-Based)
----------------------------------------------------------
Extracts likely names, dates, organizations, and locations from text
using regex patterns and capitalization heuristics — no external model
downloads needed (a production system would typically use spaCy's
pretrained NER models instead, but this demonstrates the core approach
with zero dependencies).

"""

import re

MONTHS = (
    "january|february|march|april|may|june|july|august|"
    "september|october|november|december"
)

DATE_PATTERN = re.compile(
    rf"\b(\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}|(?:{MONTHS})\s+\d{{1,2}},?\s+\d{{4}}|\d{{1,2}}/\d{{1,2}}/\d{{2,4}})\b",
    re.IGNORECASE,
)

ORG_SUFFIXES = ("Inc", "Corp", "Corporation", "Ltd", "LLC", "Company", "Co", "Group", "University")

LOCATION_HINTS = {
    "city", "town", "county", "state", "country", "street", "avenue",
    "road", "province", "district",
}


def extract_dates(text):
    return DATE_PATTERN.findall(text)


def extract_capitalized_phrases(text):
    """Find sequences of consecutive capitalized words (candidate proper nouns)."""
    return re.findall(r"\b(?:[A-Z][a-zA-Z]*\s?){1,4}\b", text)


def classify_phrase(phrase):
    words = phrase.strip().split()
    if not words:
        return None

    if any(phrase.strip().endswith(suffix) for suffix in ORG_SUFFIXES):
        return "ORGANIZATION"
    if any(hint in phrase.lower() for hint in LOCATION_HINTS):
        return "LOCATION"
    if len(words) <= 3:
        return "PERSON/PLACE"  # ambiguous without a real model
    return None


def extract_entities(text):
    entities = {"DATE": [], "ORGANIZATION": [], "LOCATION": [], "PERSON/PLACE": []}

    for date in extract_dates(text):
        entities["DATE"].append(date)

    for phrase in extract_capitalized_phrases(text):
        phrase = phrase.strip()
        if len(phrase) < 2:
            continue
        label = classify_phrase(phrase)
        if label and phrase not in entities[label]:
            entities[label].append(phrase)

    return entities


def main():
    print("Named Entity Recognition (rule-based demo)")
    print("Paste or type a sentence/paragraph (type 'quit' to exit).\n")

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue

        entities = extract_entities(text)
        print()
        for label, items in entities.items():
            if items:
                print(f"  {label}: {', '.join(items)}")
        if not any(entities.values()):
            print("  No entities detected.")
        print()


if __name__ == "__main__":
    main()
