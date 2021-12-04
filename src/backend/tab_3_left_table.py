from dash import html

from utl.general import format_number
from backend.general import make_html_table
from utl.db import select_data_from_time_range_for_given_table as get_data


def fill_left_table(categories, start_date, end_date):
    categories_filter = f''' "CATEGORY" in ({','.join(categories)})'''
    spendings = get_data("HOME_SPENDINGS", start_date, end_date, where=categories_filter)

    return (f"Suma całkowita: {format_number(sum(spendings['VALUE']))} zł",
            html.Table(make_html_table(spendings), style={"width": "30vw"}))
