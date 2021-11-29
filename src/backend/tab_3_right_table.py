from dash import dash_table

from config import month_dict
from utl.db import select_data_from_time_range_for_given_table as get_data


def fill_right_table(min_sum, start_date, end_date):
    value_filter = f''' "VALUE" >= {min_sum} '''
    spendings = (get_data("HOME_SPENDINGS", start_date, end_date, where=value_filter)
                 .sort_values("VALUE", ascending=False))

    spendings["DATE"] = spendings["DATE"].apply(lambda x: f'{month_dict[x.month]} {x.year}')
    spendings["id"] = range(1, len(spendings)+1)
    spendings.rename({"DESCRIPTION": "name", "VALUE": "value", "CATEGORY": "cat",
                      "DATE": "month"}, axis=1, inplace=True)

    return dash_table.DataTable(
        columns=[{"name": "id", "id": "id"}, {"name": "Nazwa", "id": "name"},
                 {"name": "Wartość [PLN]", "id": "value"}, {"name": "Kategoria", "id": "cat"},
                 {"name": "Miesiąc", "id": "month"}],
        data=spendings[["id", "name", "value", "cat", "month"]].to_dict('records'),
        style_data={"text-align": "center", "font-family": "Cambria"},
        style_cell={"textAlign": "center", "font-family": "Cambria", "max-width": "12vw",
                    "whiteSpace": "normal", "height": "auto", "width": "auto"},
        style_table={"overflowY": "auto", "overflowX": "auto", "width": "auto"},
        style_header={"backgroundColor": "#bcc5f7"})
