import flask
from dash import Dash
import dash_labs as dl

import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://use.fontawesome.com/releases/v5.4.1/css/all.css",
    "https://fonts.googleapis.com/css?family=Open+Sans:300,400"
    ]

external_scripts = [
    ]

# Server definition

server = flask.Flask(__name__)
app = Dash(__name__,
        plugins=[dl.plugins.pages],
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts, server=server)
