from difflib import get_close_matches

words = [
    "python", "computer", "science", "artificial",
    "intelligence", "machine", "learning",
    "student", "project", "university"
]

print("=== AI Autocorrect Tool ===")

word = input("Enter a word: ").lower()

suggestion = get_close_matches(word, words, n=1)

if suggestion:
    print("Did you mean:", suggestion[0], "?")
else:
    print("No suggestion found.")

input("\nPress Enter to exit...")