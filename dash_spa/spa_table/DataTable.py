from typing import List, Dict, Any
from dash import html, dcc, callback
from dash.exceptions import PreventUpdate

from dash_spa import prefix, isTriggered, NOUPDATE
import math

TableData = List[Dict[str, Any]]
TableColumns = List[Dict[str, Any]]

class TablePaginator(html.Div):

    def __init__(self, rows: int, page_size: int, id: str = None):
        pid = prefix(id)

        def Button(icon, className):
            return html.Button(html.I(className=icon), className=className, id=pid(className))

        self.page_size = page_size
        self.pages =  int(math.ceil(rows / page_size))
        self.store = dcc.Store(id=pid('store'), data={'current_page': 1})

        firstPage = Button("fas fa-angle-double-left","first-page")
        previousPage = Button("fas fa-angle-left","previous-page")
        nextPage = Button("fas fa-angle-right", "next-page")
        lastPage = Button("fas fa-angle-double-right", "last-page")

        style = {'min-width': '4ch'}
        pageInput = dcc.Input(className='current-page', placeholder='1', style=style, type='text', value='', id=pid('input'))
        pageInputShadow = html.Div(1, className='current-page-shadow', style=style, id=pid('input-shadow'))

        @callback(self.store.output.data,

                  pageInputShadow.output.children,
                  pageInput.output.placeholder,
                  pageInput.output.value,

                  firstPage.input.n_clicks,
                  previousPage.input.n_clicks,
                  nextPage.input.n_clicks,
                  lastPage.input.n_clicks,

                  pageInput.input.n_submit,

                  pageInput.state.value,
                  self.store.state.data)

        def _paginator_cb(firstPageButton, previousPageButton, nextPageButton, lastPageButton, submit, value, data):
            update = False
            page = data['current_page']

            if isTriggered(firstPage.input.n_clicks):
                page = 1
                update = True
            elif isTriggered(previousPage.input.n_clicks) and page > 1:
                page -= 1
                update = True
            elif isTriggered(nextPage.input.n_clicks) and page < self.pages:
                page += 1
                update = True
            elif isTriggered(lastPage.input.n_clicks):
                page = self.pages
                update = True
            if isTriggered(pageInput.input.n_submit):
                try:
                    update = True
                    input = int(value)
                    if input > 0 and input <= self.pages:
                        page = input
                except Exception:
                    pass

            if not update:
                raise PreventUpdate

            data['current_page'] = page

            return data, page, page, ""


        paginator = [
            self.store,
            firstPage,
            previousPage,
            self.pageNumberLayout(pageInput, pageInputShadow, style),
            nextPage,
            lastPage
            ]

        super().__init__(paginator, className="previous-next-container")

    def pageNumberLayout(self, pageInput, pageInputShadow, style):
        current_page = self.store.data['current_page']
        return html.Div([
            html.Div([
                pageInputShadow,
                pageInput,
            ], className='current-page-container'),
            "/",
            html.Div(self.pages, className='last-page', style=style)
        ], className='page-number')


class DataTable(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)
        self.page_size = page_size
        self.paginator = TablePaginator(len(data), self.page_size)
        table = self.table(data, columns)
        table_container = self.tableContainer(table, self.paginator)
        super().__init__(table_container)

    def tableContainer(self, table, paginator):
        spreadsheet_inner = html.Div(table,
            className="dash-spreadsheet-inner dash-spreadsheet dash-empty-01 dash-no-filter dash-fill-width",
            style={'min-height': '100%', 'min-width': '100%'}
            )

        spreadsheet_container = html.Div(spreadsheet_inner,
            className='dash-spreadsheet-container dash-spreadsheet dash-empty-01 dash-no-filter dash-fill-width',
            style={"width": "100%"}
            )

        table_container = html.Div([spreadsheet_container, paginator],
            className="dash-table-container",
            style={"position": "relative"}
            )

        return table_container

    def table(self, data: TableData, columns: TableColumns, id=None, className='cell-table'):
        pid = prefix(id)
        thead = self.tableHead(columns)
        tbody = self.tableBody(data)
        table = html.Table([thead, tbody], className=className, id = self.pid('table'))

        @callback(table.output.children, self.paginator.store.input.data)
        def _update_cb(paginator):
            page = paginator['current_page']
            tbody = self.tableBody(data, page)
            return [thead, tbody]

        return table

    def tableHead(self, columns: TableColumns):
        style = self.cellStyle()
        row =  html.Tr([html.Th(col['name'], className="dash-header", style=style) for col in columns])
        return html.Thead(row)

    def tableBody(self, data: TableData, page: int = 1):
        low = (page -1) * self.page_size
        high = (page) * self.page_size
        row_data = data[low:high]
        return html.Tbody([self.tableRow(**args) for args in row_data], id=self.pid('tbody'))

    def tableRow(self, Date, Region, Temperature, Humidity, Pressure):
        style = self.cellStyle()
        return html.Tr([
            html.Td(html.A(Date, href='#'), className="dash-cell", style=style),
            html.Td(html.Span(Region), className="dash-cell",style=style),
            html.Td(html.Span(Temperature), className="dash-cell", style=style),
            html.Td(html.Span(Humidity), className="dash-cell", style=style),
            html.Td(html.Span(Pressure), className="dash-cell", style=style)
        ])

    def cellStyle(self):
        return {"border-color": "rgb(211, 211, 211)", "border-style": "solid", "border-width": "1px"}
