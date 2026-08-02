# Rock-Paper-Scissors Learning AI (GUI Version)

A desktop app version of the Rock-Paper-Scissors AI. It opens in its own window (built with Tkinter, included with Python — no extra installs needed) and learns to predict your next move as you play.

## How It Works

1. **Context window** — The AI looks at your last 2 moves as "context."
2. **Pattern learning** — For every context it has seen, it counts which move you played next, building a table like:
   ```
   (rock, paper) -> {scissors: 5, rock: 1, paper: 2}
   ```
3. **Prediction** — Before each round, it looks up the current context and predicts your most likely next move based on what you've done before in that situation.
4. **Counter-play** — It plays whatever move beats that prediction.
5. **Update** — After you move, it records the result and updates its pattern table.

If it hasn't seen enough history yet (or the current context is new), it falls back to a random move.

## Requirements

- Python 3.x (Tkinter ships with the standard Windows/Mac installers; on some Linux distros you may need `sudo apt install python3-tk`).

A window opens with three buttons: **Rock**, **Paper**, **Scissors**. Click one each round to play. The app shows:
- Both moves played that round
- The round result (win/lose/tie)
- A running score (You / AI / Ties)

Click **Reset Score** to clear the score and wipe the AI's learned patterns, starting fresh.

## Notes & Limitations

- The AI gets better against players with real habits (most people have subconscious patterns) — try repeating a pattern on purpose and watch it start countering you.
- Against a truly random player, it converges to roughly a 33% win rate, same as any strategy.
- Score and learned patterns reset when you close the app (nothing is saved between sessions) unless you extend it — see below.

## Possible Extensions

- Save/load learned patterns to a file so the AI remembers you across sessions.
- Show the AI's current prediction/confidence on screen before you move.
- Add difficulty levels (e.g., longer context length for a "hard" mode).
- Add sound effects or move animations.
