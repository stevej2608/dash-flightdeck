from dash import html, dcc
from dash_svg import Svg, Path

def mobileNavBar():
    """ Mobile only navbar - Volt logo & burger button """
    return html.Nav([
        html.A([
            html.Img(src='../assets/img/brand/light.svg', alt='Volt logo')
        ], className='navbar-brand me-lg-5', href='../index.html'),
        html.Div([
            html.Button([
                html.Span(className='navbar-toggler-icon')
            ], className='navbar-toggler d-lg-none collapsed', type='button', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "false", "aria-label": "Toggle navigation"})
        ], className='d-flex align-items-center')
    ], className='navbar navbar-dark navbar-theme-primary px-4 col-12 d-lg-none')
