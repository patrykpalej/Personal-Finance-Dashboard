import dash
# import dash_auth

from layout import layout
from config import dash_auth_password


app = dash.Dash(__name__, suppress_callback_exceptions=True)
# auth = dash_auth.BasicAuth(app, {"patryk": dash_auth_password})
app.layout = layout()


if __name__ == '__main__':
    app.run_server(debug=True, port=3456, host='0.0.0.0')
