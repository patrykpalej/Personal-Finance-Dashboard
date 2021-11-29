from dash import dcc
from dash import html
from dash import dash_table

from config import BALANCE_N_INPUTS


def tab_5():
    table_cols = ["Suma przychodów", "Suma wydatków", "Suma oszczędności", "Bilans"]

    return html.Div(
        [html.Div(["Nazwa konta"], style={"position": "absolute", "left": "8vw", "top": "10vh"}),

         html.Div(["Ilość pieniędzy"],
                  style={"position": "absolute", "left": "23vw", "top": "10vh"})] +

        [html.Div([dcc.Input(id={"index": i, "type": "input_1_"}, value="",
                   style={"font-family": "Cambria", "position": "absolute",
                          "top": f"{str(15 + i * 6)}vh", "left": "5vw", "font-size": "18px",
                          "height": "4vh", "width": "12vw"}) for i in range(BALANCE_N_INPUTS)])] +

        [html.Div([dcc.Input(id={"index": i, "type": "input_2_"},
                   style={"font-family": "Cambria", "position": "absolute", "font-size": "18px",
                          "top": "{}vh".format(str(15 + i * 6)), "left": "20vw", "height": "4vh",
                          "width": "12vw"})]) for i in range(BALANCE_N_INPUTS)] +

        [html.Button(["Oblicz"], id="5_balance_button",
                     style={"position": "absolute", "left": "40vw",
                            "top": "80vh", "width": "5vw", "height": "5vh"}),

         html.Div([dash_table.DataTable(id="5_balance_table", data=[],
                                        columns=[{"name": i, "id": i} for i in table_cols],
                                        style_data={"text-align": "center", "font-size": "15px"},
                                        style_header={"text-align": "center",
                                                      "font-size": "18px"})],
                  style={"position": "absolute", "left": "50vw",
                         "top": "20vh", "width": "35vw"})])
