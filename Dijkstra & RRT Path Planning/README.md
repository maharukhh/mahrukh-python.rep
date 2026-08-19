# Dijkstra & RRT Path Planning

Two classic motion-planning algorithms implemented from scratch and compared on different planning problems. The project demonstrates the contrast between **deterministic grid-based search** and **sampling-based motion planning**.

## What's here

* **Dijkstra's Algorithm** — An exhaustive grid-based search that guarantees the shortest path in a weighted graph with non-negative costs.
* **RRT (Rapidly-exploring Random Tree)** — A sampling-based planner that explores continuous space by randomly sampling points and extending the tree toward them.
* **Comparison Mode** — Runs both planners on the same environment and visualizes their resulting paths, allowing direct comparison of path length, explored nodes, and planning behavior.

## Run it

```bash
python planner.py --task dijkstra
python planner.py --task rrt
python planner.py --task compare
```

Each task saves a visualization:

```text
dijkstra_path.png
rrt_path.png
compare_path.png
```

The program also prints the resulting path length and number of nodes explored.

## Why both

Dijkstra provides an exact shortest-path solution on a discrete grid but becomes less practical as the search space grows.

RRT does not guarantee the shortest path, but its sampling-based approach makes it suitable for **continuous and high-dimensional configuration spaces**, which are common in real-world robotic motion planning.

## Concepts demonstrated

* Graph-Based Path Planning
* Dijkstra's Algorithm
* Rapidly-exploring Random Trees (RRT)
* Grid-Based Search
* Sampling-Based Planning
* Obstacle Avoidance
* Path-Length and Search-Efficiency Analysis

## Dependencies

```bash
pip install numpy matplotlib
```

* Python 3.x
* NumPy
* Matplotlib
