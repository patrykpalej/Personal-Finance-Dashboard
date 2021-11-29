from dash.dependencies import Input, Output, State
from backend.general import prepare_dates_range_to_display

from app import app
from datetime import date
from backend.tab_4_search_spendings import search_spendings


@app.callback(
    Output("4_finder_time_range", "children"),

    [Input("1_start_year_dropdown", "value"),
     Input("1_start_month_dropdown", "value"),
     Input("1_end_year_dropdown", "value"),
     Input("1_end_month_dropdown", "value")]
)
def set_time_range(sy, sm, ey, em):
    if all([sy, sm, ey, em]):
        return prepare_dates_range_to_display(date(sy, sm, 1), date(ey, em, 1))

    return ""


@app.callback(
    [Output("4_finder_total_sum", "children"),
     Output("4_searched_results", "children")],

    [Input("4_search_categories", "value"),
     Input("4_search_input", "value"),
     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")
     ]
)
def find_spendings(categories, search_phrase, sy, sm, ey, em):

    if all([categories, search_phrase, sy, sm, ey, em]):
        return search_spendings([f"'{cat}'" for cat in categories], search_phrase,
                                date(sy, sm, 1), date(ey, em, 1))

    return "", ""
