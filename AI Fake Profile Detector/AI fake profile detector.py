print("=== Fake Profile Detector ===")

followers = int(input("Enter number of followers: "))
following = int(input("Enter number of following: "))
posts = int(input("Enter number of posts: "))
account_age = int(input("Enter account age (months): "))

score = 0

# Simple detection rules
if followers < 50:
    score += 1

if following > 1000:
    score += 1

if posts < 5:
    score += 1

if account_age < 3:
    score += 1

print("\nAnalysis Result:")

if score >= 3:
    print("⚠️ Profile is likely FAKE")
else:
    print("✅ Profile appears REAL")

input("\nPress Enter to exit...")