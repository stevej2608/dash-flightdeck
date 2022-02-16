from typing import Callable, List
from dash import html, dcc, callback, ALL
from dash.exceptions import PreventUpdate
from dash_spa import match, prefix, isTriggered

from .table_aio import Dict2Obj

# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback


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
        data = Dict2Obj(store.data)

        def _range_element(text):
            rng = range_element(text)
            rng.id = range_match.idx(text)
            if text == data.current:
                rng.className += " active"
            return rng


        range_elements = [_range_element(text) for text in data.range]

        @callback(store.output.data,
                  range_match.output.className,
                  range_match.input.n_clicks,
                  store.state.data,
                  range_match.state.className)
        def update_paginator(clicks, data, className):

            if not any(clicks):
                raise PreventUpdate

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
