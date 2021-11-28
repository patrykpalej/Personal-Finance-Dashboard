from utl.plots.lineplot import make_lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.calculations import calculate_moving_average, calculate_cumulative_average


def mean_ear(start_date, end_date, additional_settings):
    earnings_raw = get_data("HOME_EARNINGS", start_date, end_date)
    earnings = earnings_raw.groupby("DATE").sum()["VALUE"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date).groupby("DATE").sum()
        taxes["SUM"] = taxes["PIT"] + taxes["ZUS"] - taxes["VAT"]
        earnings = earnings - taxes["SUM"]

    ma_lag = 6
    moving_avg = calculate_moving_average(earnings, ma_lag)
    total_avg = calculate_cumulative_average(earnings)

    x_values_list = [earnings.index] * 3
    y_values_list = [earnings, moving_avg, total_avg]
    names_list = ["Zarobki", "Średnia krocząca (6m)", "Dotychczasowa średnia"]
    modes_list = ["lines+markers"] * 3
    linestyles_list = ["solid"] * 3

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
