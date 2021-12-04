from dash import dcc
from dash import html

from utl.db import select_data_from_time_range_for_given_table as get_data


spendings_categories = get_data("home_spendings", '2000-01-01', '2099-12-31')["category"].unique()
category_options = [{"label": str(cat), "value": str(cat)} for cat in spendings_categories]


def tab_3():
    return html.Div([
        html.Div([""], style={"font-family": "Cambria", "position": "absolute",
                              "top": "9vh", "left": "5vw", "font-size": "18px",
                              "border-bottom": "2px solid black"}, id="3_collation_time_range"),

        html.Div(["Wybierz kategorie:",
                  dcc.Dropdown(id="3_category_dropdown", value="", placeholder="",
                               options=category_options, multi=True)],
                 style={"position": "absolute", "width": "25vw", "left": "5vw", "top": "14vh"}),

        html.Div(style={"position": "absolute", "width": "15vw", "left": "5vw", "top": "21vh",
                        "font-size": "18px"}, id="3_total_sum"),

        html.Div(["Minimalna kwota wydatków w zestawieniu [PLN]:", dcc.Input(id="3_min_sum")],
                 style={"position": "absolute", "width": "20vw", "left": "45vw", "top": "14vh"}),

        html.Div([], id="3_collation_table_1",
                 style={"position": "absolute", "width": "30vw", "left": "5vw", "top": "27vh",
                        "height": "70vh", "overflow": "scroll"}),

        html.Hr([], style={"width": "1px", "height": "75vh", "position": "absolute",
                           "left": "40vw", "top": "20vh"}),

        html.Div([], id="3_collation_table_2",
                 style={"position": "absolute", "width": "50vw", "left": "45vw",
                        "top": "25vh", "height": "70vh", 'overflowY': 'scroll'})
    ])
