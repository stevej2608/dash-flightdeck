from typing import Callable, List
from dash import html, callback, ALL
from dash.exceptions import PreventUpdate
from dash_spa import match, prefix, isTriggered
from components.store_aio import StoreAIO

from .table_aio import Dict2Obj

# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback


class TableAIOPaginator(html.Ul):
    """Creates and manages a pagination UI AIO component. The supplied store
    data range entries are are itterated, the range_element is called for each
    value

    Args:
        range (List): Range of values to be displayed by TableAIOPaginator
        current_page (str): The currently selected value
        max (str): The maximum selectable value
        range_element (Callable): Renders a range entry from the store
        className (str, optional): The TableAIOPaginator className. Defaults to None.
        aio_id (_type_, optional): _description_. Defaults to None.

    Returns:
        html.Ui: The range AOI component

    Example:

        store = TableAIOPaginator.createStore(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)

        def range_element(value):
            return html.Li([html.Span(value, className='page-link')], className='page-item')

        paginator = TableAIOPaginator(store, range_element, className='pagination mb-0')

    Markup:
    ```
        <ul class="pagination mb-0" >
            <li class="page-item"><span class="page-link">Previous</span></li>
            <li class="page-item active""><span class="page-link">1</span></li>
            <li class="page-item"><span class="page-link">2</span></li>
            <li class="page-item"><span class="page-link">3</span></li>
            <li class="page-item"><span class="page-link">4</span></li>
            <li class="page-item"><span class="page-link">5</span></li>
            <li class="page-item"><span class="page-link">Next</span></li>
        </ul>
    ```

    """

    @property
    def state(self):
        return self.store.state.data

    @property
    def value(self):
        return self.store.input.data

    def __init__(self, range: List, current_page:str, max:str, range_element: Callable, className: str = None, aio_id=None):

        self.store = StoreAIO.create_store({'range': range, 'current_page': current_page, 'max': max}, aio_id)

        pid = prefix(self.store.id)

        range_match = match({'type': pid('li'), 'idx': ALL})
        data = Dict2Obj(self.store.data)

        def _range_element(text):
            rng = range_element(text)
            rng.id = range_match.idx(text)
            if text == data.current_page:
                rng.className += " active"
            return rng


        range_elements = [_range_element(text) for text in data.range]

        @callback(self.store.output.data,
                  range_match.output.className,
                  range_match.input.n_clicks,
                  self.store.state.data,
                  range_match.state.className)
        def update_paginator(clicks, data, className):

            if not any(clicks):
                raise PreventUpdate

            # Set the selected element to active and update
            # store.data['current_page'] with the selected value

            range_out = []
            for index, range_element in enumerate(range_elements):
                classNames = className[index].split()

                # Deactivate previously active

                if 'active' in classNames:
                    classNames.remove('active')

                if isTriggered(range_element.input.n_clicks):
                    classNames.append('active')
                    data['current_page'] = range_elements[index].id['idx']

                range_out.append(' '.join(classNames))

            return data, range_out

        super().__init__(range_elements, id=pid('TableAIOPaginator'), className=className)
