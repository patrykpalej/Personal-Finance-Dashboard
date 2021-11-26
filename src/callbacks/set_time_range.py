from dash.dependencies import Input, Output

from app import app
from utl.db import return_list_of_unique_years_in_db
from utl.db import return_list_of_months_for_given_year
from utl.dates_handling import (generate_end_years_list_based_on_start_date,
                                generate_end_months_list_based_on_start_date_and_end_year)


@app.callback(
    [Output("1_start_date_year_dropdown", "options"),
     Output("1_start_date_year_dropdown", "value")],

    Input("1_set_whole_time_range", "value")
)
def set_start_years_list(checkbox_value):
    if checkbox_value == ["whole_time_range"]:
        first_year_in_db = min(return_list_of_unique_years_in_db())
        return [{"label": str(first_year_in_db), "value": first_year_in_db}], first_year_in_db
    else:
        unique_years_in_db = return_list_of_unique_years_in_db()
        start_date_year_options = [{"label": str(year), "value": year}
                                   for year in unique_years_in_db]
        return start_date_year_options, None


@app.callback(
    [Output("1_start_date_month_dropdown", "options"),
     Output("1_start_date_month_dropdown", "value")],

    [Input("1_start_date_year_dropdown", "value"),
     Input("1_set_whole_time_range", "value")]
)
def set_start_months_list_based_on_start_year(start_year, checkbox_value):
    if checkbox_value == ["whole_time_range"]:
        first_year_in_db = min(return_list_of_unique_years_in_db())
        first_month = min(return_list_of_months_for_given_year(first_year_in_db))
        return [{"label": str(first_month), "value": first_month}], first_month
    else:
        unq_months = return_list_of_months_for_given_year(start_year)
        return [{"label": str(month), "value": month} for month in unq_months], None


@app.callback(
    [Output("1_end_date_year_dropdown", "options"),
     Output("1_end_date_year_dropdown", "value")],

    [Input("1_start_date_year_dropdown", "value"),
     Input("1_start_date_month_dropdown", "value"),
     Input("1_set_whole_time_range", "value")]
)
def set_end_years_list_based_on_start_date(start_year, start_month, checkbox_value):
    if checkbox_value == ["whole_time_range"]:
        last_year_in_db = max(return_list_of_unique_years_in_db())
        return [{"label": str(last_year_in_db), "value": last_year_in_db}], last_year_in_db
    else:
        all_possible_end_years = generate_end_years_list_based_on_start_date(
            start_year, start_month)
        return [{"label": str(year), "value": year} for year in all_possible_end_years], None


@app.callback(
    [Output("1_end_date_month_dropdown", "options"),
     Output("1_end_date_month_dropdown", "value")],

    [Input("1_start_date_year_dropdown", "value"),
     Input("1_start_date_month_dropdown", "value"),
     Input("1_end_date_year_dropdown", "value"),
     Input("1_set_whole_time_range", "value")]
)
def set_end_months_list_based_on_start_date_and_end_year(
        start_year, start_month, end_year, checkbox_value):

    if checkbox_value == ["whole_time_range"]:
        last_year_in_db = max(return_list_of_unique_years_in_db())
        last_month = max(return_list_of_months_for_given_year(last_year_in_db))
        return [{"label": str(last_month), "value": last_month}], last_month
    else:
        all_possible_end_months = generate_end_months_list_based_on_start_date_and_end_year(
            start_year, start_month, end_year)
        return [{"label": str(month), "value": month} for month in all_possible_end_months], None
