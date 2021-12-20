from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from flask import current_app

from .orders_table import OrdersTable

register_page(__name__, path="/")

def Card(content, title, className='col-12 col-md-6 mb-4 mb-lg-0 col-lg-3'):
    return html.Div([
        dbc.Card([
            html.H5(title, className='card-header'),
            html.Div(content, className='card-body')
        ])
    ], className=className)

def BreadCrumb():
    return  html.Nav([
        html.Ol([
            html.Li([
                html.A('Home', href='#')
            ], className='breadcrumb-item'),
            html.Li('Overview', className='breadcrumb-item active')
        ], className='breadcrumb')
    ])


def Footer():
    return html.Footer([
        html.Span([
            'Copyright © 2019-2020 ',
            html.A('Themesberg', href='https://themesberg.com')
        ]),
        html.Ul([
            html.Li([
                html.A('Privacy Policy', className='nav-link text-secondary')
            ], className='nav-item'),
            html.Li([
                html.A('Terms and conditions', className='nav-link text-secondary', href='#')
            ], className='nav-item'),
            html.Li([
                html.A('Contact', className='nav-link text-secondary', href='#')
            ], className='nav-item')
        ], className='nav m-0')
    ], className='pt-5 d-flex justify-content-between')


def SideLink(title, icon=None, alt=None, active=False, href="#"):
    app = current_app.get_dash()
    active = " active" if active else ""
    return  html.Li([
        html.A([
            html.Img(src=app.get_asset_url(icon), className='feather feather-home', alt=alt),
            html.Span(title, className='ml-2')
        ], href=href, className='nav-link' + active)
    ], className='nav-item')

def SideButton(title, href="#", btn_style="btn-secondary"):
    return html.Li([
        html.A(title, className=f'btn btn-sm {btn_style} ml-3 mt-2', href=href)
    ], className='nav-item')

def SideIconButton(title, icon=None, alt=None, href="#", btn_style="btn-secondary"):
    app = current_app.get_dash()
    return html.Li([
        html.A([
            html.Img(src=app.get_asset_url(icon), className='bi-book', alt=alt),
            html.Span(title, className='ml-2')
        ], className=f'btn btn-sm {btn_style} ml-3 mt-2', href=href)
    ], className='nav-item')


def layout():
    app = current_app.get_dash()
    return html.Div([

        # Top navbar - Title, Search, User

        html.Nav([

            html.Div([
                html.A('Simple Dashboard', className='navbar-brand', href='#'),
                html.Button([
                    html.Span(className='navbar-toggler-icon')
                ], className='navbar-toggler d-md-none collapsed mb-3', type='button', tabIndex='collapse')
            ], className='d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between'),

            html.Div([
                dcc.Input(className='form-control form-control-dark', type='text', placeholder='Search')
            ], className='col-12 col-md-4 col-lg-2'),

            html.Div([
                dbc.DropdownMenu(
                    label="Hello, John Doe",
                    children=[
                        dbc.DropdownMenuItem(html.A('Settings', className='dropdown-item', href='#')),
                        dbc.DropdownMenuItem(html.A('Messages', className='dropdown-item', href='#')),
                        dbc.DropdownMenuItem(html.A('Sign out', className='dropdown-item', href='#')),
                    ], color="secondary")
            ], className='col-12 col-md-5 col-lg-8 d-flex align-items-center justify-content-md-end mt-3 mt-md-0')
        ], className='navbar navbar-light bg-light p-3'),

        html.Div([
            html.Div([

                # Side panel

                html.Nav([
                    html.Div([

                        html.Ul([
                            SideLink('Dashboard', icon="feather-home.svg", alt="home", active=True),
                            SideLink('Orders', icon="feather-file.svg", alt="file"),
                            SideLink('Products', icon="feather-shopping-cart.svg", alt="shopping-cart"),
                            SideLink('Customers', icon="feather-users.svg", alt="users"),
                            SideLink('Reports', icon="feather-bar-chart-2.svg", alt="bar-chart-2"),
                            SideLink('Integrations', icon="feather-layers.svg", alt="layers"),
                            SideIconButton('Read tutorial', icon="bi_book.svg", alt="book", href='https://themesberg.com/blog/bootstrap/simple-bootstrap-5-dashboard-tutorial'),
                            SideButton('Volt Dashboard', btn_style='btn-warning', href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard'),
                            SideButton('By Themesberg', btn_style='btn-primary', href='https://themesberg.com')
                        ], className='nav flex-column')

                    ], className='position-sticky')
                ], id='sidebar', className='col-md-3 col-lg-2 d-md-block bg-light sidebar collapse'),

                # Main panel

                html.Main([
                    BreadCrumb(),

                    html.H1('Dashboard', className='h2'),
                    html.P('This is the homepage of a simple admin interface which is part of a tutorial written on Themesberg'),

                    html.Div([
                        Card([
                            html.H5('345k', className='card-title'),
                            html.P('Feb 1 - Apr 1, United States', className='card-text'),
                            html.P('18.2% increase since last month', className='card-text text-success')
                        ], 'Customers'),
                        Card([
                            html.H5('$2.4k', className='card-title'),
                            html.P('Feb 1 - Apr 1, United States', className='card-text'),
                            html.P('4.6% increase since last month', className='card-text text-success')
                        ], 'Revenue'),
                        Card([
                            html.H5('43', className='card-title'),
                            html.P('Feb 1 - Apr 1, United States', className='card-text'),
                            html.P('2.6% decrease since last month', className='card-text text-danger')
                        ], 'Purchases'),

                        Card([
                            html.H5('64k', className='card-title'),
                            html.P('Feb 1 - Apr 1, United States', className='card-text'),
                            html.P('2.5% increase since last month', className='card-text text-success')
                        ], 'Traffic'),
                    ], className='row my-4'),

                    html.Div([
                        Card([
                            OrdersTable(),
                            html.A('View all', href='#', className='btn btn-block btn-light')
                        ], title='Latest transactions', className='col-12 col-xl-8 mb-4 mb-lg-0'),
                        Card([
                            html.Div(id='traffic-chart')
                        ], title='Traffic last 6 months', className='col-12 col-xl-4'),
                    ], className='row'),

                    Footer()

                ], className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4')
            ], className='row')
        ], className='container-fluid')
    ])
