from dash import html
from holoniq.utils import log
from app import create_app
from server import serve_app

from components.table_pagination import TableAIOPagination

layout = html.Div([
    TableAIOPagination(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)
])


if __name__ == "__main__":
    app = create_app(layout, plugins=[])
    serve_app(app, debug=False)
