from utl.plots.make_lineplot import lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.calculations import calculate_moving_average, calculate_cumulative_average


def mean_spend(start_date, end_date, _):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("DATE").sum()["VALUE"]

    ma_lag = 6
    moving_avg = calculate_moving_average(spendings, ma_lag)
    total_avg = calculate_cumulative_average(spendings)

    x_values_list = [spendings.index] * 3
    y_values_list = [spendings, moving_avg, total_avg]
    names_list = ["Wydatki", "Średnia krocząca (6m)", "Dotychczasowa średnia"]
    modes_list = ["lines+markers"] * 3
    linestyles_list = ["solid"] * 3

    return lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
