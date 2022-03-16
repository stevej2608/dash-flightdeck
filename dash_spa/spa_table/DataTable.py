from typing import List, Dict, Any
from dash import html, dcc

from dash_spa import prefix

TableData = List[Dict[str, Any]]

TableColumns = List[Dict[str, Any]]

class DataTable(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)
        self.page_size = page_size
        table = self.table(data, columns)
        paginator = self.tablePaginator()
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

    def tablePaginator(self):
        firstPageButton = html.Button(html.I(className="fas fa-angle-double-left"), className="first-page")
        previousPageButton = html.Button(html.I(className="fas fa-angle-left"), className="previous-page")
        nextPageButton = html.Button(html.I(className="fas fa-angle-right"), className="next-page")
        lastPageButton = html.Button(html.I(className="fas fa-angle-double-right"), className="last-page")
        pageNumber = self.pageNumber()
        return html.Div([
            firstPageButton,
            previousPageButton,
            pageNumber,
            nextPageButton,
            lastPageButton
            ], className="previous-next-container")

    def pageNumber(self):
        style={'min-width': '4ch'}
        pageInput = dcc.Input(className='current-page', placeholder='1', style=style, type='text', value='')
        return html.Div([
            html.Div([
                html.Div("1", className='current-page-shadow', style=style),
                pageInput,
            ], className='current-page-container'),
            "/",
            html.Div("6", className='last-page', style=style)
        ], className='page-number')

    def cellStyle(self):
        return {"border-color": "rgb(211, 211, 211)", "border-style": "solid", "border-width": "1px"}
