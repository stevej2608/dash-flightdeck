import flask
from dash import Dash
import dash_labs as dl

external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/chartist/0.3.1/chartist.min.css"
    ]

external_scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"
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
