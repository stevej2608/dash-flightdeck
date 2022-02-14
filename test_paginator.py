from dash import html
from app import create_app
from server import serve_app

from components.table_pagination_aoi import TableAIOPaginator, TableAIOPaginatorView


def create_paginator():
    store = TableAIOPaginator.createStore(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)

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


def layout():
    paginator1 = create_paginator()
    paginator2 = create_paginator()
    paginator3 = create_paginator()
    return html.Div([paginator1, paginator2, paginator3])


if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
