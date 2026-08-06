# 3D Game Simulation (basic)

A minimal 3D engine built entirely from scratch with Pygame — no 3D library or game engine involved. It renders wireframe cubes in 3D space and lets you fly a first-person camera through the scene, using hand-written vector math and perspective projection.

## How It Works

1. **3D scene** — A field of cubes is defined as sets of 3D vertices (corner points) and edges (which vertices connect to which), laid out in a grid pattern in world space.
2. **Camera transform** — Every frame, each vertex's world position is converted into camera space: first translated relative to the camera's position, then rotated by the camera's yaw (left/right look direction), using standard rotation math.
3. **Perspective projection** — Camera-space 3D points are projected onto the 2D screen using a simple pinhole-camera formula (`screen_position = focal_length / depth`), which is what makes farther objects appear smaller — the same principle behind real perspective and most 3D engines' projection stage.
4. **Rendering** — Only the projected 2D edges are drawn (as lines), giving each cube its wireframe look. Points behind the camera are skipped so they don't get drawn incorrectly.
5. **Free camera movement** — The camera can move forward/back and strafe left/right relative to its current facing direction, move up/down, and rotate — a basic first-person "fly" camera.

## Files

- `basic_3d_simulation.py` — the full program: cube generation, the camera class (transform + projection), and the Pygame render loop.

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## Usage

```bash
pip install pygame
python basic_3d_simulation.py
```

**Controls:**
| Action | Effect |
|---|---|
| `W` / `S` | Move forward / backward |
| `A` / `D` | Strafe left / right |
| `UP` / `DOWN` | Move camera up / down |
| `LEFT` / `RIGHT` | Rotate camera (look left/right) |
| `R` | Reset camera to starting position |

## Notes & Limitations

- This is a wireframe-only renderer — there's no solid-face rendering, lighting, or texturing, since the goal is to demonstrate the underlying 3D math rather than build a full engine.
- Camera pitch (looking up/down) isn't implemented — only yaw (turning left/right) and vertical position movement.
- The scene layout, cube size, and field of view (`FOV`) are configurable constants at the top of the file.

## Possible Extensions

- Add camera pitch for full look-around freedom.
- Add solid face rendering with simple back-face culling and flat shading.
- Add collision detection so the camera can't fly through cubes.
