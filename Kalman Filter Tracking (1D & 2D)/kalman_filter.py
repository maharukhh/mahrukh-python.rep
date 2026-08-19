"""
Kalman Filter for 1D/2D Position Tracking
==============================================
A from-scratch (no external filtering libraries) Kalman filter that fuses
noisy position measurements with a constant-velocity motion model to
produce a smoothed state estimate — the same core algorithm used for GPS
smoothing, sensor fusion, and object tracking on real robots.

Usage
-----
    python kalman_filter.py --task 1d
    python kalman_filter.py --task 2d
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np


class KalmanFilter:
    """Generic linear Kalman filter: state x, transition F, measurement H."""

    def __init__(self, F, H, Q, R, x0, P0):
        self.F = F  # state transition matrix
        self.H = H  # measurement matrix
        self.Q = Q  # process noise covariance
        self.R = R  # measurement noise covariance
        self.x = x0  # initial state estimate
        self.P = P0  # initial estimate covariance

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x

    def update(self, z):
        y = z - self.H @ self.x                       # innovation
        S = self.H @ self.P @ self.H.T + self.R        # innovation covariance
        K = self.P @ self.H.T @ np.linalg.inv(S)       # Kalman gain
        self.x = self.x + K @ y
        self.P = (np.eye(self.P.shape[0]) - K @ self.H) @ self.P
        return self.x


def demo_1d():
    rng = np.random.default_rng(1)
    n_steps = 60
    dt = 1.0
    true_velocity = 2.0
    true_pos = np.cumsum(np.full(n_steps, true_velocity)) - true_velocity
    measurement_noise_std = 4.0
    measurements = true_pos + rng.normal(0, measurement_noise_std, n_steps)

    F = np.array([[1, dt], [0, 1]])
    H = np.array([[1, 0]])
    Q = np.array([[0.05, 0], [0, 0.05]])
    R = np.array([[measurement_noise_std ** 2]])
    x0 = np.array([measurements[0], 0])
    P0 = np.eye(2) * 10

    kf = KalmanFilter(F, H, Q, R, x0, P0)
    estimates = []
    for z in measurements:
        kf.predict()
        est = kf.update(np.array([z]))
        estimates.append(est[0])
    estimates = np.array(estimates)

    rmse_measured = np.sqrt(np.mean((measurements - true_pos) ** 2))
    rmse_filtered = np.sqrt(np.mean((estimates - true_pos) ** 2))
    print(f"RMSE — raw measurements: {rmse_measured:.2f} | Kalman-filtered: {rmse_filtered:.2f}")

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(true_pos, label="true position", color="black", linewidth=2)
    ax.scatter(range(n_steps), measurements, color="red", s=15, alpha=0.5, label="noisy measurements")
    ax.plot(estimates, color="blue", linewidth=2, label="Kalman estimate")
    ax.set_title(f"1D Kalman Filter — RMSE reduced {rmse_measured:.2f} -> {rmse_filtered:.2f}")
    ax.set_xlabel("time step")
    ax.set_ylabel("position")
    ax.legend()
    plt.savefig("kalman_1d.png", dpi=120)
    print("Saved visualization to kalman_1d.png")
    plt.show()


def demo_2d():
    rng = np.random.default_rng(2)
    n_steps = 80
    dt = 1.0
    t = np.arange(n_steps)
    true_x = 0.5 * t
    true_y = 10 * np.sin(t / 10)

    measurement_noise_std = 3.0
    meas_x = true_x + rng.normal(0, measurement_noise_std, n_steps)
    meas_y = true_y + rng.normal(0, measurement_noise_std, n_steps)

    F = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    H = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0]])
    Q = np.eye(4) * 0.05
    R = np.eye(2) * (measurement_noise_std ** 2)
    x0 = np.array([meas_x[0], meas_y[0], 0, 0])
    P0 = np.eye(4) * 10

    kf = KalmanFilter(F, H, Q, R, x0, P0)
    est_x, est_y = [], []
    for zx, zy in zip(meas_x, meas_y):
        kf.predict()
        est = kf.update(np.array([zx, zy]))
        est_x.append(est[0])
        est_y.append(est[1])
    est_x, est_y = np.array(est_x), np.array(est_y)

    rmse_measured = np.sqrt(np.mean((meas_x - true_x) ** 2 + (meas_y - true_y) ** 2))
    rmse_filtered = np.sqrt(np.mean((est_x - true_x) ** 2 + (est_y - true_y) ** 2))
    print(f"RMSE — raw measurements: {rmse_measured:.2f} | Kalman-filtered: {rmse_filtered:.2f}")

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.plot(true_x, true_y, color="black", linewidth=2, label="true trajectory")
    ax.scatter(meas_x, meas_y, color="red", s=12, alpha=0.5, label="noisy GPS-like measurements")
    ax.plot(est_x, est_y, color="blue", linewidth=2, label="Kalman estimate")
    ax.set_title(f"2D Kalman Filter — RMSE reduced {rmse_measured:.2f} -> {rmse_filtered:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.axis("equal")
    plt.savefig("kalman_2d.png", dpi=120)
    print("Saved visualization to kalman_2d.png")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Kalman filter tracking demos")
    parser.add_argument("--task", choices=["1d", "2d"], required=True)
    args = parser.parse_args()
    demo_1d() if args.task == "1d" else demo_2d()


if __name__ == "__main__":
    main()
