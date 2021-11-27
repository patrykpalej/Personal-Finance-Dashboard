from datetime import date
import plotly.graph_objects as go

from backend.create_plots.cat_bar import cat_bar
from backend.create_plots.freq_pie import freq_pie
from backend.create_plots.meta_pie import meta_pie
from backend.create_plots.food_pie import food_pie
from backend.create_plots.ear_pie import ear_pie
from backend.create_plots.inc_pie import inc_pie
from backend.create_plots.cum_sums import cum_sums
from backend.create_plots.month_spend_ear import month_spend_ear
from backend.create_plots.ear_srcs import ear_srcs
from backend.create_plots.ear_vs_spend import ear_vs_spend
from backend.create_plots.meta_cats import meta_cats
from backend.create_plots.ear_spend_frac import ear_spend_frac
from backend.create_plots.mean_spend import mean_spend
from backend.create_plots.mean_ear import mean_ear


def make_chart(plot_name, sy, sm, ey, em, additional_settings):
    if not all([plot_name, sy, sm, ey, em]):
        return go.Figure()

    fig = eval(plot_name)(date(sy, sm, 1), date(ey, em, 1), additional_settings)

    if isinstance(fig, int):
        return go.Figure()
    else:
        return fig
