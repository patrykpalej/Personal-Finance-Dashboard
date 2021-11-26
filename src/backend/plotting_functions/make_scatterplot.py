import numpy as np
import plotly.graph_objects as go


def scatterplot(x, y, point_labels, xlabel, ylabel, add_trend_line=True, add_y_equals_x=True):
    fig = go.Figure()
    plot = go.Scatter(x=x, y=y, mode='markers', name="Dane", text=point_labels)
    fig.add_trace(plot)

    lims = [float(min(min(x), min(y))), float(max(max(x), max(y)))]

    if add_trend_line:
        trend_line_coeffs = np.polyfit(np.array(x).astype('float'), np.array(y).astype('float'), 1)

        y_ = [lims[0] * trend_line_coeffs[0] + trend_line_coeffs[1],
              lims[1] * trend_line_coeffs[0] + trend_line_coeffs[1]]

        trend_line_plot = go.Scatter(x=lims, y=y_, mode='lines', name="Linia trendu")
        fig.add_trace(trend_line_plot)

    if add_y_equals_x:
        yx_line = go.Scatter(x=lims, y=lims, mode='lines', name="y=x")
        fig.add_trace(yx_line)

    fig.update_layout(margin={'l': 10, 'r': 10, 't': 10, 'b': 10},
                      xaxis_range=(.9*lims[0], 1.1*lims[1]), yaxis_range=(.9*lims[0], 1.1*lims[1]),
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      xaxis_title=xlabel, yaxis_title=ylabel)

    return fig
