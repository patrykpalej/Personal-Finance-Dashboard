import dash
# import dash_auth
from dash.dependencies import Input, Output, State, ALL

from layout import layout
from config import dash_auth_password
from utl.db import return_list_of_months_for_given_year


app = dash.Dash(__name__, suppress_callback_exceptions=True)
# auth = dash_auth.BasicAuth(app, {"patryk": dash_auth_password})
app.layout = layout()

# ===============================================================================================


@app.callback(
    Output("1_start_date_month_dropdown", "options"),
    Input("1_start_date_year_dropdown", "value")
)
def set_months_list_based_on_year__start(year):
    return return_list_of_months_for_given_year(year) if year else []


@app.callback(
    Output("1_end_date_month_dropdown", "options"),
    Input("1_end_date_year_dropdown", "value")
)
def set_months_list_based_on_year__end(year):
    return return_list_of_months_for_given_year(year) if year else []

# ===============================================================================================


if __name__ == '__main__':
    app.run_server(debug=True, port=3456, host='0.0.0.0')
