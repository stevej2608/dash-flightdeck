from dash import html
from app import create_app
from server import serve_app

from components.table_pagination import TableAIOPagination, TableAIOPaginatorView


def layout():
    store = TableAIOPagination.createStore(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)

    def content(current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]

    paginator = TableAIOPagination(store, className='pagination mb-0')
    viewer = TableAIOPaginatorView(store, className='fw-normal small mt-4 mt-lg-0' , content=content)

    return html.Div([
        store,
        html.Nav(paginator),
        viewer
    ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')



if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
