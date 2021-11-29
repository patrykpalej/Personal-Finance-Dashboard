from dash import dash_table
from dash import html


def tab_2():

    return html.Div([
        html.Div([""], id="2_dates_range_summary",
                 style={"font-family": "Cambria", "position": "absolute", "font-size": "18px",
                        "border-bottom": "2px solid black"}),

        html.Br(),
        html.Br(),

        dash_table.DataTable(
            id="2_stat_table", style_cell={'textAlign': 'center'},
            columns=[{"id": "none", "name": ""},
                     {"id": "mean", "name": "Średnia"},
                     {"id": "median", "name": "Mediana"},
                     {"id": "deviation", "name": "Średnie odchylenie"},
                     {"id": "sum", "name": "Suma"}])],

        style={"position": "absolute", "left": "10vw", "top": "10vh", "width": "45vw",
               "height": "60vh", "font-family": "Cambria", "font-size": "18px"})
