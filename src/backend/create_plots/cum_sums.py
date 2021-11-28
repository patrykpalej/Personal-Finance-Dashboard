import numpy as np
from utl.plots.lineplot import make_lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def cum_sums(start_date, end_date, additional_settings):
    earnings_raw = get_data("HOME_EARNINGS", start_date, end_date)
    earnings = earnings_raw.groupby("DATE").sum()["VALUE"]

    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("DATE").sum()["VALUE"]

    longterm_raw = get_data("HOME_LONG_TERM", start_date, end_date)
    longterm = longterm_raw.groupby("DATE").sum()["VALUE"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date).groupby("DATE").sum()
        taxes["SUM"] = taxes["PIT"] + taxes["ZUS"] - taxes["VAT"]
        earnings = earnings - taxes["SUM"]

    excess = earnings - spendings

    x_values_list = [spendings.index] * 4
    y_values_list = [np.cumsum(values) for values in [earnings, spendings, longterm, excess]]
    names_list = ["Zarobki", "Wydatki", "Inwestycje", "Nadwyżki"]
    modes_list = ["lines+markers"] * 4
    linestyles_list = ["solid"] * 4

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
