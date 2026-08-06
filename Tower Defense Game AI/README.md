# Tower Defense Game AI

A tower defense game where enemies intelligently pathfind through a maze toward your base, automatically rerouting if you block their path with a tower, while your towers automatically target and shoot the nearest enemy in range.

## How It Works

1. **Enemy pathfinding** — Each enemy's route from the spawn point to your base is computed with Breadth-First Search across the grid, treating placed towers as obstacles.
2. **Dynamic rerouting** — Whenever you place a new tower, the game recomputes BFS paths for all currently-alive enemies from their current position, so they intelligently reroute around your new tower instead of walking through it.
3. **Placement validation** — You can't place a tower that would completely block every path from spawn to base — the game checks with BFS before allowing placement, so enemies always have a way through.
4. **Tower targeting** — Each tower scans all enemies within its range every frame and fires at the nearest one, on a cooldown timer.
5. **Waves & economy** — Enemies spawn in waves that grow in size and toughness over time. Defeating enemies and clearing waves earns gold, which you spend on more towers.

## Files

- `tower_defense_ai.py` — the full game: grid/maze logic, BFS pathfinding, tower targeting AI, wave spawning, and the Pygame game loop.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python tower_defense_ai.py
```

**Controls:**
| Action | Effect |
|---|---|
| Left click on grid | Place a tower (costs gold) |
| `SPACE` | Start the next wave early |
| `R` | Restart the game |

## Notes & Limitations

- You lose a life each time an enemy reaches your base; the game ends when lives reach zero.
- Grid size, tower cost/range/damage, and wave scaling are all configurable constants at the top of the file.
- All towers currently behave identically (same range, damage, fire rate) — there's no tower variety yet.

## Possible Extensions

- Add multiple tower types (e.g., slow towers, splash-damage towers) with different costs and stats.
- Add enemy variety (fast/weak vs. slow/tanky) that requires different tower strategies.
- Add a minimap or path preview showing the enemies' current route before you place a tower.
