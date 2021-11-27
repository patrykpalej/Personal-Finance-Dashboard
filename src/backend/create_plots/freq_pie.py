from utl.plots.make_pieplot import pieplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.dates_handling import calculate_n_of_uniuqe_months_based_on_range


def freq_pie(start_date, end_date, additional_settings):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("CATEGORY").sum()["VALUE"].sort_values(ascending=False)

    n_of_main_categories = 4

    labels = list(spendings.index[:n_of_main_categories]) + ["Inne"]

    if "calc_per_month" in additional_settings:
        n_of_months = calculate_n_of_uniuqe_months_based_on_range(spendings_raw["DATE"])
        values = ([round(item, 2) for item in spendings[:n_of_main_categories] / n_of_months] +
                  [round(sum(spendings[n_of_main_categories:]) / n_of_months, 2)])
    else:
        values = ([round(item, 2) for item in spendings[:n_of_main_categories]]
                  + [round(sum(spendings[n_of_main_categories:]), 2)])

    return pieplot(labels, values)
