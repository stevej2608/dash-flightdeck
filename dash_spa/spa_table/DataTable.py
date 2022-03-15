from typing import List, Dict, Any
from dash import html
from dash.development.base_component import Component

from dash_spa import prefix

TableColumns = List[Dict[str, Any]]

class TableRow(html.Tr):
    def __init__(self, Date, Region, Temperature, Humidity, Pressure):
        super().__init__([
            html.Td(html.A(Date, href='#', className='fw-bold')),
            html.Td(html.Span(Region, className='fw-normal')),
            html.Td(html.Span(Temperature, className='fw-normal')),
            html.Td(html.Span(Humidity, className='fw-normal')),
            html.Td(html.Span(Pressure, className='fw-bold'))
        ])

class TableBody(html.Tbody):
    def __init__(self, rows, id=None):
        pid = prefix(id)
        super().__init__([TableRow(**args) for args in rows], id=pid('tbody'))

class TableHead(html.Thead):
    def __init__(self, columns: TableColumns):
        row =  html.Tr([html.Th(col['name'], className='border-gray-200') for col in columns])
        super().__init__(row)


class Table(html.Table):
    def __init__(self, data: Dict, columns: TableColumns, thead: TableHead, tbody: TableBody, id=None, className=None):
        pid = prefix(id)

        thead = thead(columns)
        tbody = tbody(data, id=pid())

        super().__init__([thead, tbody], className=className)


class DataTable(html.Table):

    def __init__(
        self,
        data=Component.UNDEFINED,
        columns: TableColumns = Component.UNDEFINED,
        page_size: int = Component.UNDEFINED
    ):
        table = Table(data[0:page_size], columns, TableHead, TableBody)
        super().__init__(table)
