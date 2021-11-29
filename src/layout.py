from dash import dcc
from dash import html

from frontend.tab_1 import tab_1
from frontend.tab_2 import tab_2
from frontend.tab_3 import tab_3
from frontend.tab_4 import tab_4
from frontend.tab_5 import tab_5


def layout():
    return html.Div([
        dcc.Tabs(id="app_tabs", value="tab1",
                 children=[dcc.Tab(children=tab_1(), id="tab_1", value="tab1",
                                   label="Wykresy"),
                           dcc.Tab(children=tab_2(), id="tab_2", value="tab2",
                                   label="Statystyki"),
                           dcc.Tab(children=tab_3(), id="tab_3", value="tab3",
                                   label="Zestawienia wydatków"),
                           dcc.Tab(children=tab_4(), id="tab_4", value="tab4",
                                   label="Wyszukiwarka"),
                           dcc.Tab(children=tab_5(), id="tab_5", value="tab5",
                                   label="Bilans")])
    ])
