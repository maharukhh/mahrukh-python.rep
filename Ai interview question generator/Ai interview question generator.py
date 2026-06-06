questions = {
    "python": [
        "What is the difference between a list and a tuple?",
        "Explain OOP concepts in Python.",
        "What are Python decorators?",
        "What is the difference between deep copy and shallow copy?",
        "How do you handle exceptions in Python?"
    ],

    "data science": [
        "What is machine learning?",
        "Explain supervised and unsupervised learning.",
        "What is overfitting?",
        "What is the difference between mean and median?",
        "What libraries do you use for data analysis?"
    ],

    "web developer": [
        "What is HTML?",
        "What is the difference between GET and POST?",
        "Explain CSS Flexbox.",
        "What is JavaScript used for?",
        "What is a responsive website?"
    ]
}

print("=== AI Interview Question Generator ===")
role = input("Enter job role (Python/Data Science/Web Developer): ").lower()

if role in questions:
    print("\nGenerated Interview Questions:\n")

    for i, question in enumerate(questions[role], start=1):
        print(f"{i}. {question}")

else:
    print("\nRole not found!")
    print("Available roles:")
    for r in questions:
        print("-", r.title())

input("\nPress Enter to exit...")