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
        """Button with supplied icon and down arrow. When clicked a drop-down
        selection of entries is revealed.

        Args:
            dropdownEntries (list): The dropdon entries
            buttonText (str): The button text
            buttonIcon (Svg, optional): Optional button icon. Defaults to PLUS_ICON.
            buttonColor (str, optional): BS5 button colour. Defaults to 'secondary'.
            downArrow (bool, optional): Show down arrow. Defaults to False.

        Example:

            DropdownButtonAIO([
                dropdownLink("Add User", USER_ADD_ICON),

                dropdownLink("Add Widget", WIDGET_ICON),

                dropdownLink("Upload Files", UPLOAD_ICON),

                dropdownLink("Preview Security", SECURITY_ICON),

                dropdownLink("Upgrade to Pro", FIRE_ICON_DANGER),

            ], "New Task", buttonColor="gray-800")

        """


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
