from dash import html, callback, MATCH
from dash.development.base_component import Component
from dash_spa import match, component_uuid

class AIOBase:

    components = {}

    def __init__(self, id=None):
        self.id = id if id else component_uuid()
        AIOBase.components[self.id] = self

    @staticmethod
    def getAIOinstance(id):
        return AIOBase.components[id]



class TableAIO(html.Div, AIOBase):

    class ids:
        table = match({'component': 'TableAIO', 'subcomponent': 'table', 'idx': MATCH})
        table_rows = match({'component': 'TableAIO', 'subcomponent': 'trow', 'idx': MATCH})


    def __init__(self, aio_id=None):
        AIOBase.__init__(self, aio_id)
        super().__init__(html.Div(id=self.id))
