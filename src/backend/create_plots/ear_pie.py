from utl.plots.pieplot import make_pieplot
from utl.taxes_handling import subtract_taxes_from_earnings
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.dates_handling import calculate_n_of_uniuqe_months_based_on_range


def ear_pie(start_date, end_date, additional_settings):
    earnings_raw = get_data("home_earnings", start_date, end_date)
    earnings = earnings_raw.groupby(["date", "source"]).sum()["value"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("home_taxes", start_date, end_date).groupby("date").sum()
        earnings_minus_taxes = subtract_taxes_from_earnings(earnings, taxes)
        top_earnings = earnings_minus_taxes.groupby("source").sum().sort_values(ascending=False)
    else:
        top_earnings = earnings.groupby("source").sum().sort_values(ascending=False)

    if "calc_per_month" in additional_settings:
        n_of_months = calculate_n_of_uniuqe_months_based_on_range(earnings_raw["date"])
        top_earnings = (top_earnings / n_of_months).apply(round, args=(2,))

    threshold_percentage = 0.04
    labels, values = [], []
    for i, (source, value) in enumerate(top_earnings.iteritems()):
        if value >= threshold_percentage * sum(top_earnings):
            labels.append(source)
            values.append(round(value, 2))
        else:
            labels.append("Inne")
            values.append(round(sum(top_earnings[i:]), 2))
            break

    return make_pieplot(labels, values)
