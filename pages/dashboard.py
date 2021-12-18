from dash import html, register_page
import dash_bootstrap_components as dbc
from flask import current_app

register_page(__name__, path="/")

def layout():
    app = current_app.get_dash()
    return html.Div([
        html.Header([
            html.Img(src=app.get_asset_url("logo.svg"), className="App-logo", alt="logo"),
            html.P(["Edit ", html.Code("usage.py"), " and save to reload."]),
            html.A("Learn Dash", className="App-link", href="https://dash.plotly.com/",  target="_blank", rel="noopener noreferrer")
        ], className="App-header")
    ], className="App")
