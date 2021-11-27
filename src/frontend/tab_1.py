from dash import dcc
from dash import html

from config import long_chart_names


def tab_1():
    additional_options = [
        {'label': 'Przeliczaj na miesiąc', 'value': 'calc_per_month'},
        {'label': 'Wartości po odjęciu podatków (dla faktur)', 'value': 'subtract_tax'}]

    set_time_range_options = [{"label": "Wybierz cały zakres czasu", "value": "whole_time_range"}]

    chart_groups_names = list(long_chart_names.keys())
    specific_charts_names = long_chart_names[chart_groups_names[0]]

    # =========================================================================================

    tab_layout = [
        # General settings
        html.Div(["Pierwszy miesiąc:",
                  dcc.Dropdown(id="1_start_year_dropdown", value="", placeholder="rok"),
                  dcc.Dropdown(id="1_start_month_dropdown", value="", placeholder="miesiąc")],

                 style={"width": "10vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "2vw", "top": "8vh",
                        "grid-row-gap": "14px", "position": "absolute"}),

        html.Div(["Ostatni miesiąc:",
                  dcc.Dropdown(id="1_end_year_dropdown", value="", placeholder="rok"),
                  dcc.Dropdown(id="1_end_month_dropdown", value="", placeholder="miesiąc")],

                 style={"width": "10vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "22vw", "top": "8vh",
                        "grid-row-gap": "14px", "position": "absolute"}),

        html.Div([dcc.Checklist(id="1_set_whole_time_range", options=set_time_range_options,
                                labelStyle={'display': 'block'})],
                 style={"width": "20vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "35vw", "grid-row-gap": "14px",
                        "top": "17vh", "position": "absolute"}
                 ),

        html.Div(["Dodatkowe ustawienia:",
                  dcc.Checklist(id="1_additional_settings", options=additional_options,
                                labelStyle={'display': 'block'}, value=['subtract_tax'])],
                 style={"width": "20vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "60vw", "grid-row-gap": "14px",
                        "top": "8vh", "position": "absolute"}
                 ),

        html.Hr([], style={"top": "16vh", "position": "relative", "height": "1px"}),

        # Charts
        html.Div(["Grupa wykresów:",
                  dcc.Dropdown(id="1_plot_types_1", placeholder="", options=[
                      {'label': name, 'value': name} for name in chart_groups_names])],
                 style={"width": "10vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "2vw",
                        "grid-row-gap": "14px", "top": "25vh", "position": "absolute"}),
        html.Div(["Wykres:",
                  dcc.Dropdown(id="1_plot_names_1", placeholder="", options=[
                      {'label': opt, 'value': opt} for opt in specific_charts_names])],
                 style={"width": "25vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "15vw",
                        "grid-row-gap": "14px", "top": "25vh", "position": "absolute"}),

        dcc.Graph(id="1_plot_1", style={"position": "absolute", "top": "40vh", "width": "40vw",
                                        "height": "60vh", "left": "2vw"}),

        html.Div(["Grupa wykresów:",
                  dcc.Dropdown(id="1_plot_types_2", value="", placeholder="", options=[
                      {'label': name, 'value': name} for name in chart_groups_names])],
                 style={"width": "10vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "52vw",
                        "grid-row-gap": "14px", "top": "25vh", "position": "absolute"}),
        html.Div(["Wykres:",
                  dcc.Dropdown(id="1_plot_names_2", value="", placeholder="", options=[
                      {'label': opt, 'value': opt} for opt in specific_charts_names])],
                 style={"width": "25vw", "font-family": "Cambria", "font-size": "18px",
                        "height": "10vh", "display": "grid", "left": "65vw",
                        "grid-row-gap": "14px", "top": "25vh", "position": "absolute"}),

        dcc.Graph(id="1_plot_2", style={"position": "absolute", "top": "40vh", "width": "40vw",
                                        "height": "60vh", "left": "52vw"})
    ]

    return tab_layout
