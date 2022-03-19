from typing import List, Dict, Any
from dash import html, callback

from dash_spa import prefix
from .TablePaginator import TablePaginator

TableData = List[Dict[str, Any]]
TableColumns = List[Dict[str, Any]]

class DataTable(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)
        self.page_size = page_size
        self.paginator = self.tablePaginator(len(data), self.page_size)
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

        @callback(table.output.children, self.paginator.value)
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
        high = high if high < len(data) else len(data)

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

    def tablePaginator(self, rows:int, page_size):
        return TablePaginator(rows, page_size)
