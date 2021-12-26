from dash import  dcc, html
import dash_bootstrap_components as dbc

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
        Search(),
        UserMenu()
    ]
