from dash import html, dcc
from dash_svg import Svg, Path

def searchIcon():
    return Svg([
        Path(fillRule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clipRule='evenodd')
    ], className='icon icon-xs', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 20 20', fill='currentColor', **{"aria-hidden": "true"})


def searchForm():
    return  html.Form([
        html.Div([
            html.Span([
                searchIcon()
            ], className='input-group-text', id='topbar-addon'),
            dcc.Input(type='text', className='form-control', id='topbarInputIconLeft', placeholder='Search')
        ], className='input-group input-group-merge search-bar')
    ], className='navbar-search form-inline', id='navbar-search-main')


def topNavBar():
    """"Top navbar, search form ..."""
    return html.Nav([
        html.Div([
            html.Div([
                html.Div([
                    searchForm()
                ], className='d-flex align-items-center')
            ], className='d-flex justify-content-between w-100', id='navbarSupportedContent')
        ], className='container-fluid px-0')
    ], className='navbar navbar-top navbar-expand navbar-dashboard navbar-dark ps-0 pe-2 pb-0')
