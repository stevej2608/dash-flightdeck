from typing import List, Dict, Any
from dash import html

from dash_spa import prefix

TableData = List[Dict[str, Any]]

TableColumns = List[Dict[str, Any]]

CELL_STYLE={"border-color": "rgb(211, 211, 211)", "border-style": "solid", "border-width": "1px"}

class DataTable(html.Div):

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):

        self.pid = prefix(id)

        table = self.table(data[0:page_size], columns)

        spreadsheet_inner = html.Div(table,
            className="dash-spreadsheet-inner dash-spreadsheet dash-empty-01 dash-no-filter dash-fill-width",
            style={'min-height': '100%', 'min-width': '100%'}
            )

        spreadsheet_container = html.Div(spreadsheet_inner,
            className='dash-spreadsheet-container dash-spreadsheet dash-empty-01 dash-no-filter dash-fill-width',
            style={"width": "100%"}
            )

        table_container = html.Div(spreadsheet_container,
            className="dash-table-container",
            style={"position": "relative"}
            )

        super().__init__(table_container)

    def table(self, data: TableData, columns: TableColumns, id=None, className='cell-table'):
        pid = prefix(id)
        thead = self.tableHead(columns)
        tbody = self.tableBody(data)
        return html.Table([thead, tbody], className=className)

    def tableHead(self, columns: TableColumns):
        row =  html.Tr([html.Th(col['name'], className="dash-header column-0 ", style=CELL_STYLE) for col in columns])
        return html.Thead(row)

    def tableBody(self, rows):
        return html.Tbody([self.tableRow(**args) for args in rows], id=self.pid('tbody'))

    def tableRow(self, Date, Region, Temperature, Humidity, Pressure):
        return html.Tr([
            html.Td(html.A(Date, href='#'), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Region), className="dash-cell column-0",style=CELL_STYLE),
            html.Td(html.Span(Temperature), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Humidity), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Pressure), className="dash-cell column-0", style=CELL_STYLE)
        ])
