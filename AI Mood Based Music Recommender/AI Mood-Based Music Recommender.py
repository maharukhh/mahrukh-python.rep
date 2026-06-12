import random

music = {
    "happy": [
        "Gallan Goodiyaan - Dil Dhadakne Do",
        "Badtameez Dil - Yeh Jawaani Hai Deewani",
        "Ude Dil Befikre - Befikre"
    ],
    "sad": [
        "Channa Mereya - Ae Dil Hai Mushkil",
        "Agar Tum Saath Ho - Tamasha",
        "Tujhe Bhula Diya - Anjaana Anjaani"
    ],
    "angry": [
        "Sadda Haq - Rockstar",
        "Zinda - Bhaag Milkha Bhaag",
        "Kar Har Maidaan Fateh - Sanju"
    ],
    "relaxed": [
        "Kun Faya Kun - Rockstar",
        "Iktara - Wake Up Sid",
        "Shaam - Aisha"
    ],
    "romantic": [
        "Tum Hi Ho - Aashiqui 2",
        "Raabta - Agent Vinod",
        "Pehla Nasha - Jo Jeeta Wohi Sikandar"
    
    ]
}

def recommend_music(mood):
    mood = mood.lower()

    if mood in music:
        song = random.choice(music[mood])
        print("Recommended song:", song)
    else:
        print("Mood not found.")
        print("Try: happy, sad, angry, relaxed, romantic")

print("AI Mood-Based Music Recommender")

while True:
    mood = input("\nEnter your mood or type exit: ")

    if mood.lower() == "exit":
        print("Goodbye!")
        break

    recommend_music(mood)