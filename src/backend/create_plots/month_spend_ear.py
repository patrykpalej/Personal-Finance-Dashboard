from utl.plots.lineplot import make_lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def month_spend_ear(start_date, end_date, additional_settings):
    spendings_raw = get_data("home_spendings", start_date, end_date)
    spendings = spendings_raw.groupby("date").sum()["value"]

    earnings_raw = get_data("home_earnings", start_date, end_date)
    earnings = earnings_raw.groupby("date").sum()["value"]

    if spendings.index.nunique() > earnings.index.nunique():
        earnings = earnings.reindex(spendings.index).fillna(0)

    if earnings.index.nunique() > spendings.index.nunique():
        spendings = spendings.reindex(earnings.index).fillna(0)

    if "subtract_tax" in additional_settings:
        taxes = get_data("home_taxes", start_date, end_date).groupby("date").sum()
        taxes["sum"] = taxes["pit"] + taxes["zus"] - taxes["vat"]
        earnings = earnings - taxes["sum"]

    x_values_list = [spendings.index, earnings.index]
    y_values_list = [spendings, earnings]
    names_list = ["Wydatki", "Zarobki"]
    modes_list = ["lines+markers"] * 2
    linestyles_list = ["solid"] * 2

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
