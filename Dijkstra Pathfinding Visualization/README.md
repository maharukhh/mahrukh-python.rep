# Dijkstra Pathfinding Visualization

An interactive grid-based visualization of Dijkstra's shortest-path algorithm, built with Pygame. Place a start point, an end point, and walls, then watch the algorithm search the grid cell by cell and reveal the shortest path it finds.

## How It Works

1. **Grid representation** — The window is a grid of cells. Each cell is either open, a wall, the start, or the end.
2. **Search** — Dijkstra's algorithm explores outward from the start using a priority queue, always expanding the closest unvisited cell first, until it reaches the end (or exhausts all reachable cells).
3. **Animation** — Cells are colored as they're visited (blue) so you can watch the search frontier grow in real time.
4. **Path reconstruction** — Once the end is reached, the algorithm backtracks through parent pointers to draw the shortest path in yellow.

## Files

- `dijkstra_pathfinding.py` — the full app: grid/node setup, Dijkstra's algorithm, and the Pygame visualization loop.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python dijkstra_pathfinding.py
```

**Controls:**
| Action | Effect |
|---|---|
| Left click | Place start → then end → then walls |
| Right click | Erase a cell (wall, start, or end) |
| `SPACE` | Run Dijkstra's algorithm |
| `C` | Clear the entire grid |

## Notes & Limitations

- All edges have equal weight (moving to any open neighbor costs 1), so on an unweighted grid Dijkstra's algorithm behaves like Breadth-First Search — it's implemented as full Dijkstra (with a priority queue) so it's easy to extend to weighted terrain later.
- The grid size (`ROWS`, `COLS`) and cell size (`CELL`) are configurable constants at the top of the file.

## Possible Extensions

- Add weighted terrain (e.g., "mud" cells that cost more to cross) to make the priority queue's role visible.
- Add a side-by-side comparison mode against A* to show the difference in nodes explored.
- Add diagonal movement as an option.
