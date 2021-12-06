import dash
import dash_auth

from layout import layout
from config import dash_auth_password


app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.layout = layout()
auth = dash_auth.BasicAuth(app, {"patryk": dash_auth_password})
