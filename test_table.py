from dash import html
from app import create_app
from server import serve_app
import pandas as pd

from components.store_aio import StoreAIO
from components.dropdown_aio import DropdownAIO
from test_paginator import create_paginator


class TableActionAIO(html.Div):
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
        action = TableActionAIO()
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

def layout():

    df = pd.read_csv('data/subscriptions.csv')
    paginator = create_paginator(["Previous", 1, 2, 3, 4, 5, "Next"], 1, 25)

    return html.Div([
        StoreAIO.container,
        Table(df, TableHead, TableBody, className='table table-hover'),
        paginator
    ], className='card card-body border-0 shadow table-wrapper table-responsive')



if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)

