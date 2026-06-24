languages = {
    "Spanish": {
        "Hola": "Hello",
        "Gracias": "Thank You",
        "Adios": "Goodbye"
    },
    "French": {
        "Bonjour": "Hello",
        "Merci": "Thank You",
        "Au revoir": "Goodbye"
    }
}

print("=== AI-Based Language Learning App ===")

print("\nAvailable Languages:")
for lang in languages:
    print("-", lang)

choice = input("\nChoose a language: ")

if choice in languages:
    print(f"\nLearning {choice}...\n")

    score = 0

    for word, meaning in languages[choice].items():
        print(f"What is the meaning of '{word}'?")
        answer = input("Your Answer: ")

        if answer.lower() == meaning.lower():
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong! ❌ Correct Answer: {meaning}\n")

    print("Quiz Finished!")
    print("Score:", score, "/", len(languages[choice]))

    if score == len(languages[choice]):
        print("AI Feedback: Excellent! 🌟")
    elif score >= 2:
        print("AI Feedback: Good Job! Keep Practicing 👍")
    else:
        print("AI Feedback: Practice More 📚")

else:
    print("Language not available.")

input("Press Enter to exit...")