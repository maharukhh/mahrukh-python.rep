"""
Differential-Drive Robot Dynamics Simulator
==============================================
Models how independent left/right wheel velocities translate into robot
motion (position + heading) for a differential-drive robot — the base
kinematic model used to test and compare controllers (PID, pure pursuit,
LQR) elsewhere in this repo. Includes a few canonical motion primitives:
straight line, in-place rotation, and arc/turn.

"""

import matplotlib.pyplot as plt
import numpy as np


WHEEL_BASE = 0.4  # m, distance between the two wheels


def step(pose, v_left, v_right, dt):
    """
    pose: (x, y, theta). Returns the next pose given wheel velocities (m/s).
    """
    x, y, theta = pose
    v = (v_left + v_right) / 2
    omega = (v_right - v_left) / WHEEL_BASE
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += omega * dt
    return (x, y, theta)


def simulate(wheel_speed_fn, steps=300, dt=0.05, pose0=(0.0, 0.0, 0.0)):
    pose = pose0
    trajectory = [pose]
    for i in range(steps):
        t = i * dt
        v_left, v_right = wheel_speed_fn(t)
        pose = step(pose, v_left, v_right, dt)
        trajectory.append(pose)
    return np.array(trajectory)


def demo():
    maneuvers = {
        "straight line": lambda t: (0.5, 0.5),
        "in-place rotation": lambda t: (-0.3, 0.3),
        "arc turn (right wheel faster)": lambda t: (0.3, 0.6),
        "S-curve (oscillating differential)": lambda t: (0.4 - 0.15 * np.sin(t), 0.4 + 0.15 * np.sin(t)),
    }

    fig, axes = plt.subplots(2, 2, figsize=(11, 9))
    for ax, (name, fn) in zip(axes.flat, maneuvers.items()):
        traj = simulate(fn)
        ax.plot(traj[:, 0], traj[:, 1], color="steelblue", linewidth=2)
        ax.scatter(traj[0, 0], traj[0, 1], c="green", s=60, zorder=5, label="start")
        ax.scatter(traj[-1, 0], traj[-1, 1], c="red", s=60, zorder=5, label="end")
        # draw a heading arrow at the final pose (scaled to the trajectory's own extent
        # so it stays proportional even for near-stationary maneuvers like pure rotation)
        fx, fy, ftheta = traj[-1]
        span = max(np.ptp(traj[:, 0]), np.ptp(traj[:, 1]), 0.5)
        arrow_len = 0.15 * span
        ax.arrow(fx, fy, arrow_len * np.cos(ftheta), arrow_len * np.sin(ftheta),
                  head_width=0.05 * span, color="black")
        ax.set_title(name)
        ax.set_aspect("equal")
        cx, cy = traj[:, 0].mean(), traj[:, 1].mean()
        half = max(span, arrow_len * 2) * 0.75 + 0.2
        ax.set_xlim(cx - half, cx + half)
        ax.set_ylim(cy - half, cy + half)
        ax.legend(fontsize=7, loc="upper left")
        ax.grid(alpha=0.3)
        print(f"{name}: final pose x={fx:.2f}, y={fy:.2f}, theta={np.rad2deg(ftheta):.1f}°")

    plt.suptitle("Differential-Drive Kinematics — Canonical Maneuvers", fontsize=14)
    plt.tight_layout()
    plt.savefig("diff_drive_maneuvers.png", dpi=120)
    print("Saved visualization to diff_drive_maneuvers.png")
    plt.show()


if __name__ == "__main__":
    demo()
