from typing import List, Dict, Any
from dash import html, dcc, callback
from dash.exceptions import PreventUpdate

from dash_spa import prefix, isTriggered
import math

TableData = List[Dict[str, Any]]
TableColumns = List[Dict[str, Any]]

class TablePaginator(html.Div):

    def __init__(self, rows: int, page_size: int, id: str = None):
        self.pid = prefix(id)
        self.page_size = page_size
        self.pages =  int(math.ceil(rows / page_size))
        self.store = dcc.Store(id=self.pid('store'), data={'current_page': 1})
        paginator = self.tablePaginator()
        super().__init__(paginator)


    def tablePaginator(self):

        def Button(icon, className):
            id = self.pid(className)
            return html.Button(html.I(className=icon), className=className, id=id)

        firstPage = Button("fas fa-angle-double-left","first-page")
        previousPage = Button("fas fa-angle-left","previous-page")
        nextPage = Button("fas fa-angle-right", "next-page")
        lastPage = Button("fas fa-angle-double-right", "last-page")

        pageInput = self.input(id=self.pid('input'))

        @callback(pageInput.output.value, self.store.output.data,
                  pageInput.input.value,
                  firstPage.input.n_clicks,previousPage.input.n_clicks,nextPage.input.n_clicks,lastPage.input.n_clicks,
                  self.store.input.data
                  )
        def button_callback(input, firstPageButton, previousPageButton, nextPageButton, lastPageButton, data):
            page = data['current_page']

            if isTriggered(firstPage.input.n_clicks):
                page = 1
            elif isTriggered(previousPage.input.n_clicks):
                page -= 1
            elif isTriggered(nextPage.input.n_clicks):
                page += 1
            elif isTriggered(lastPage.input.n_clicks):
                page = self.pages
            if isTriggered(pageInput.input.value):
                try:
                    input = int(input)
                    if input > 0 and input <= self.pages:
                        page = input
                except Exception:
                    pass

            data['current_page'] = page

            return page, data

        return html.Div([
            self.store,
            firstPage,
            previousPage,
            self.pageNumberLayout(pageInput),
            nextPage,
            lastPage
            ], className="previous-next-container")

    def pageNumberLayout(self, pageInput):
        style = self.inputStyle()
        current_page = self.store.data['current_page']
        return html.Div([
            html.Div([
                html.Div(current_page, className='current-page-shadow', style=style),
                pageInput,
            ], className='current-page-container'),
            "/",
            html.Div(self.pages, className='last-page', style=style)
        ], className='page-number')

    def input(self, id):
        style = self.inputStyle()
        return dcc.Input(className='current-page', placeholder='1', style=style, type='text', value='', id=id)

    def inputStyle(self):
        return {'min-width': '4ch'}


class DataTable(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)
        self.page_size = page_size
        table = self.table(data, columns)
        paginator = TablePaginator(len(data), self.page_size)
        table_container = self.tableContainer(table, paginator)
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
        return html.Table([thead, tbody], className=className)

    def tableHead(self, columns: TableColumns):
        style = self.cellStyle()
        row =  html.Tr([html.Th(col['name'], className="dash-header", style=style) for col in columns])
        return html.Thead(row)

    def tableBody(self, data: TableData):
        row_data = data[0:self.page_size]
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
