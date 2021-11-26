import plotly.graph_objects as go


def pieplot(labels, values):
    fig = go.Figure()

    plot = go.Pie(labels=labels, values=[round(v, 2) for v in values])

    fig.add_trace(plot)
    fig.update_layout(margin={'l': 10, 'r': 10, 't': 10, 'b': 10})

    return fig
