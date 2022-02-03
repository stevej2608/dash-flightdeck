import uuid
import logging
from dash import Output, Input, State, html, dcc, callback, MATCH

from icons.hero import ARROW_ICON

def dropdownFolderEntry(text, href):
    return html.Li([
        dcc.Link([
            html.Span(text, className='sidebar-text')
        ], className='nav-link', href=href)
    ], className='nav-item')

class TableActionAIO(html.Div):

    class ids:
        button = lambda aio_id: {
            'component': 'TableActionAIO',
            'subcomponent': 'button',
            'aio_id': aio_id
        }
        container = lambda aio_id: {
            'component': 'TableActionAIO',
            'subcomponent': 'container',
            'aio_id': aio_id
        }

    ids = ids

    def __init__(self, children, aio_id=None):
        """Table Action component, shows children in dropdown

        Args:
            children (list): The child elements
            aio_id (str, optional): The component ID. Defaults to None.
        """

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        _button = html.Button([
                html.Span([
                    html.Span(className='fas fa-ellipsis-h icon-dark')
                ], className='icon icon-sm'),
                html.Span("Toggle Dropdown", className='visually-hidden')
            ], id=self.ids.button(aio_id), className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0')

        # Drop down container

        _container = html.Div(children, id=self.ids.container(aio_id), className='dropdown-menu py-0')

        super().__init__([
            html.Div([
                _button,
                _container
            ], className='btn-group')
        ])

    @callback(Output(ids.container(MATCH), 'className'),
            Input(ids.button(MATCH), 'n_clicks'),
            Input(ids.container(MATCH), 'n_clicks'),
            State(ids.container(MATCH), 'className'))
    def show_dropdown(button_clicks, container_clicks, className):
        logging.info('show_dropdown: button_clicks=%s, container_clicks=%s, className = %s', button_clicks, container_clicks, className)

        if not (button_clicks or container_clicks):
            return className

        if 'show' in className:
            return className.replace(' show', '')
        else:
            return className + ' show'


