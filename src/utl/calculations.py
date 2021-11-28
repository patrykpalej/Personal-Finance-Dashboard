import numpy as np


def calculate_moving_average(values, lag):
    values = np.array(values)
    return [values[i - lag + 1:i + 1].mean() for i, _ in enumerate(values)]


def calculate_cumulative_average(values):
    values = np.array(values)
    return [values[:i+1].mean() for i, _ in enumerate(values)]
