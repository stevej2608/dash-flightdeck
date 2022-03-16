from typing import List, Dict, Any
from dash import html
from dash.development.base_component import Component

from dash_spa import prefix

TableColumns = List[Dict[str, Any]]

CELL_STYLE={"border-color": "rgb(211, 211, 211)", "border-style": "solid", "border-width": "1px"}

class TableRow(html.Tr):
    def __init__(self, Date, Region, Temperature, Humidity, Pressure):
        super().__init__([
            html.Td(html.A(Date, href='#'), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Region), className="dash-cell column-0",style=CELL_STYLE),
            html.Td(html.Span(Temperature), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Humidity), className="dash-cell column-0", style=CELL_STYLE),
            html.Td(html.Span(Pressure), className="dash-cell column-0", style=CELL_STYLE)
        ])

class TableBody(html.Tbody):
    def __init__(self, rows, id=None):
        pid = prefix(id)
        super().__init__([TableRow(**args) for args in rows], id=pid('tbody'))

class TableHead(html.Thead):
    def __init__(self, columns: TableColumns):
        row =  html.Tr([html.Th(col['name'], className="dash-header column-0 ", style=CELL_STYLE) for col in columns])
        super().__init__(row)


class Table(html.Table):
    def __init__(self, data: Dict, columns: TableColumns, thead: TableHead, tbody: TableBody, id=None, className='cell-table'):
        pid = prefix(id)

        thead = thead(columns)
        tbody = tbody(data, id=pid())

        super().__init__([thead, tbody], className=className)


class DataTable(html.Div):

    def __init__(
        self,
        data=Component.UNDEFINED,
        columns: TableColumns = Component.UNDEFINED,
        page_size: int = Component.UNDEFINED
    ):
        table = Table(data[0:page_size], columns, TableHead, TableBody)

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
