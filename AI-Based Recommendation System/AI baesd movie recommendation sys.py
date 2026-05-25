# AI-Based Recommendation System

movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr. Bean", "Home Alone", "The Mask"],
    "horror": ["Conjuring", "Annabelle", "Insidious"],
    "sci-fi": ["Interstellar", "Inception", "Avatar"]
}

print("=== AI-Based Recommendation System ===")
print("Available Categories:")
print("Action, Comedy, Horror, Sci-Fi")

# convert input to lowercase
choice = input("\nEnter your favorite category: ").lower()

if choice in movies:
    print("\nRecommended Movies for You:")

    for movie in movies[choice]:
        print("-", movie)

else:
    print("\nSorry! Category not found.")

input("\nPress Enter to exit...")