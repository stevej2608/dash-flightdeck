from dash import  dcc, html
import dash_bootstrap_components as dbc

def Brand():
    return html.Div([
        html.A('Simple Dashboard', className='navbar-brand', href='#'),
        html.Button([
            html.Span(className='navbar-toggler-icon')
        ], className='navbar-toggler d-md-none collapsed mb-3', type='button', tabIndex='collapse')
    ], className='d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between')

def Search():
    return  html.Div([
        dcc.Input(className='form-control form-control-dark', type='text', placeholder='Search')
    ], className='col-12 col-md-4 col-lg-2')

def UserMenu():
    return html.Div([
        dbc.DropdownMenu(
            label="Hello, John Doe",
            children=[
                dbc.DropdownMenuItem(html.A('Settings', className='dropdown-item', href='#')),
                dbc.DropdownMenuItem(html.A('Messages', className='dropdown-item', href='#')),
                dbc.DropdownMenuItem(html.A('Sign out', className='dropdown-item', href='#')),
            ], color="secondary")
    ], className='col-12 col-md-5 col-lg-8 d-flex align-items-center justify-content-md-end mt-3 mt-md-0')

def Navbar():
    return [
        Brand(),
        Search(),
        UserMenu()
    ]
