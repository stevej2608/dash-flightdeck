from dash import html
import pandas as pd
from components.dropdown_aio import DropdownAIO

from components.table_pagination_aoi import TableAIOPaginator, TableAIOPaginatorView


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

def data2Dict():

    # Convert TABLE_DATA CSV into dict of dicts. The returned primary dict has
    # an entry for each column who's values are the row values for the column
    # indexed on row number

    data = {}
    for col in TABLE_COLS: data[col] = {}

    for irow, row in enumerate(TABLE_DATA):
        for icol, value in enumerate(row.split(',')):
            colName = TABLE_COLS[icol]
            data[colName][irow] = value.strip()
    return data

df = pd.DataFrame.from_dict(data2Dict())

def _tableHead():
    return html.Thead([
        html.Tr([
            html.Th(colTitle, className='border-gray-200') for colTitle in df.columns
        ])
    ])


def _tableAction():

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

    return html.Div(DropdownAIO(button, container), className='btn-group')


def _tableRow(cid, product, issue_date, due_date, total, status, action=None):

    action = _tableAction()

    return html.Tr([
        html.Td(html.A(cid, href='#', className='fw-bold')),
        html.Td(html.Span(product, className='fw-normal')),
        html.Td(html.Span(issue_date, className='fw-normal')),
        html.Td(html.Span(due_date, className='fw-normal')),
        html.Td(html.Span(total, className='fw-bold')),
        html.Td(html.Span(status, className='fw-bold text-warning')),
        html.Td(action)
    ])

def _tableBody():
    rows = df.values.tolist()
    return html.Tbody([
        _tableRow(cid, product, issue_date, due_date, total, status, action) for cid, product, issue_date, due_date, total, status, action in rows
    ])


def create_paginator(range, current, max):
    store = TableAIOPaginator.createStore(range, current, max)

    def range_element(value):
        return html.Li([html.Span(value, className='page-link')], className='page-item')

    def content(current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]

    paginator = TableAIOPaginator(store, range_element, className='pagination mb-0')
    viewer = TableAIOPaginatorView(store, content=content, className='fw-normal small mt-4 mt-lg-0' )

    return html.Div([
        store,
        html.Nav(paginator),
        viewer
    ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')


def table():
    thead = _tableHead()
    tbody = _tableBody()
    paginator = create_paginator(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)
    return html.Div([
        html.Table([
            thead,
            tbody,
        ], className='table table-hover'),
        paginator
    ], className='card card-body border-0 shadow table-wrapper table-responsive')

