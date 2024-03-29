from utl.plots.barplot import make_barplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.dates_handling import calculate_n_of_uniuqe_months_based_on_range


def cat_bar(start_date, end_date, additional_settings):
    spendings_raw = get_data("home_spendings", start_date, end_date)
    spendings = spendings_raw.groupby("category").sum(numeric_only=True)["value"].sort_values()

    if "calc_per_month" in additional_settings:
        n_of_months = calculate_n_of_uniuqe_months_based_on_range(spendings_raw["date"])
        x = [round(item, 2) for item in spendings / n_of_months]
    else:
        x = [round(item, 2) for item in spendings]

    y = spendings.index
    x_label = "Wartość"
    y_label = "Kategoria"

    return make_barplot(x, y, x_label, y_label)
