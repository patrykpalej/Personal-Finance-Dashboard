from utl.plots.pieplot import make_pieplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.dates_handling import calculate_n_of_uniuqe_months_based_on_range


def meta_pie(start_date, end_date, additional_settings):
    spendings_raw = get_data("home_spendings", start_date, end_date)
    spendings = spendings_raw.groupby("metacategory").sum()["value"].sort_values(ascending=False)

    labels = list(spendings.index)

    if "calc_per_month" in additional_settings:
        n_of_months = calculate_n_of_uniuqe_months_based_on_range(spendings_raw["date"])
        values = (spendings / n_of_months).apply(round, args=(2,))
    else:
        values = spendings

    return make_pieplot(labels, values)
