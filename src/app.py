import dash
from layout import layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = layout()
