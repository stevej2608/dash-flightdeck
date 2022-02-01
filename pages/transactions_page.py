import logging
from dash import html, dcc, register_page
from dash_svg import Svg, Path

from .components import sideBar, mobileNavBar, topNavBar, footer
from .transactions import breadCrumbs, table, tableHeader


register_page(__name__, path="/pages/transactions.html", title="Dash/Flightdeck - Transactions")


def layout():
    logging.info('layout()')
    return  html.Div([
        mobileNavBar(),
        sideBar(),
        html.Main([
            topNavBar(),
            breadCrumbs(),
            tableHeader(),
            table(),
            footer()
        ], className='content')
    ])
