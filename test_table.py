from holoniq.utils import log
from dash import html, dcc, callback
from dash.exceptions import PreventUpdate
import pandas as pd

from app import create_app
from server import serve_app

from dash_spa import prefix

from components.store_aio import StoreAIO
from components.dropdown_aio import DropdownAIO
from components.button_container_aoi import ButtonContainerAIO

from components.table import TableAIOPaginator, TableAIOPaginatorView,  SearchAIO, filter_df

from icons.hero import TICK_ICON, GEAR_ICON


class TablePaginator(html.Div):

    def __init__(self):
        """Custom Paginator"""

        def range_element(value):
            return html.Li([html.Span(value, className='page-link')], className='page-item')

        paginator = TableAIOPaginator(["Previous", 1, 2, 3, 4, 5, "Next"], 1, 25, range_element, className='pagination mb-0')

        def content(current, max):
            return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]

        viewer = TableAIOPaginatorView(paginator.store, render_content=content, className='fw-normal small mt-4 mt-lg-0' )

        className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between'

        super().__init__([html.Nav(paginator), viewer], className=className)


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

        self.store = container.store

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
    def __init__(self, rows, id=None):
        pid = prefix(id)
        super().__init__([TableRow(*args) for args in rows], id=pid('tbody'))

class TableHead(html.Thead):
    def __init__(self, columns):
        row =  html.Tr([html.Th(title, className='border-gray-200') for title in columns])
        super().__init__(row)

class Table(html.Table):
    def __init__(self, df: pd.DataFrame, thead: TableHead, tbody: TableBody, id=None, search:dcc.Store = None, className=None):
        self.df = df
        pid = prefix(id)

        thead = thead(df.columns)
        tbody = tbody(df[0:5].values.tolist(), id=pid())

        # https://stackoverflow.com/questions/26640129/search-for-string-in-all-pandas-dataframe-columns-and-filter
        # ID eq 45697

        if search is not None:
            @callback(tbody.output.children, search.input.data)
            def _cb(value):

                log.info('value = [%s]', value)

                if value is None:
                    raise PreventUpdate

                value = value['search']

                if value is None:
                    raise PreventUpdate

                df = filter_df(self.df, value)
                rows = df[0:10].values.tolist()
                return [TableRow(*args) for args in rows]


        super().__init__([thead, tbody], className=className)

def table(df, search: dcc.Store, paginator: TablePaginator):

    return html.Div([
        Table(df, TableHead, TableBody, search=search, className='table table-hover'),
        paginator
    ], className='card card-body border-0 shadow table-wrapper table-responsive')


def pageHeader(search, settingsDropdown):
    return html.Div([
        html.Div([
            search,
            settingsDropdown,
        ], className='row align-items-center justify-content-between')
    ], className='table-settings mb-4')

def layout():

    df = pd.read_csv('data/subscriptions.csv')

    settingsDropdown = TableSetting()
    search = SearchAIO(placeholder='Search orders')
    paginator = TablePaginator()

    return html.Div([
        StoreAIO.container,
        html.Main([
            html.Div(className='d-flex py-4'),
            pageHeader(search, settingsDropdown),
            table(df, search.store, paginator),
        ], className='content')
    ])

if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
