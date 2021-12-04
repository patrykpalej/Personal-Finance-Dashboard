from dash import dcc
from dash import html

from utl.db import select_data_from_time_range_for_given_table as get_data


spendings_categories = get_data("home_spendings", '2000-01-01', '2099-12-31')["category"].unique()
category_options = ([{"label": "WSZYSTKO", "value": "all"}]
                    + [{"label": str(cat), "value": str(cat)} for cat in spendings_categories])


def tab_4():
    return html.Div([
        html.Div(style={"font-family": "Cambria", "position": "absolute", "left": "5vw",
                        "top": "9vh", "font-size": "18px", "border-bottom": "2px solid black"},
                 id="4_finder_time_range"),

        html.Div(style={"font-family": "Cambria", "position": "absolute", "top": "9vh",
                        "left": "25vw", "font-size": "18px", "border-bottom": "2px solid black"},
                 id="4_finder_total_sum"),

        html.Div(["Fraza do wyszukania: ", dcc.Input(id="4_search_input")],
                 style={"position": "absolute", "width": "15vw", "left": "6vw", "top": "17vh",
                        "height": "5vh"}),

        html.Div(["Wybierz kategorie:", dcc.Dropdown(id="4_search_categories", value="", multi=True,
                                                     placeholder="", options=category_options)],
                 style={"position": "absolute", "width": "15vw", "left": "5vw", "top": "25vh"}),

        html.Div(id="4_searched_results",
                 style={"position": "absolute", "width": "32vw", "left": "25vw", "top": "15vh",
                        "height": "70vh", "overflow": "scroll"})
    ])
