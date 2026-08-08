"""
Machine Translation Tool (Dictionary-Based Demo)
----------------------------------------------------
A simple word-for-word English <-> Urdu translator using a built-in
dictionary. This is a lightweight educational demo (not a full
statistical/neural translator) — it shows the core idea of lookup-based
translation without needing internet access or an API key.

Usage:
  python machine_translation.py
"""

EN_TO_UR = {
    "hello": "ہیلو",
    "hi": "ہائے",
    "good": "اچھا",
    "morning": "صبح",
    "how": "کیسے",
    "are": "ہیں",
    "you": "آپ",
    "i": "میں",
    "am": "ہوں",
    "fine": "ٹھیک",
    "thank": "شکریہ",
    "thanks": "شکریہ",
    "yes": "جی ہاں",
    "no": "نہیں",
    "please": "براہ کرم",
    "sorry": "معذرت",
    "love": "محبت",
    "friend": "دوست",
    "food": "کھانا",
    "water": "پانی",
    "book": "کتاب",
    "school": "اسکول",
    "work": "کام",
    "today": "آج",
    "tomorrow": "کل",
    "yesterday": "گزشتہ کل",
    "name": "نام",
    "my": "میرا",
    "is": "ہے",
    "what": "کیا",
    "where": "کہاں",
    "why": "کیوں",
    "who": "کون",
}

UR_TO_EN = {v: k for k, v in EN_TO_UR.items()}


def translate(text, direction="en-ur"):
    words = text.strip().split()
    table = EN_TO_UR if direction == "en-ur" else UR_TO_EN

    translated = []
    for word in words:
        cleaned = word.lower().strip(".,!?")
        translated.append(table.get(cleaned, word))  # fall back to original word if unknown
    return " ".join(translated)


def main():
    print("Machine Translation Tool (English <-> Urdu, dictionary-based demo)")
    print("Commands: type 'en' to translate English->Urdu, 'ur' for Urdu->English, 'quit' to exit.\n")

    direction = "en-ur"
    print(f"Current direction: English -> Urdu")

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if text.lower() == "en":
            direction = "en-ur"
            print("Switched to: English -> Urdu")
            continue
        if text.lower() == "ur":
            direction = "ur-en"
            print("Switched to: Urdu -> English")
            continue
        if not text:
            continue
        print(f"  Translation: {translate(text, direction)}\n")


if __name__ == "__main__":
    main()
