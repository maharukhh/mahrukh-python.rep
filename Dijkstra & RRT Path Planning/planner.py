"""
Dijkstra & RRT Path Planners
==============================================
Two motion-planning algorithms compared side by side:

  1. Dijkstra's algorithm  — optimal, grid-based, exhaustive search
  2. RRT (Rapidly-exploring Random Tree) — sampling-based, works in
     continuous space, the family of planner used by real robot
     motion-planning stacks (MoveIt, OMPL) for high-dimensional problems

Usage
-----
    python planner.py --task dijkstra
    python planner.py --task rrt
    python planner.py --task compare
"""

import argparse
import heapq

import matplotlib.pyplot as plt
import numpy as np


# --------------------------------------------------------------------------
# 1. Dijkstra's algorithm over a 2D occupancy grid
# --------------------------------------------------------------------------
def dijkstra(grid: np.ndarray, start: tuple, goal: tuple):
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows, cols = grid.shape

    dist = {start: 0.0}
    came_from = {}
    visited = set()
    pq = [(0.0, start)]

    while pq:
        d, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], visited

        for dr, dc in neighbors:
            neighbor = (current[0] + dr, current[1] + dc)
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue
            if grid[neighbor[0], neighbor[1]] == 1:
                continue
            step_cost = np.hypot(dr, dc)
            new_dist = d + step_cost
            if neighbor not in dist or new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                came_from[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    return None, visited


def make_grid():
    rng = np.random.default_rng(7)
    grid = np.zeros((30, 30), dtype=int)
    for _ in range(6):
        r, c = rng.integers(0, 25, size=2)
        h, w = rng.integers(3, 8, size=2)
        grid[r:r + h, c:c + w] = 1
    start, goal = (0, 0), (29, 29)
    grid[start], grid[goal] = 0, 0
    return grid, start, goal


def demo_dijkstra():
    grid, start, goal = make_grid()
    path, visited = dijkstra(grid, start, goal)
    if path is None:
        print("No path found.")
        return
    print(f"Dijkstra: path found with {len(path)} steps, {len(visited)} nodes explored.")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(grid, cmap="Greys")
    visited_arr = np.array(list(visited))
    ax.scatter(visited_arr[:, 1], visited_arr[:, 0], c="lightblue", s=6, label="explored")
    path_arr = np.array(path)
    ax.plot(path_arr[:, 1], path_arr[:, 0], color="red", linewidth=2, label="Dijkstra path")
    ax.scatter(*start[::-1], c="green", s=80, label="start")
    ax.scatter(*goal[::-1], c="blue", s=80, label="goal")
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title(f"Dijkstra's Algorithm ({len(visited)} nodes explored)")
    plt.savefig("dijkstra_path.png", dpi=120)
    print("Saved visualization to dijkstra_path.png")
    plt.show()


# --------------------------------------------------------------------------
# 2. RRT (Rapidly-exploring Random Tree) over continuous 2D space
# --------------------------------------------------------------------------
class RRTNode:
    __slots__ = ("point", "parent")

    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent


def collides(p1, p2, obstacles, steps=15):
    for t in np.linspace(0, 1, steps):
        x = p1[0] + t * (p2[0] - p1[0])
        y = p1[1] + t * (p2[1] - p1[1])
        for (ox, oy, r) in obstacles:
            if (x - ox) ** 2 + (y - oy) ** 2 <= r ** 2:
                return True
    return False


def rrt(start, goal, obstacles, bounds, max_iter=3000, step_size=2.0, goal_sample_rate=0.1, goal_radius=1.5):
    rng = np.random.default_rng(3)
    nodes = [RRTNode(np.array(start, dtype=float))]

    for _ in range(max_iter):
        if rng.random() < goal_sample_rate:
            sample = np.array(goal, dtype=float)
        else:
            sample = rng.uniform(bounds[0], bounds[1], size=2)

        nearest = min(nodes, key=lambda n: np.linalg.norm(n.point - sample))
        direction = sample - nearest.point
        dist = np.linalg.norm(direction)
        if dist < 1e-9:
            continue
        new_point = nearest.point + (direction / dist) * min(step_size, dist)

        if collides(nearest.point, new_point, obstacles):
            continue

        new_node = RRTNode(new_point, nearest)
        nodes.append(new_node)

        if np.linalg.norm(new_point - np.array(goal)) < goal_radius:
            goal_node = RRTNode(np.array(goal, dtype=float), new_node)
            nodes.append(goal_node)
            path = []
            n = goal_node
            while n is not None:
                path.append(n.point)
                n = n.parent
            return path[::-1], nodes

    return None, nodes


def make_rrt_scene():
    start, goal = (2, 2), (48, 48)
    bounds = (np.array([0, 0]), np.array([50, 50]))
    obstacles = [(15, 15, 6), (30, 30, 7), (35, 10, 5), (10, 35, 5), (25, 45, 4)]
    return start, goal, bounds, obstacles


def demo_rrt():
    start, goal, bounds, obstacles = make_rrt_scene()
    path, nodes = rrt(start, goal, obstacles, bounds)
    if path is None:
        print("RRT: no path found within iteration budget.")
        return
    print(f"RRT: path found using {len(nodes)} tree nodes, {len(path)} waypoints.")

    fig, ax = plt.subplots(figsize=(7, 7))
    for (ox, oy, r) in obstacles:
        ax.add_patch(plt.Circle((ox, oy), r, color="gray", alpha=0.6))
    for node in nodes:
        if node.parent is not None:
            ax.plot([node.point[0], node.parent.point[0]],
                     [node.point[1], node.parent.point[1]], color="lightblue", linewidth=0.6)
    path_arr = np.array(path)
    ax.plot(path_arr[:, 0], path_arr[:, 1], color="red", linewidth=2.5, label="RRT path")
    ax.scatter(*start, c="green", s=100, label="start", zorder=5)
    ax.scatter(*goal, c="blue", s=100, label="goal", zorder=5)
    ax.set_xlim(bounds[0][0], bounds[1][0])
    ax.set_ylim(bounds[0][1], bounds[1][1])
    ax.set_aspect("equal")
    ax.legend(loc="upper left", fontsize=8)
    ax.set_title(f"RRT Path Planning ({len(nodes)} tree nodes)")
    plt.savefig("rrt_path.png", dpi=120)
    print("Saved visualization to rrt_path.png")
    plt.show()


# --------------------------------------------------------------------------
# 3. Side-by-side comparison
# --------------------------------------------------------------------------
def path_length(path_arr: np.ndarray) -> float:
    """Total Euclidean length of a polyline given as an (N, 2) array."""
    diffs = np.diff(path_arr, axis=0)
    return float(np.hypot(diffs[:, 0], diffs[:, 1]).sum())


def demo_compare():
    """Runs Dijkstra and RRT on their own scenes and plots them side by
    side in one figure, printing a stats table so the trade-offs (nodes
    explored/sampled vs. path quality) are visible at a glance.

    Note: Dijkstra runs on a discrete grid and RRT runs in continuous
    space with circular obstacles, so this isn't literally the same map
    for both — it's a qualitative comparison of search behavior, not an
    apples-to-apples benchmark on identical input.
    """
    grid, d_start, d_goal = make_grid()
    d_path, d_visited = dijkstra(grid, d_start, d_goal)

    r_start, r_goal, bounds, obstacles = make_rrt_scene()
    r_path, r_nodes = rrt(r_start, r_goal, obstacles, bounds)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6.5))

    # --- Dijkstra panel ---
    ax1.imshow(grid, cmap="Greys")
    if d_visited:
        visited_arr = np.array(list(d_visited))
        ax1.scatter(visited_arr[:, 1], visited_arr[:, 0], c="lightblue", s=6, label="explored")
    if d_path is not None:
        d_path_arr = np.array(d_path)
        ax1.plot(d_path_arr[:, 1], d_path_arr[:, 0], color="red", linewidth=2, label="path")
        d_len = path_length(d_path_arr)
    else:
        d_len = None
    ax1.scatter(*d_start[::-1], c="green", s=80, label="start", zorder=5)
    ax1.scatter(*d_goal[::-1], c="blue", s=80, label="goal", zorder=5)
    ax1.legend(loc="upper left", fontsize=8)
    ax1.set_title(f"Dijkstra — {len(d_visited)} nodes explored")

    # --- RRT panel ---
    for (ox, oy, r) in obstacles:
        ax2.add_patch(plt.Circle((ox, oy), r, color="gray", alpha=0.6))
    for node in r_nodes:
        if node.parent is not None:
            ax2.plot([node.point[0], node.parent.point[0]],
                      [node.point[1], node.parent.point[1]], color="lightblue", linewidth=0.6)
    if r_path is not None:
        r_path_arr = np.array(r_path)
        ax2.plot(r_path_arr[:, 0], r_path_arr[:, 1], color="red", linewidth=2.5, label="path")
        r_len = path_length(r_path_arr)
    else:
        r_len = None
    ax2.scatter(*r_start, c="green", s=100, label="start", zorder=5)
    ax2.scatter(*r_goal, c="blue", s=100, label="goal", zorder=5)
    ax2.set_xlim(bounds[0][0], bounds[1][0])
    ax2.set_ylim(bounds[0][1], bounds[1][1])
    ax2.set_aspect("equal")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.set_title(f"RRT — {len(r_nodes)} tree nodes")

    fig.suptitle("Dijkstra (exhaustive, grid) vs RRT (sampling-based, continuous)")
    plt.tight_layout()
    plt.savefig("compare_path.png", dpi=120)
    print("Saved visualization to compare_path.png")

    print("\n--- Comparison summary ---")
    print(f"{'Planner':<10}{'Nodes':<12}{'Waypoints':<12}{'Path length':<14}")
    print(f"{'Dijkstra':<10}{len(d_visited):<12}{len(d_path) if d_path else 0:<12}"
          f"{f'{d_len:.2f}' if d_len is not None else 'N/A':<14}")
    print(f"{'RRT':<10}{len(r_nodes):<12}{len(r_path) if r_path else 0:<12}"
          f"{f'{r_len:.2f}' if r_len is not None else 'N/A':<14}")

    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Dijkstra vs RRT path planning demos")
    parser.add_argument("--task", choices=["dijkstra", "rrt", "compare"], required=True)
    args = parser.parse_args()

    if args.task == "dijkstra":
        demo_dijkstra()
    elif args.task == "rrt":
        demo_rrt()
    elif args.task == "compare":
        demo_compare()


if __name__ == "__main__":
    main()