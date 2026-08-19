# Differential-Drive Robot Dynamics Simulator

A Python-based simulator for modeling how independent left and right wheel velocities control a differential-drive robot's **position and heading**. This is a fundamental kinematic model for mobile robots and provides the foundation for testing and comparing controllers such as PID, Pure Pursuit, and LQR.

The simulator saves:

```text
diff_drive_maneuvers.png
```

The visualization demonstrates four common maneuvers:

* Straight-line motion
* In-place rotation
* Arc turning
* S-curve motion using an oscillating wheel-speed difference

The final robot pose `(x, y, heading)` is also printed for each maneuver.

## How it works

The simulator uses standard **differential-drive kinematics**. Linear velocity is calculated from the average of the left and right wheel speeds, while angular velocity depends on their difference and the robot's wheelbase.

This motion model provides the foundation for other mobile-robot controller simulations in the repository.

## Concepts demonstrated

* Differential-Drive Kinematics
* Mobile Robot Motion Modeling
* Linear and Angular Velocity
* Wheel-Speed Control
* Robot Pose Tracking
* Controller Simulation

## Dependencies

```bash
pip install numpy matplotlib
```

* Python 3.x
* NumPy
* Matplotlib
