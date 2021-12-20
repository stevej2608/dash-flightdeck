from dash import  html
import dash_bootstrap_components as dbc

from .orders_table import OrdersTable

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


def MainPanel():
    return html.Main([
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
        ], className='row')
    ])