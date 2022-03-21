from dash import html
from app import create_app
from server import serve_app

from components.store_aio import StoreAIO
from components.table import TableAIOPaginator, TableAIOPaginatorView


def create_paginator(range, current, max):

    def range_element(value):
        return html.Li([html.Span(value, className='page-link')], className='page-item')

    paginator = TableAIOPaginator(range, current, max, range_element, className='pagination mb-0')

    def content(current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]

    viewer = TableAIOPaginatorView(paginator.store, render_content=content, className='fw-normal small mt-4 mt-lg-0' )

    return html.Div([
        html.Nav(paginator),
        viewer
    ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')


def layout():
    paginator1 = create_paginator(["Previous", 1, 2, 3, 4, 5, "Next"], 1, 25)
    paginator2 = create_paginator(["Begin", 1, 2, 3, 4, 5, "End"], 3, 20)
    paginator3 = create_paginator(["Previous", 1, 2, 3, 4, 5, 6, 7, "Next"], 7, 50)
    return html.Div([StoreAIO.container, paginator1, paginator2, paginator3])


if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
