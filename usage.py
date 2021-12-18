from dash import html
from app import app
from server import serve_app

app.layout = html.Div([
    html.Header([
        html.Img(src=app.get_asset_url("logo.svg"), className="App-logo", alt="logo"),
        html.P(["Edit ", html.Code("usage.py"), " and save to reload."]),
        html.A("Learn Dash", className="App-link", href="https://dash.plotly.com/",  target="_blank", rel="noopener noreferrer")
    ], className="App-header")
], className="App")


if __name__ == '__main__':
    serve_app(app, debug=True)
