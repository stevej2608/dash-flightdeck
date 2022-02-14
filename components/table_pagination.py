from typing import Callable, List
from dash import html, dcc, callback, ALL, callback_context
from dash.exceptions import PreventUpdate
from dash_spa import match, prefix, isTriggered

# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback


class Dict2Obj:
    def __init__(self, d=dict) -> object:
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)

class TableAIOPaginator(html.Ul):

    @staticmethod
    def createStore(range: List, current:str, max:str, aio_id=None) -> dcc.Store:
        """Create a dcc.Store component for use by TableAIOPaginator

        Args:
            range (List): Range of values to be displayed by TableAIOPaginator
            current (str): The currently selected value
            max (str): The maximum selectable value
            aio_id (_type_, optional): _description_. Defaults to None.

        Returns:
            dcc.Store: The store component
        """

        pid = prefix(aio_id)
        store_date = {'range': range, 'current': current, 'max': max}
        return dcc.Store(id=pid(), data=store_date)


    def __init__(self, store: dcc.Store, range_element: Callable, className: str = None):
        """Creates and manages a pagination UI AIO component. The supplied store
        data range entries are are itterated, the range_element is called for each
        value

        Args:
            store (dcc.Store): Store is updated when the user clicks on a range UI component
            range_element (Callable): Renders a range entry from the store
            className (str, optional): The TableAIOPaginator className. Defaults to None.

        Returns:
            html.Ui: The range AOI component

        Example:

            store = TableAIOPaginator.createStore(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)

            def range_element(value):
                return html.Li([html.Span(value, className='page-link')], className='page-item')

            paginator = TableAIOPaginator(store, range_element, className='pagination mb-0')

        """

        pid = prefix(store.id)

        range_match = match({'type': pid('li'), 'idx': ALL})

        def _range_element(text):
            rng = range_element(text)
            rng.id = range_match.idx(text)
            return rng

        data = Dict2Obj(store.data)

        range_elements = [_range_element(text) for text in data.range]

        @callback(store.output.data,
                  range_match.output.className,
                  range_match.input.n_clicks,
                  store.state.data,
                  range_match.state.className)
        def update_paginator(clicks, data, className):

            # Set the selected element to active and update
            # store.data['current'] with the selected value

            range_out = []
            for index, range_element in enumerate(range_elements):
                classNames = className[index].split()

                # Deactivate previously active

                if 'active' in classNames:
                    classNames.remove('active')

                if isTriggered(range_element.input.n_clicks):
                    classNames.append('active')
                    data['current'] = range_elements[index].id['idx']

                range_out.append(' '.join(classNames))

            return data, range_out

        super().__init__(range_elements, id=pid('TableAIOPaginator'), className=className)


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
