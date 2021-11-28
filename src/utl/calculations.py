import numpy as np


def calculate_moving_average(values, lag):
    values = np.array(values)
    return [values[i - lag + 1:i + 1].mean() for i, _ in enumerate(values)]


def calculate_cumulative_average(values):
    values = np.array(values)
    return [values[:i+1].mean() for i, _ in enumerate(values)]


def calculate_trend_line_points_pair(values):
    values = np.array(values)
    trend_line_polyfit = np.polyfit(np.array(range(len(values))), values, 1)

    return [(0, trend_line_polyfit[1]),
            (len(values)-1, trend_line_polyfit[0] * len(values) + trend_line_polyfit[1])]
