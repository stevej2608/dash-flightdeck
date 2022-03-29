from abc import abstractmethod
from typing import List, Dict, Any
from dash import html, callback

from dash_spa import prefix

TableData = List[Dict[str, Any]]
TableColumns = List[Dict[str, Any]]

class TableAIO(html.Div):

    TABLE_CLASS_NAME = ''

    def __init__(self, data: TableData, columns: TableColumns, page_size: int = None, id: str = None):
        self.pid = prefix(id)

        self.paginator = self.tablePaginator(page=1, page_size=page_size, total_items=len(data))
        table = self.table(data, columns, page=1, page_size=page_size)
        super().__init__([table, self.paginator], className=self.TABLE_CLASS_NAME)

    def table(self, data, columns: TableColumns, page=1, page_size = None):
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

    def tableHead(self, columns: TableColumns):
        row =  html.Tr([html.Th(col['name'], className='border-gray-200') for col in columns])
        return html.Thead(row)

    def tableBody(self, data, page=1, page_size = None):
        if page_size:
            low = (page -1) * page_size
            high = (page) * page_size
            high = high if high < len(data) else len(data)
            data = data[low:high]
        return html.Tbody([self.tableRow(args) for args in data])

    @abstractmethod
    def tableRow(self, args):
        return None

    def tablePaginator(self, page:int, page_size, total_items):
        return False
