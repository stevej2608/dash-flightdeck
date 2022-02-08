import uuid
from dash import html, callback


class AIOPrefix:

    def __init__(self, component_id):
        self.component_id=component_id
        self.aio_id = str(uuid.uuid4())

    def id(self, subcomponent_id):
        return {
            'component': self.component_id,
            'subcomponent': subcomponent_id,
            'aio_id': self.aio_id
        }


class AIOBase(html.Div):

    def __init__(self, children):
        super().__init__(children)

    def callback(self, output, inputs=[], state=[]):
        return callback(output, inputs, state)
