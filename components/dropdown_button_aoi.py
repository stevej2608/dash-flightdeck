import uuid
import logging
from dash import Output, Input, State, html, dcc, callback, MATCH

from icons.hero import DOWN_ARROW_ICON, PLUS_ICON

def dropdownLink(title, icon, href='#'):
    return dcc.Link([
        icon,
        title
    ], className='dropdown-item d-flex align-items-center', href=href)

class DropdownButtonAIO(html.Div):

    class ids:
        button = lambda aio_id: {
            'component': 'DropdownButtonAIO',
            'subcomponent': 'button',
            'aio_id': aio_id
        }
        content = lambda aio_id: {
            'component': 'DropdownButtonAIO',
            'subcomponent': 'content',
            'aio_id': aio_id
        }

    ids = ids

    def __init__(self, dropdownEntries, buttonText, buttonIcon=PLUS_ICON, buttonColor='secondary', downArrow=False):

        aio_id = str(uuid.uuid4())

        button = html.Button([
                buttonIcon,
                buttonText,
                DOWN_ARROW_ICON if downArrow else None
            ], id=self.ids.button(aio_id), className=f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle')

        # Drop down container

        container = html.Div(
            dropdownEntries,
            id=self.ids.content(aio_id),
            className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')

        super().__init__(html.Div([button, container], className='dropdown'))

    @callback(Output(ids.content(MATCH), 'className'),Input(ids.button(MATCH), 'n_clicks'), State(ids.content(MATCH), 'className'))
    def update_dropdown(n_clicks, className):
        logging.info('hidden = %s', className)

        if not n_clicks:
            return className

        if 'show' in className:
            return className.replace(' show', '')
        else:
            return className + ' show'
