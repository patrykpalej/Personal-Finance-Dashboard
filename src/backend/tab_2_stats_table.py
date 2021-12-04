from utl.general import format_number
from utl.db import select_data_from_time_range_for_given_table as get_data


def prepare_stats_table_data(start_date, end_date, additional_settings):
    earnings = get_data("home_earnings", start_date, end_date).groupby("date").sum()["value"]
    spendings = get_data("home_spendings", start_date, end_date).groupby("date").sum()["value"]
    longterm = get_data("home_longterm", start_date, end_date).groupby("date").sum()["value"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("home_taxes", start_date, end_date).groupby("date").sum()
        taxes["sum"] = taxes["pit"] + taxes["zus"] - taxes["vat"]
        earnings = earnings - taxes["sum"]

    budget_elements = ["Zarobki", "Wydatki", "Nadwyżki", "Inwestycje"]
    budget_dict = dict(zip(budget_elements, [earnings, spendings, earnings-spendings, longterm]))
    table_columns = ["none", "mean", "median", "deviation", "sum"]

    table_data = []

    for item in budget_elements:
        values = budget_dict[item]
        aggregations = [format_number(number)
                        for number in [values.mean(), values.median(), values.mad(), values.sum()]]

        table_data.append(dict(zip(table_columns, [item, *aggregations])))

    return table_data
