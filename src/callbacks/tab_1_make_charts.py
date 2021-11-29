from dash.dependencies import Input, Output, State

from app import app
from backend.tab_1_charts import make_chart
from config import long_chart_names, short_chart_names


def update_plotnames_list(plots_group_name, sy, sm, ey, em):
    if plots_group_name is not None and all([sy, sm, ey, em]):
        long_options_names = long_chart_names[plots_group_name]
        short_options_names = short_chart_names[plots_group_name]

        return [{'label': option_long, 'value': option_short}
                for option_long, option_short in zip(long_options_names, short_options_names)]
    else:
        return []


@app.callback(
    Output("1_plot_types_1", "options"),

    [Input("1_start_year_dropdown", "value"),
     Input("1_start_month_dropdown", "value"),
     Input("1_end_year_dropdown", "value"),
     Input("1_end_month_dropdown", "value")]
)
def update_plotgroups_1(sy, sm, ey, em):
    if all([sy, sm, ey, em]):
        return [{'label': name, 'value': name} for name in long_chart_names.keys()]
    else:
        return []


@app.callback(
    Output("1_plot_types_2", "options"),

    [Input("1_start_year_dropdown", "value"),
     Input("1_start_month_dropdown", "value"),
     Input("1_end_year_dropdown", "value"),
     Input("1_end_month_dropdown", "value")]
)
def update_plotgroups_2(sy, sm, ey, em):
    if all([sy, sm, ey, em]):
        return [{'label': name, 'value': name} for name in long_chart_names.keys()]
    else:
        return []


@app.callback(
    Output('1_plot_names_1', 'options'),

    [Input('1_plot_types_1', 'value'),

     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")]
)
def update_plotnames_1_dropdown(plots_group_name, sy, sm, ey, em):
    return update_plotnames_list(plots_group_name, sy, sm, ey, em)


@app.callback(
    Output('1_plot_names_2', 'options'),

    [Input('1_plot_types_2', 'value'),

     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")]
)
def update_plotnames_2_dropdown(plots_group_name, sy, sm, ey, em):
    return update_plotnames_list(plots_group_name, sy, sm, ey, em)


@app.callback(
    [Output("1_plot_1", "figure")],

    [Input("1_plot_names_1", "value"),
     Input("1_additional_settings", "value"),

     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")],
)
def draw_plot_1(plot_name, additional_settings, sy, sm, ey, em):
    return make_chart(plot_name, sy, sm, ey, em, additional_settings),


@app.callback(
    [Output("1_plot_2", "figure")],

    [Input("1_plot_names_2", "value"),
     Input("1_additional_settings", "value"),

     State("1_start_year_dropdown", "value"),
     State("1_start_month_dropdown", "value"),
     State("1_end_year_dropdown", "value"),
     State("1_end_month_dropdown", "value")],
)
def draw_plot_2(plot_name, additional_settings, sy, sm, ey, em):
    return make_chart(plot_name, sy, sm, ey, em, additional_settings),
