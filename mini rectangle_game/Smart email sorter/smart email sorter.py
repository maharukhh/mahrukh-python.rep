print("=== Smart Email Sorter ===")

email = input("Enter email subject or content: ").lower()

if any(word in email for word in ["meeting", "project", "office", "deadline"]):
    category = "Work"

elif any(word in email for word in ["sale", "discount", "offer", "buy now"]):
    category = "Promotions"

elif any(word in email for word in ["friend", "party", "birthday", "invitation"]):
    category = "Social"

elif any(word in email for word in ["win money", "lottery", "free cash", "click here"]):
    category = "Spam"

else:
    category = "General"

print("\nEmail Category:", category)

input("\nPress Enter to exit...")