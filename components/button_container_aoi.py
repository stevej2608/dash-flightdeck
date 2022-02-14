from typing import Callable, List
from dash import html, dcc, callback, ALL, callback_context
from dash.exceptions import PreventUpdate
from dash_spa import match, prefix, isTriggered

class ButtonContainerAIO(html.Div):

    @staticmethod
    def createStore(range: List, current:str, aio_id=None) -> dcc.Store:

        pid = prefix(aio_id)
        store_date = {'range': range, 'current': current}
        return dcc.Store(id=pid(), data=store_date)


    def __init__(self, store: dcc.Store, range_element: Callable, className: str = None):
        pass