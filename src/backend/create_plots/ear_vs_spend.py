from utl.plots.scatterplot import make_scatterplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def ear_vs_spend(start_date, end_date, additional_settings):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("DATE").sum()["VALUE"]

    earnings_raw = get_data("HOME_EARNINGS", start_date, end_date)
    earnings = earnings_raw.groupby("DATE").sum()["VALUE"]

    if spendings.index.nunique() > earnings.index.nunique():
        earnings = earnings.reindex(spendings.index).fillna(0)

    if earnings.index.nunique() > spendings.index.nunique():
        spendings = spendings.reindex(earnings.index).fillna(0)

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date).groupby("DATE").sum()
        taxes["SUM"] = taxes["PIT"] + taxes["ZUS"] - taxes["VAT"]
        earnings = earnings - taxes["SUM"]

    x = earnings
    y = spendings
    point_labels = spendings.index
    xlabel = "Zarobki"
    ylabel = "Wydatki"

    return make_scatterplot(x, y, point_labels, xlabel, ylabel)
