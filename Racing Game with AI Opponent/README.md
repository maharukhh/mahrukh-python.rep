# Racing Game with AI Opponent

A top-down racing game where you compete against an AI-controlled car around an oval track. The AI steers toward a sequence of waypoints and adjusts its speed for turns, so it drives the track competently without any hardcoded path.

## How It Works

1. **Track as waypoints** — The oval track is defined as a ring of waypoints spaced evenly around an ellipse.
2. **AI steering** — Each frame, the AI computes the angle from its current position to its next target waypoint and turns toward it at a fixed turn rate, advancing to the next waypoint once it gets close enough.
3. **AI speed control** — The AI slows down proportionally to how sharp the upcoming turn is (a large heading difference to the target means a tighter turn) and speeds back up on straights, so it doesn't spin out or crawl on straightaways.
4. **Player physics** — You accelerate, brake, and steer with simple friction-based physics — steering only takes effect above a minimum speed, like a real car.
5. **Race logic** — Both cars track which waypoint they're heading to and how many full laps they've completed; first to the lap target wins.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python racing_game_ai.py
```

**Controls:**
| Action | Effect |
|---|---|
| `UP` | Accelerate |
| `DOWN` | Brake / reverse |
| `LEFT` / `RIGHT` | Steer |
| `R` | Restart the race |

## Notes & Limitations

- The track shape, number of waypoints, and lap target (`TRACK_A`, `TRACK_B`, `NUM_WAYPOINTS`, `laps_to_win`) are configurable in the file.
- The AI doesn't detect or avoid the player's car — it drives its own line regardless of where you are, so no collisions between cars occur, only against the general race logic.

## Possible Extensions

- Add car-to-car collision so races feel more competitive.
- Add multiple track layouts to choose from.
- Give the AI a difficulty setting (turn rate, max speed) for easy/medium/hard modes.
