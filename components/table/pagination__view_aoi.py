from typing import Callable
from dash import html, dcc, callback
from dash.exceptions import PreventUpdate
from dash_spa import prefix

from .table_aio import Dict2Obj

class TableAIOPaginatorView(html.Div):

    def __init__(self, store: dcc.Store, content: Callable, className= None):
        """Manages and updates the view component of the associated
        TableAIOPaginator. The TableAIOPaginatorView callback is triggered when the
        store component value changes. The callback calls the supplied
        'content' function. The function return value is rendered as the child
        element of the TableAIOPaginatorView

        Args:
            store (dcc.Store): The store element that is updated by the paginator
            content (Callable): Function used to update the component children
            className (str): the className of the component

        Returns:
            html.Div: The view component

        Example:

            store = TableAIOPaginator.createStore(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)

            def content(current, max):
                return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]

            viewer = TableAIOPaginatorView(store, content, className='fw-normal small mt-4 mt-lg-0' )

        """
        pid = prefix(store.id)
        s = Dict2Obj(store.data)

        super().__init__(content(s.current, s.max), id=pid('TableAIOPaginatorView'), className=className)

        @callback(self.output.children, store.input.data)
        def update_view(data):

            if data is not None:
                s = Dict2Obj(data)
                return content(s.current, s.max)

            raise PreventUpdate
