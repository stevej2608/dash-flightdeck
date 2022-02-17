from dash import html
from app import create_app
from server import serve_app
import pandas as pd

from components.store_aio import StoreAIO
from components.dropdown_aio import DropdownAIO
from components.button_container_aoi import ButtonContainerAIO
from test_paginator import create_paginator

from icons.hero import TICK_ICON, GEAR_ICON
from pages.transactions.table_header import _searchOrders

class TableSetting(html.Div):

    def __init__(self):

        button = DropdownAIO.Button([
        GEAR_ICON,html.Span("Toggle Dropdown", className='visually-hidden')
        ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-1')


        def element_renderer(value, selected):
            if selected:
                element = html.Div([value, TICK_ICON], className = 'dropdown-item d-flex align-items-center fw-bold')
            else:
                element = html.Div([value], className = 'dropdown-item fw-bold')

            if value == "30":
                element.className += ' rounded-bottom'

            return element

        container = ButtonContainerAIO(["10", "20", "30"], "10", element_renderer, className='dropdown-menu dropdown-menu-xs dropdown-menu-end pb-0')
        container.children[0:0] = [html.Span("Show", className='small ps-3 fw-bold text-dark')]

        dropdown = DropdownAIO(button, container)

        super().__init__(dropdown, className='col-4 col-md-2 col-xl-1 ps-md-0 text-end')


class RowActionAIO(html.Div):
    def __init__(self):
        button = DropdownAIO.Button([
            html.Span(html.Span(className='fas fa-ellipsis-h icon-dark'), className='icon icon-sm'),
            html.Span("Toggle Dropdown", className='visually-hidden')
        ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0')

        # dropdown bottom-left. Ripped from the Volt transactons table using Firefox debug tools

        style={"position": "absolute",
                "inset": "0px 0px auto auto",
                "margin": "0px",
                "transform": "translate3d(0px, 25.3333px, 0px)"
                }

        container = html.Div([
            html.A([html.Span(className='fas fa-eye me-2'), "View Details" ], className='dropdown-item rounded-top', href='#'),
            html.A([html.Span(className='fas fa-edit me-2'), "Edit"], className='dropdown-item', href='#'),
            html.A([html.Span(className='fas fa-trash-alt me-2'), "Remove" ], className='dropdown-item text-danger rounded-bottom', href='#')
        ], className='dropdown-menu py-0', style=style)

        super().__init__(DropdownAIO(button, container), className='btn-group')


class TableRow(html.Tr):
    def __init__(self, cid, product, issue_date, due_date, total, status, action=None):
        action = RowActionAIO()
        super().__init__([
            html.Td(html.A(cid, href='#', className='fw-bold')),
            html.Td(html.Span(product, className='fw-normal')),
            html.Td(html.Span(issue_date, className='fw-normal')),
            html.Td(html.Span(due_date, className='fw-normal')),
            html.Td(html.Span(total, className='fw-bold')),
            html.Td(html.Span(status, className='fw-bold text-warning')),
            html.Td(action)
        ])

class TableBody(html.Tbody):
    def __init__(self, rows):
        super().__init__([TableRow(*args) for args in rows])

class TableHead(html.Thead):
    def __init__(self, columns):
        row =  html.Tr([html.Th(title, className='border-gray-200') for title in columns])
        super().__init__(row)

class Table(html.Table):
    def __init__(self, df, thead, tbody, className=None):
        thead = thead(df.columns)
        tbody = tbody(df[0:5].values.tolist())
        super().__init__([thead, tbody], className=className)

def table():
    df = pd.read_csv('data/subscriptions.csv')
    paginator = create_paginator(["Previous", 1, 2, 3, 4, 5, "Next"], 1, 25)
    return html.Div([
        Table(df, TableHead, TableBody, className='table table-hover'),
        paginator
    ], className='card card-body border-0 shadow table-wrapper table-responsive')


def pageHeader(settingsDropdown):
    return html.Div([
        html.Div([
            _searchOrders(),
            settingsDropdown,
        ], className='row align-items-center justify-content-between')
    ], className='table-settings mb-4')

def layout():

    df = pd.read_csv('data/subscriptions.csv')
    settingsDropdown = TableSetting()

    return html.Div([
        StoreAIO.container,
        html.Main([
            html.Div(className='d-flex py-4'),
            pageHeader(settingsDropdown),
            table(),
        ], className='content')
    ])

if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)

