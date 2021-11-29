from dash.dependencies import Input, Output

from app import app
from datetime import date
from backend.general import prepare_dates_range_to_display
from backend.tab_2_stats_table import prepare_stats_table_data


@app.callback(
    [Output("2_stat_table", "data"),
     Output("2_dates_range_summary", "children")],

    [Input("1_start_year_dropdown", "value"),
     Input("1_start_month_dropdown", "value"),
     Input("1_end_year_dropdown", "value"),
     Input("1_end_month_dropdown", "value"),
     Input("1_additional_settings", "value")]
)
def fill_stats_table(sy, sm, ey, em, additional_settings):
    if all([sy, sm, ey, em]):
        start_date, end_date = date(sy, sm, 1), date(ey, em, 1)

        return (prepare_stats_table_data(start_date, end_date, additional_settings),
                prepare_dates_range_to_display(start_date, end_date))

    return [dict(zip(["none", "mean", "median", "deviation", "sum"], [item, "", "", "", ""]))
            for item in ["Zarobki", "Wydatki", "Nadwyżki", "Inwestycje"]], ""
