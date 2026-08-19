# Kalman Filter Tracking (1D & 2D)

A Python-based implementation of a **Kalman Filter built from scratch** using NumPy linear algebra. The project combines noisy position measurements with a constant-velocity motion model to produce a smoother and more accurate estimate of an object's true position.

## Run it

```bash
python kalman_filter.py --task 1d
python kalman_filter.py --task 2d
```

Both modes calculate and print the **RMSE (Root Mean Square Error)** for the raw measurements and filtered estimates, and save a visualization comparing the true trajectory, noisy measurements, and Kalman-filtered estimate.

## How it works

The filter operates through two repeating steps:

1. **Predict** — Estimates the next state using the motion model.
2. **Update** — Corrects the prediction using the latest measurement and the **Kalman Gain**, which balances confidence between the model and sensor data.

This predict-update cycle is a fundamental technique used in **sensor fusion, GPS smoothing, object tracking, and autonomous robotics**.

## Concepts demonstrated

* Kalman Filtering
* 1D and 2D State Estimation
* Sensor Noise Reduction
* Constant-Velocity Motion Models
* Prediction and Measurement Updates
* Kalman Gain
* RMSE-Based Performance Evaluation
* Sensor Fusion Fundamentals

## Dependencies

```bash
pip install numpy matplotlib
```

* Python 3.x
* NumPy
* Matplotlib
