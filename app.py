import flask
from dash import Dash
import dash_labs as dl

import dash_bootstrap_components as dbc

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css",

    "https://use.fontawesome.com/releases/v5.4.1/css/all.css",
    "https://fonts.googleapis.com/css?family=Open+Sans:300,400"
    ]

external_scripts = [
    "https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js",
    "https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js",
    {'src': "https://buttons.github.io/buttons.js",'async': 'true', 'defer': 'true' }
    ]

# Server definition

server = flask.Flask(__name__)
app = Dash(__name__,
        plugins=[dl.plugins.pages],
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts, server=server)


# Allow pages to access the dash app instance, eg:
#
#  from flask import current_app
#
#  app = current_app.get_dash()

def get_dash():
    return app

server.get_dash = get_dash
