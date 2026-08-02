# Snake Game with AI

A classic Snake game where an AI autopilot plays the game for you (or you can take manual control), routing the snake to the food using Breadth-First Search while avoiding its own body.

## How It Works

1. **Primary strategy — BFS to food** — Each frame, the AI runs a Breadth-First Search from the snake's head to the food, treating the snake's body (minus the tail, which will have moved by the time the head gets there) as obstacles. If a path exists, the AI takes the first step along it.
2. **Fallback strategy — flood fill** — If no path to the food currently exists (the snake would trap itself), the AI instead picks whichever legal move leaves it the most open space, calculated with a flood fill from each candidate move. This keeps the snake alive longer instead of driving it into a dead end.
3. **Manual mode** — You can turn the AI off at any time and steer with the arrow keys yourself.

## Files

- `snake_ai.py` — the full game: grid/food logic, the AI (BFS + flood-fill fallback), and the Pygame game loop.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python snake_ai.py
```

**Controls:**
| Action | Effect |
|---|---|
| `A` | Toggle AI control on/off |
| Arrow keys | Manual steering (only active when AI is off) |
| `R` | Restart the game |

## Notes & Limitations

- The AI plays close to optimally for simple boards but isn't guaranteed to survive indefinitely — as the snake grows very long, even a flood-fill-based fallback can eventually run out of safe space, same as a real player would.
- Grid size and game speed (`COLS`, `ROWS`, `FPS`) are configurable constants at the top of the file.

## Possible Extensions

- Add a Hamiltonian-cycle strategy for a near-guaranteed-safe (if slower) autopilot on any board size.
- Add a score/high-score display saved between runs.
- Add obstacles/walls in the middle of the board for extra challenge.
