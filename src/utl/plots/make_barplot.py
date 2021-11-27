import plotly.graph_objects as go


def barplot(x, y, x_label, y_label, orientation='h'):
    fig = go.Figure()

    plot = go.Bar(x=x, y=y, orientation=orientation)

    fig.add_trace(plot)
    fig.update_layout(margin={'l': 10, 'r': 10, 't': 10, 'b': 10}, xaxis_title=x_label,
                      yaxis_title=y_label)

    return fig
