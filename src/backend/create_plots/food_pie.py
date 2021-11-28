from utl.plots.pieplot import make_pieplot
from utl.db import select_data_from_time_range_for_given_table as get_data
from utl.dates_handling import calculate_n_of_uniuqe_months_based_on_range


def food_pie(start_date, end_date, additional_settings):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings_food = spendings_raw[spendings_raw["CATEGORY"] == "Jedzenie"]
    food_grouped = spendings_food.groupby("DESCRIPTION").sum()["VALUE"].sort_values(ascending=False)

    threshold_percentage = 0.04

    labels, values = [], []
    for i, value in food_grouped.iteritems():
        if value > threshold_percentage * sum(food_grouped):
            labels.append(i)
            values.append(value)
        else:
            labels.append("Inne")
            values.append(round(sum(food_grouped.loc[i:]), 2))
            break

    if "calc_per_month" in additional_settings:
        n_of_months = calculate_n_of_uniuqe_months_based_on_range(spendings_raw["DATE"])
        values = [round(item / n_of_months, 2) for item in values]

    return make_pieplot(labels, values)
