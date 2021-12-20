from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from flask import current_app

from .navbar import Navbar
from .sidepanel import SidePanel
from .main_panel import MainPanel
from .footer import Footer

register_page(__name__, path="/")

def layout():
    return html.Div([
        Navbar(),
        html.Div([
            html.Div([
                SidePanel(),
                MainPanel(),
                Footer()
                ], className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4')
            ], className='row')
        ], className='container-fluid')
