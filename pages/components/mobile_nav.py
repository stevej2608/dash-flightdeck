from dash import html, dcc
from dash_svg import Svg, Path

def crossIcon():
    return  Svg([
        Path(d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z", fillRule="evenodd", clipRule="evenodd")
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def mobileNavBar():
    """ Mobile only navbar - Volt logo & burger button """
    return html.Nav([
        html.A([
            html.Img(className='navbar-brand-dark', src='../../assets/img/brand/light.svg', alt='Volt logo'),
            html.Img(className='navbar-brand-light', src='../../assets/img/brand/dark.svg', alt='Volt logo')
        ], className='navbar-brand me-lg-5', href='../../index.html'),
        html.Div([
            html.Button([

                # Burger button

                html.Span(className='navbar-toggler-icon')

            ], className='navbar-toggler d-lg-none collapsed', type='button', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "false", "aria-label": "Toggle navigation"})
        ], className='d-flex align-items-center')
    ], className='navbar navbar-dark navbar-theme-primary px-4 col-12 d-lg-none')


def mobileSidebarHeader():
    """ Mobile only sidebar header"""
    return html.Div([
        html.Div([
            # Snip avatar
            html.Div([
                # Snip Hi, Jane
                html.A([
                    html.Img(className='icon icon-sm', src='../../assets/img/icons/sign_out.svg', height='20', width='20', alt='upgrade'),
                    "Sign Out"
                ], href='../../pages/examples/sign-in.html', className='btn btn-secondary btn-sm d-inline-flex align-items-center')
            ], className='d-block')
        ], className='d-flex align-items-center'),

        # Sidebar close [X] icon

        html.Div([
            html.A([
                crossIcon(),
            ], href='#sidebarMenu', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "true", "aria-label": "Toggle navigation"})
        ], className='collapse-close d-md-none')

    ], className='user-card d-flex d-md-none align-items-center justify-content-between justify-content-md-center pb-4')
