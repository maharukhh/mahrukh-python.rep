import random
import tkinter as tk
from collections import defaultdict

MOVES = ['rock', 'paper', 'scissors']
BEATS = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}  # what beats what
EMOJI = {'rock': '\u270a', 'paper': '\u270b', 'scissors': '\u270c\ufe0f'}


class RPSLearningAI:
    def __init__(self, history_length=2):
        self.history_length = history_length
        self.opponent_history = []
        self.pattern_counts = defaultdict(lambda: defaultdict(int))
        self.score = {'ai': 0, 'opponent': 0, 'ties': 0}

    def _get_context(self):
        if len(self.opponent_history) < self.history_length:
            return None
        return tuple(self.opponent_history[-self.history_length:])

    def predict_opponent_move(self):
        context = self._get_context()
        if context is None or context not in self.pattern_counts:
            return random.choice(MOVES)
        counts = self.pattern_counts[context]
        return max(counts, key=counts.get)

    def choose_move(self):
        predicted = self.predict_opponent_move()
        return BEATS[predicted]

    def learn(self, opponent_move):
        context = self._get_context()
        if context is not None:
            self.pattern_counts[context][opponent_move] += 1
        self.opponent_history.append(opponent_move)

    def play_round(self, opponent_move):
        ai_move = self.choose_move()
        result = self._judge(ai_move, opponent_move)
        self.learn(opponent_move)
        return ai_move, result

    def _judge(self, ai_move, opponent_move):
        if ai_move == opponent_move:
            self.score['ties'] += 1
            return 'tie'
        elif BEATS[opponent_move] == ai_move:
            self.score['ai'] += 1
            return 'ai_wins'
        else:
            self.score['opponent'] += 1
            return 'opponent_wins'


class RPSApp:
    def __init__(self, root):
        self.ai = RPSLearningAI(history_length=2)
        self.root = root
        root.title("Rock Paper Scissors — Learning AI")
        root.geometry("420x420")
        root.resizable(False, False)

        tk.Label(root, text="Rock, Paper, Scissors", font=("Segoe UI", 18, "bold")).pack(pady=(20, 5))
        tk.Label(root, text="The AI learns your patterns as you play.",
                 font=("Segoe UI", 10), fg="gray").pack(pady=(0, 15))

        self.result_var = tk.StringVar(value="Make your move!")
        tk.Label(root, textvariable=self.result_var, font=("Segoe UI", 14)).pack(pady=10)

        self.moves_var = tk.StringVar(value="")
        tk.Label(root, textvariable=self.moves_var, font=("Segoe UI", 28)).pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)
        for move in MOVES:
            tk.Button(
                btn_frame, text=f"{EMOJI[move]}\n{move.capitalize()}",
                font=("Segoe UI", 12), width=8, height=3,
                command=lambda m=move: self.play(m)
            ).pack(side=tk.LEFT, padx=8)

        self.score_var = tk.StringVar(value="You: 0   AI: 0   Ties: 0")
        tk.Label(root, textvariable=self.score_var, font=("Segoe UI", 12, "bold")).pack(pady=(20, 5))

        tk.Button(root, text="Reset Score", command=self.reset).pack(pady=5)

    def play(self, user_move):
        ai_move, result = self.ai.play_round(user_move)
        self.moves_var.set(f"You: {EMOJI[user_move]}      AI: {EMOJI[ai_move]}")

        if result == 'tie':
            self.result_var.set("It's a tie!")
        elif result == 'ai_wins':
            self.result_var.set("AI wins this round!")
        else:
            self.result_var.set("You win this round!")

        s = self.ai.score
        self.score_var.set(f"You: {s['opponent']}   AI: {s['ai']}   Ties: {s['ties']}")

    def reset(self):
        self.ai = RPSLearningAI(history_length=2)
        self.result_var.set("Make your move!")
        self.moves_var.set("")
        self.score_var.set("You: 0   AI: 0   Ties: 0")


if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()