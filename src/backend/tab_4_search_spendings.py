from dash import html

from backend.general import make_html_table
from utl.db import select_data_from_time_range_for_given_table as get_data


def make_a_search(spendings, search_phrase):
    return spendings[spendings["description"].apply(lambda x: search_phrase.lower() in x)]


def search_spendings(categories, search_phrase, start_date, end_date):
    categories_filter = f''' category in ({','.join(categories)})'''
    spendings = get_data("home_spendings", start_date, end_date, where=categories_filter)
    searched_results = make_a_search(spendings, search_phrase)

    return (f"Suma pasujących wydatków: {round(sum(searched_results['value']), 2)} zł",
            html.Table(make_html_table(searched_results), style={"width": "30vw"}))
