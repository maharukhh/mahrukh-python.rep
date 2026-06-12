from datetime import datetime
from collections import Counter
import json
import os

DATA_FILE = "mood_entries.json"


class MoodEntry:
    def __init__(self, mood, note, stress_level, sleep_hours, timestamp=None):
        self.mood = mood.lower()
        self.note = note
        self.stress_level = stress_level
        self.sleep_hours = sleep_hours
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "mood": self.mood,
            "note": self.note,
            "stress_level": self.stress_level,
            "sleep_hours": self.sleep_hours,
            "timestamp": self.timestamp
        }


class MoodTracker:
    positive_words = ["happy", "calm", "good", "great", "hopeful", "relaxed", "excited"]
    negative_words = ["sad", "angry", "bad", "tired", "anxious", "stressed", "lonely"]

    def __init__(self):
        self.entries = self.load_entries()

    def load_entries(self):
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def save_entries(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.entries, file, indent=4)

    def add_entry(self):
        mood = input("How are you feeling today? ")
        note = input("Write a short note about your day: ")

        stress_level = int(input("Stress level from 1 to 10: "))
        sleep_hours = float(input("How many hours did you sleep? "))

        entry = MoodEntry(mood, note, stress_level, sleep_hours)
        self.entries.append(entry.to_dict())
        self.save_entries()

        print("\nMood entry saved.")
        print(self.get_ai_suggestion(entry.to_dict()))

    def analyze_sentiment(self, text):
        words = text.lower().split()

        positive_score = sum(1 for word in words if word in self.positive_words)
        negative_score = sum(1 for word in words if word in self.negative_words)

        if positive_score > negative_score:
            return "Positive"
        elif negative_score > positive_score:
            return "Negative"
        return "Neutral"

    def get_ai_suggestion(self, entry):
        sentiment = self.analyze_sentiment(entry["note"])

        if entry["stress_level"] >= 8:
            return "Suggestion: Your stress seems high. Try deep breathing, a short walk, or talking to someone you trust."

        if entry["sleep_hours"] < 6:
            return "Suggestion: You may need more rest. Consider reducing screen time before bed tonight."

        if sentiment == "Negative":
            return "Suggestion: Your note sounds a bit heavy. Try journaling more, taking a break, or reaching out for support."

        if sentiment == "Positive":
            return "Suggestion: Great to see a positive pattern. Notice what helped today and try to repeat it."

        return "Suggestion: Keep tracking your mood. Small patterns become clearer over time."

    def show_entries(self):
        if not self.entries:
            print("No mood entries found.")
            return

        for entry in self.entries:
            print("\n----------------------")
            print(f"Date: {entry['timestamp']}")
            print(f"Mood: {entry['mood']}")
            print(f"Stress Level: {entry['stress_level']}/10")
            print(f"Sleep: {entry['sleep_hours']} hours")
            print(f"Note: {entry['note']}")
            print(f"Sentiment: {self.analyze_sentiment(entry['note'])}")

    def mood_summary(self):
        if not self.entries:
            print("No data available for summary.")
            return

        moods = [entry["mood"] for entry in self.entries]
        stress_levels = [entry["stress_level"] for entry in self.entries]
        sleep_hours = [entry["sleep_hours"] for entry in self.entries]

        most_common_mood = Counter(moods).most_common(1)[0][0]
        average_stress = sum(stress_levels) / len(stress_levels)
        average_sleep = sum(sleep_hours) / len(sleep_hours)

        print("\nMood Summary")
        print("----------------------")
        print(f"Total entries: {len(self.entries)}")
        print(f"Most common mood: {most_common_mood}")
        print(f"Average stress level: {average_stress:.1f}/10")
        print(f"Average sleep hours: {average_sleep:.1f}")

        if average_stress >= 7:
            print("Trend: Stress has been high recently.")
        elif average_sleep < 6:
            print("Trend: Sleep may be affecting your mood.")
        else:
            print("Trend: Your mood patterns look fairly stable.")

    def menu(self):
        while True:
            print("\nAI Mental Health Mood Tracker")
            print("1. Add mood entry")
            print("2. View all entries")
            print("3. View mood summary")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.show_entries()
            elif choice == "3":
                self.mood_summary()
            elif choice == "4":
                print("Take care. Remember, tracking is helpful, but professional support matters too.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    tracker = MoodTracker()
    tracker.menu()