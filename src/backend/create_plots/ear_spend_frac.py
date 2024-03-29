from utl.plots.lineplot import make_lineplot
from utl.calculations import calculate_trend_line_points_pair
from utl.db import select_data_from_time_range_for_given_table as get_data


def ear_spend_frac(start_date, end_date, additional_settings):
    spendings_raw = get_data("home_spendings", start_date, end_date)
    spendings = spendings_raw.groupby("date").sum(numeric_only=True)["value"]

    earnings_raw = get_data("home_earnings", start_date, end_date)
    earnings = earnings_raw.groupby("date").sum(numeric_only=True)["value"]

    if spendings.index.nunique() > earnings.index.nunique():
        earnings = earnings.reindex(spendings.index).fillna(0)

    if earnings.index.nunique() > spendings.index.nunique():
        spendings = spendings.reindex(earnings.index).fillna(0)

    if "subtract_tax" in additional_settings:
        taxes = get_data("home_taxes", start_date, end_date).groupby("date").sum(numeric_only=True)
        taxes["sum"] = taxes["pit"] + taxes["zus"] - taxes["vat"]
        earnings = earnings - taxes["sum"]

    fraction = (earnings / spendings).fillna(0)
    trend_line_points_pair = calculate_trend_line_points_pair(fraction)
    trend_line_values = [point[1] for point in trend_line_points_pair]

    # fillna

    x_values_list = [fraction.index, (fraction.index[0], fraction.index[-1])]
    y_values_list = [fraction, trend_line_values]
    names_list = ["Dane", "Linia trendu"]
    modes_list = ["lines+markers", "lines"]
    linestyles_list = ["solid", "dash"]

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
