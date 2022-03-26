from dash import html, dcc
from dash_spa import prefix

class StoreAIO:

    container = html.Div([], id='_aio_storage')

    @staticmethod
    def create_store(data: dict={}, id=None):
        pid = prefix(id)
        store = dcc.Store(id=pid(), data=data)
        StoreAIO.container.children.append(store)
        return store
