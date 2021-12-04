from dash import html

from utl.general import format_number
from backend.general import make_html_table
from utl.db import select_data_from_time_range_for_given_table as get_data


def fill_left_table(categories, start_date, end_date):
    categories_filter = f''' category in ({','.join(categories)})'''
    spendings = get_data("home_spendings", start_date, end_date, where=categories_filter)

    return (f"Suma całkowita: {format_number(sum(spendings['value']))} zł",
            html.Table(make_html_table(spendings), style={"width": "30vw"}))
