from utl.plots.make_lineplot import lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def month_spend_ear(start_date, end_date, additional_settings):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("DATE").sum()["VALUE"]

    earnings_raw = get_data("HOME_EARNINGS", start_date, end_date)
    earnings = earnings_raw.groupby("DATE").sum()["VALUE"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date).groupby("DATE").sum()
        taxes["SUM"] = taxes["PIT"] + taxes["ZUS"] - taxes["VAT"]
        earnings = earnings - taxes["SUM"]

    x_values_list = [spendings.index, earnings.index]
    y_values_list = [spendings, earnings]
    names_list = ["Wydatki", "Zarobki"]
    modes_list = ["lines+markers"] * 2
    linestyles_list = ["solid"] * 2

    return lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
