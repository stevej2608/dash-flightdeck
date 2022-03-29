from typing import List, Dict, Any
from dash import html, callback

from dash_spa import prefix
from components.dropdown_aio import DropdownAIO
from components.table import TableAIOPaginator, TableAIOPaginatorView

TableData = List[Dict[str, Any]]
TableColumns = List[Dict[str, Any]]

class TableAIO(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)

        self.paginator = self.tablePaginator(page=1, page_size=page_size, total_items=len(data))
        table = self.table(data, columns, page=1, page_size=page_size)
        super().__init__([table, self.paginator], className='card card-body border-0 shadow table-wrapper table-responsive')

    def table(self, data, columns: TableColumns, page=1, page_size = 10):
        thead = self.tableHead(columns)
        tbody = self.tableBody(data, page=1, page_size=page_size)
        table = html.Table([thead,tbody], className='table table-hover', id=self.pid('table'))

        if self.paginator:

            @callback(table.output.children, self.paginator.value)
            def _update_cb(paginator_state):
                state = self.paginator.state(paginator_state)
                tbody = self.tableBody(data, page=state.page, page_size=state.page_size)
                return [thead, tbody]

        return table

    def tableAction(self):
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


    def tableHead(self, columns: TableColumns):
        row =  html.Tr([html.Th(col['name'], className='border-gray-200') for col in columns])
        return html.Thead(row)

    def tableBody(self, data, page=1, page_size = 10):

        low = (page -1) * page_size
        high = (page) * page_size
        high = high if high < len(data) else len(data)
        data = data[low:high]
        return html.Tbody([self.tableRow(args) for args in data])

    def tableRow(self, args):

        cid, product, issue_date, due_date, total, status = args.values()
        action = self.tableAction()

        return html.Tr([
            html.Td(html.A(cid, href='#', className='fw-bold')),
            html.Td(html.Span(product, className='fw-normal')),
            html.Td(html.Span(issue_date, className='fw-normal')),
            html.Td(html.Span(due_date, className='fw-normal')),
            html.Td(html.Span(total, className='fw-bold')),
            html.Td(html.Span(status, className='fw-bold text-warning')),
            html.Td(action)
        ])

    def tablePaginator(self, page:int, page_size, total_items):

        paginator = TableAIOPaginator(page=page, page_size=page_size, total_items=total_items, className='pagination mb-0')
        viewer = TableAIOPaginatorView(paginator)

        class CompositePaginator(html.Div):

            @property
            def value(self):
                return self.paginator.store.input.data

            def __init__(self, paginator, viewer):
                self.paginator = paginator
                children = [html.Nav(paginator), viewer]
                super().__init__(children, className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')

            def state(self, state:dict = None):
                return self.paginator.state(state)

        return CompositePaginator(paginator, viewer)
