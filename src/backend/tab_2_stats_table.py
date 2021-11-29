from utl.general import format_number
from utl.db import select_data_from_time_range_for_given_table as get_data


def prepare_stats_table_data(start_date, end_date, additional_settings):
    earnings = get_data("HOME_EARNINGS", start_date, end_date).groupby("DATE").sum()["VALUE"]
    spendings = get_data("HOME_SPENDINGS", start_date, end_date).groupby("DATE").sum()["VALUE"]
    longterm = get_data("HOME_LONG_TERM", start_date, end_date).groupby("DATE").sum()["VALUE"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date).groupby("DATE").sum()
        taxes["SUM"] = taxes["PIT"] + taxes["ZUS"] - taxes["VAT"]
        earnings = earnings - taxes["SUM"]

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
