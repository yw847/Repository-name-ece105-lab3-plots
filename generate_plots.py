"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps
# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot scatter of sensor readings over time.

    Parameters
    ----------
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray
    timestamps : numpy.ndarray
    ax : matplotlib.axes.Axes

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, label="Sensor A", alpha=0.6)
    ax.scatter(timestamps, sensor_b, label="Sensor B", alpha=0.6)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Scatter Plot")

    ax.legend()
    ax.grid(True, alpha=0.3)
def plot_histogram(sensor_a, sensor_b, ax):
    """Plot histogram of sensor readings.

    Parameters
    ----------
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray
    ax : matplotlib.axes.Axes

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=20, alpha=0.5, label="Sensor A")
    ax.hist(sensor_b, bins=20, alpha=0.5, label="Sensor B")

    ax.set_title("Histogram")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")

    ax.legend()
    ax.grid(True, alpha=0.3)
def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot boxplot of sensor readings.

    Parameters
    ----------
    sensor_a : numpy.ndarray
    sensor_b : numpy.ndarray
    ax : matplotlib.axes.Axes

    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=["Sensor A", "Sensor B"])

    ax.set_title("Box Plot")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, alpha=0.3)
def main():
    """Main function to generate plots and save figure."""
    sensor_a, sensor_b, timestamps = generate_data(seed=6231)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])
    plot_histogram(sensor_a, sensor_b, axes[0, 1])
    plot_boxplot(sensor_a, sensor_b, axes[1, 0])

    axes[1, 1].axis("off")
    axes[1, 1].set_title("Summary")
    plt.tight_layout()
    plt.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")
    plt.show()
if __name__ == "__main__":
    main()