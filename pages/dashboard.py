from dash import html, register_page

from .navbar import Navbar
from .side_panel import SidePanel
from .main_panel import MainPanel
from .footer import Footer

register_page(__name__, path="/")

# https://getbootstrap.com/docs/5.1/layout/grid/
# https://www.freecodecamp.org/news/semantic-html5-elements/
# https://css-tricks.com/snippets/css/a-guide-to-flexbox/#flexbox-background

def layout():
    return html.Div([
        html.Nav(Navbar(), className='navbar navbar-light bg-light p-3'),
        html.Div([
            html.Div([
                html.Nav(SidePanel(), className='col-md-3 col-lg-2 d-md-block bg-light sidebar collapse'),
                html.Main(MainPanel()),
                html.Footer(Footer(), className='pt-5 d-flex justify-content-between')
                ], className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4')
            ], className='row')
        ], className='container-fluid')
