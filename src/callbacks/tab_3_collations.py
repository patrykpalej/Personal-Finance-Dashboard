from dash.dependencies import Input, Output, State
from backend.general import prepare_dates_range_to_display

from app import app
from datetime import date
from backend.tab_3_left_table import fill_left_table
from backend.tab_3_right_table import fill_right_table


@app.callback(
    Output("3_collation_time_range", "children"),

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
    [Output("3_collation_table_1", "children"),
     Output("3_total_sum", "children")],

    [Input("3_category_dropdown", "value"),
     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")]
)
def fill_left_collation_table(categories, sy, sm, ey, em):
    if all([categories, sy, sm, ey, em]):
        return fill_left_table([f"'{cat}'" for cat in categories], date(sy, sm, 1), date(ey, em, 1))

    return [], ""


@app.callback(
    Output("3_collation_table_2", "children"),

    [Input("3_min_sum", "value"),
     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")]
)
def fill_right_collation_table(min_sum, sy, sm, ey, em):
    if all([min_sum, sy, sm, ey, em]):
        return fill_right_table(min_sum, date(sy, sm, 1), date(ey, em, 1))

    return []
