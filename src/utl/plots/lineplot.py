import plotly.graph_objects as go


def make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list, x_labels=None,
                  x_tickvals=None, ylims=None):
    fig = go.Figure()

    for x, y, name, mode, linestyle in zip(x_values_list, y_values_list, names_list, modes_list,
                                           linestyles_list):
        plot = go.Scatter(x=x, y=y, name=name, mode=mode, line={'dash': linestyle})
        fig.add_trace(plot)

    fig.update_layout(margin={'l': 10, 'r': 10, 't': 10, 'b': 10}, yaxis_range=ylims,
                      xaxis={"tickmode": "array", "ticktext": x_labels, "tickvals": x_tickvals},
                      legend={"orientation": "h", "yanchor": "bottom", "y": 1.02,
                              "xanchor": "right", "x": 1})
    return fig
