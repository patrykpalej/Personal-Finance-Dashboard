import dash
# import dash_auth
from dash.dependencies import Input, Output, State, ALL

from layout import layout
# from config import dash_auth_password
from utl.db import return_list_of_months_for_given_year
from utl.general_functions import (generate_end_years_list_based_on_start_date,
                                   generate_end_months_list_based_on_start_date_and_end_year)


app = dash.Dash(__name__, suppress_callback_exceptions=True)
# auth = dash_auth.BasicAuth(app, {"patryk": dash_auth_password})
app.layout = layout()

# ===============================================================================================


@app.callback(
    Output("1_start_date_month_dropdown", "options"),
    Input("1_start_date_year_dropdown", "value")
)
def set_start_months_list_based_on_start_year(start_year):
    unq_months = return_list_of_months_for_given_year(start_year)
    return [{"label": str(month), "value": month} for month in unq_months]


@app.callback(
    Output("1_end_date_year_dropdown", "options"),

    [Input("1_start_date_year_dropdown", "value"),
     Input("1_start_date_month_dropdown", "value")]
)
def set_end_years_list_based_on_start_date(start_year, start_month):
    all_possible_end_years = generate_end_years_list_based_on_start_date(start_year, start_month)
    return [{"label": str(year), "value": year} for year in all_possible_end_years]


@app.callback(
    Output("1_end_date_month_dropdown", "options"),
    [Input("1_start_date_year_dropdown", "value"),
     Input("1_start_date_month_dropdown", "value"),
     Input("1_end_date_year_dropdown", "value")]
)
def set_end_months_list_based_on_start_date_and_end_year(start_year, start_month, end_year):
    all_possible_end_months = generate_end_months_list_based_on_start_date_and_end_year(
        start_year, start_month, end_year)
    return [{"label": str(month), "value": month} for month in all_possible_end_months]

# ===============================================================================================


if __name__ == '__main__':
    app.run_server(debug=True, port=3456, host='0.0.0.0')
