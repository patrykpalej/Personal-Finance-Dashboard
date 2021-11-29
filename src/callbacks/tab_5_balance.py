from dash.dependencies import Input, Output, State, ALL

from app import app
from config import bank_accounts
from backend.tab_5_calculate_balance import calculate_balance


@app.callback(
    [Output("5_balance_table", "data"),
     Output({"index": ALL, "type": "input_1_"}, "value")],

    [Input("5_balance_button", "n_clicks"),
     State({"type": "input_1_", "index": ALL}, "value"),
     State({"type": "input_2_", "index": ALL}, "value")]
)
def calculate_balance_callback(n_clicks, accounts_names, amounts):
    accounts_names[:len(bank_accounts)] = bank_accounts

    if n_clicks:
        return calculate_balance(accounts_names, amounts)

    return [], accounts_names
