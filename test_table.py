from dash import html
from app import create_app
from server import serve_app
import pandas as pd

from components.store_aio import StoreAIO
from components.dropdown_aio import DropdownAIO
from test_paginator import create_paginator


TABLE_COLS = ["#", "Bill For", "Issue Date", "Due Date", "Total", "Status", "Action"]

TABLE_DATA = [
    "456478,Platinum Subscription Plan,1 May 2020,1 Jun 2020,$799.00, Due",
    "456423,Platinum Subscription Plan,1 Apr 2020,1 May 2020,$799.00, Paid",
    "456420,Platinum Subscription Plan,1 Mar 2020,1 Apr 2020,$799.00, Paid",
    "456421,Platinum Subscription Plan,1 Feb 2020,1 Mar 2020,$799.00, Paid",
    "456420,Platinum Subscription Plan,1 Jan 2020,1 Feb 2020,$799.00, Paid",
    "456479,Platinum Subscription Plan,1 Dec 2019,1 Jan 2020,$799.00, Paid",
    "456478,Platinum Subscription Plan,1 Nov 2019,1 Dec 2019,$799.00, Paid",
    "453673,Gold Subscription Plan,1 Oct 2019,1 Nov 2019, $533.42, Cancelled",
    "456468,Gold Subscription Plan,1 Sep 2019,1 Oct 2019, $533.42, Paid",
    "456478,Flexible Subscription Plan,1 Aug 2019,1 Sep 2019, $233.42,  Paid",
]

def data2Dict(cols, row_data):

    # Convert TABLE_DATA CSV into dict of dicts. The returned primary dict has
    # an entry for each column who's values are the row values for the column
    # indexed on row number

    data = {}
    for col in cols: data[col] = {}

    for irow, row in enumerate(row_data):
        for icol, value in enumerate(row.split(',')):
            colName = cols[icol]
            data[colName][irow] = value.strip()
    return data

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
        tbody = tbody(df.values.tolist())
        super().__init__([thead, tbody], className=className)

def layout():

    df = pd.DataFrame.from_dict(data2Dict(TABLE_COLS, TABLE_DATA))
    paginator = create_paginator(["Previous", 1, 2, 3, 4, 5, "Next"], 1, 25)

    return html.Div([
        StoreAIO.container,
        Table(df, TableHead, TableBody, className='table table-hover'),
        paginator
    ], className='card card-body border-0 shadow table-wrapper table-responsive')



if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
