"""
Coverage Path Planning (Boustrophedon / Lawnmower Pattern)
==============================================
Generates a full-coverage sweep path over a 2D area with obstacles,
the pattern used by real cleaning robots, lawnmowing robots, and
agricultural spraying drones to guarantee every reachable cell is visited.

"""

import matplotlib.pyplot as plt
import numpy as np


def generate_area(rows=25, cols=35, seed=11):
    rng = np.random.default_rng(seed)
    grid = np.zeros((rows, cols), dtype=int)
    for _ in range(5):
        r, c = rng.integers(2, rows - 5), rng.integers(2, cols - 5)
        h, w = rng.integers(2, 4), rng.integers(2, 4)
        grid[r:r + h, c:c + w] = 1
    return grid


def boustrophedon_path(grid):
    """
    Sweeps row by row (like mowing a lawn), alternating direction each row
    so the path is continuous, skipping obstacle cells.
    """
    rows, cols = grid.shape
    path = []
    for r in range(rows):
        col_range = range(cols) if r % 2 == 0 else range(cols - 1, -1, -1)
        for c in col_range:
            if grid[r, c] == 0:
                path.append((r, c))
    return path


def coverage_stats(grid, path):
    free_cells = np.sum(grid == 0)
    covered = len(set(path))
    return covered, free_cells, 100 * covered / free_cells


def demo():
    grid = generate_area()
    path = boustrophedon_path(grid)
    covered, free_cells, pct = coverage_stats(grid, path)
    print(f"Coverage path: {len(path)} steps, {covered}/{free_cells} free cells covered ({pct:.1f}%)")

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(grid, cmap="Greys", alpha=0.8)
    path_arr = np.array(path)
    ax.plot(path_arr[:, 1], path_arr[:, 0], color="orange", linewidth=1.2, alpha=0.8)
    ax.scatter(path_arr[0, 1], path_arr[0, 0], c="green", s=90, label="start", zorder=5)
    ax.scatter(path_arr[-1, 1], path_arr[-1, 0], c="red", s=90, label="end", zorder=5)
    ax.set_title(f"Boustrophedon Coverage Path — {pct:.1f}% of free area covered")
    ax.legend(loc="upper right")
    plt.savefig("coverage_path.png", dpi=120)
    print("Saved visualization to coverage_path.png")
    plt.show()


if __name__ == "__main__":
    demo()
