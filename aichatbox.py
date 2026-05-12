import random

print("====================================")
print("      AI CHATBOT PROJECT")
print("====================================")
print("Type 'bye' to exit")

responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "hi": ["Hello!", "Hi!", "Greetings!"],
    "how are you": [
        "I am fine.",
        "Doing great!",
        "I am good, thank you!"
    ],
    "name": ["I am an AI Chatbot."],
    "help": ["I can answer simple questions."],
    "bye": ["Goodbye!", "See you later!"]
}

while True:

    # User input
    user_input = input("You: ").lower()

    # Exit condition
    if user_input == "bye":
        print("Bot:", random.choice(responses["bye"]))
        break

    found = False

    for key in responses:
        if key in user_input:
            print("Bot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("Bot: Sorry, I do not understand.")