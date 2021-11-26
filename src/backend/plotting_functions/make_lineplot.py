import plotly.graph_objects as go


def lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list, x_labels,
             x_tickvals, ylims):
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


# if len(x_labels) > 24:
    #     factor = round(len(x_labels) / 12)
    #     tickvals = list(range(len(x_labels)))[::factor]
    #     x_labels = x_labels[::factor]
    #
    # else:
    #     tickvals = list(range(len(x_labels)))
    #
    # y_min_lim = min(0, 1.1 * float(min([min([val for val in x if val > 0]) for x in values_list])))
    # y_max_lim = 1.1 * float(max([n for n in [max([val for val in x if val > 0]) for x in values_list] if n > 0]))
