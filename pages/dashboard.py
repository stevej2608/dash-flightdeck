from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from flask import current_app

register_page(__name__, path="/")

def Card(content, title):
    return html.Div([
        html.Div([
            html.H5(title, className='card-header'),
            html.Div(content, className='card-body')
        ], className='card')
    ], className='col-12 col-md-6 mb-4 mb-lg-0 col-lg-3')


def OrdersTable():
    return html.Div([
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th('Order', scope='col'),
                    html.Th('Product', scope='col'),
                    html.Th('Customer', scope='col'),
                    html.Th('Total', scope='col'),
                    html.Th('Date', scope='col'),
                    html.Th(scope='col')
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ])
            ])
        ], className='table')
    ], className='table-responsive')


def layout():
    app = current_app.get_dash()
    return html.Div([
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
                html.Nav([
                    html.Div([
                        html.Ul([
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-home.svg"), className='feather feather-home', alt="home"),
                                    html.Span('Dashboard', className='ml-2')
                                ], className='nav-link active')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-file.svg"), className='feather feather-file', alt="file"),
                                    html.Span('Orders', className='ml-2')
                                ], className='nav-link', href='#')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-shopping-cart.svg"), className='feather feather-shopping-cart', alt="shopping-cart"),
                                    html.Span('Products', className='ml-2')
                                ], className='nav-link', href='#')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-users.svg"), className='feather feather-users', alt="users"),
                                    html.Span('Customers', className='ml-2')
                                ], className='nav-link', href='#')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-bar-chart-2.svg"), className='feather feather-bar-chart-2', alt="bar-chart-2"),
                                    html.Span('Reports', className='ml-2')
                                ], className='nav-link', href='#')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("feather-layers.svg"), className='feather feather-layers', alt="layers"),
                                    html.Span('Integrations', className='ml-2')
                                ], className='nav-link', href='#')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Img(src=app.get_asset_url("bi_book.svg"), className='bi-book', alt="book"),
                                    html.Span('Read tutorial', className='ml-2')
                                ], className='btn btn-sm btn-secondary ml-3 mt-2', href='https://themesberg.com/blog/bootstrap/simple-bootstrap-5-dashboard-tutorial')
                            ], className='nav-item'),
                            html.Li([
                                html.A('Volt Dashboard', className='btn btn-sm btn-warning ml-3 mt-2', href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard')
                            ], className='nav-item'),
                            html.Li([
                                html.A('By Themesberg', className='btn btn-sm btn-primary ml-3 mt-2', href='https://themesberg.com')
                            ], className='nav-item')
                        ], className='nav flex-column')
                    ], className='position-sticky')
                ], id='sidebar', className='col-md-3 col-lg-2 d-md-block bg-light sidebar collapse'),
                html.Main([
                    html.Nav([
                        html.Ol([
                            html.Li([
                                html.A('Home', href='#')
                            ], className='breadcrumb-item'),
                            html.Li('Overview', className='breadcrumb-item active')
                        ], className='breadcrumb')
                    ]),
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

                        html.Div([
                            html.Div([
                                html.H5('Latest transactions', className='card-header'),
                                html.Div([
                                    OrdersTable(),
                                    html.A('View all', href='#', className='btn btn-block btn-light')
                                ], className='card-body')
                            ], className='card')
                        ], className='col-12 col-xl-8 mb-4 mb-lg-0'),

                        html.Div([
                            html.Div([
                                html.H5('Traffic last 6 months', className='card-header'),
                                html.Div([
                                    html.Div(id='traffic-chart')
                                ], className='card-body')
                            ], className='card')
                        ], className='col-12 col-xl-4')


                    ], className='row'),


                    html.Footer([
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
                ], className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4')
            ], className='row')
        ], className='container-fluid')
    ])