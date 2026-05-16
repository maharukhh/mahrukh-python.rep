spam_words = ["win", "free", "prize", "money", "click", "offer"]

email = input("Enter email message: ")

email = email.lower()

is_spam = False

for word in spam_words:
    if word in email:
        is_spam = True
        break

if is_spam:
    print("This is a SPAM email")
else:
    print("This is NOT a spam email")