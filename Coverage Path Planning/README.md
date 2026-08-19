# Coverage Path Planning (Boustrophedon Pattern)

A Python-based coverage path planning project that generates a full-area sweep path over a 2D environment containing obstacles. It demonstrates the **boustrophedon (lawnmower) pattern** commonly used in cleaning robots, agricultural robots, and autonomous drones.

The program prints the total path length and percentage of free space covered, and saves the visualization as:

```text
coverage_path.png
```

## How it works

The environment is traversed row by row, alternating between left-to-right and right-to-left movement to create an efficient back-and-forth sweep pattern.

Cells occupied by obstacles are skipped, allowing the planner to cover the reachable free space while navigating around blocked areas.

## Concepts demonstrated

* Coverage Path Planning
* Boustrophedon / Lawn-mower Pattern
* Obstacle-Aware Navigation
* Grid-Based Path Planning
* Coverage and Path-Length Analysis
* Autonomous Robot Navigation

## Dependencies

```bash
pip install numpy matplotlib
```

* Python 3.x
* NumPy
* Matplotlib
