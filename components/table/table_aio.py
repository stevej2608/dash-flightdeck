from dash import html, callback, MATCH
from dash.development.base_component import Component
from dash_spa import match, component_id

class Dict2Obj:
    def __init__(self, d=dict) -> object:
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)

class TableAIO(html.Div):

    class ids:
        table = match({'component': 'TableAIO', 'subcomponent': 'table', 'idx': MATCH})
        table_rows = match({'component': 'TableAIO', 'subcomponent': 'trow', 'idx': MATCH})


    def __init__(self, aio_id=None):
        super().__init__(html.Div(id=self.id))
