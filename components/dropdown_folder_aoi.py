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

class DropdownFolderAIO(html.Div):

    class ids:
        button = lambda aio_id: {
            'component': 'DropdownAIO',
            'subcomponent': 'button',
            'aio_id': aio_id
        }
        content = lambda aio_id: {
            'component': 'DropdownAIO',
            'subcomponent': 'content',
            'aio_id': aio_id
        }

    ids = ids

    def __init__(self, children, text, icon, aio_id=None):
        """Sidebar dropdown component with icon, text and arrow; that when clicked displays the child elements

        Args:
            children (list): The child elements
            text (str): The drop down text
            icon (Svg): The dropdown icon
            aio_id (str, optional): The component ID. Defaults to None.
        """

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        button = html.Span([
            html.Span([
                html.Span(icon, className='sidebar-icon'),
                html.Span(text, className='sidebar-text')
            ]),
            html.Span(ARROW_ICON, className='link-arrow')
        ], id=self.ids.button(aio_id), className='nav-link collapsed d-flex justify-content-between align-items-center')

        # Drop down container

        container = html.Div([
            html.Ul(children, className='flex-column nav')
        ], id=self.ids.content(aio_id),className='multi-level collapse', role='list')

        super().__init__([
            html.Li([
                button,
                container
            ], className='nav-item')
        ])

    @callback(Output(ids.content(MATCH), 'className'),Input(ids.button(MATCH), 'n_clicks'), State(ids.content(MATCH), 'className'))
    def update_dropdown(n_clicks, className):
        logging.info('hidden = %s', className)

        if not n_clicks:
            return className

        if 'collapse' in className:
            return className.replace(' collapse', '')
        else:
            return className + ' collapse'
