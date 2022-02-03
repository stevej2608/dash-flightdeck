import uuid
import logging
from dash import Output, Input, State, html, dcc, callback, MATCH
import dash_holoniq_components as dhc
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
        container = lambda aio_id: {
            'component': 'DropdownButtonAIO',
            'subcomponent': 'container',
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

        _button = dhc.Button([
                buttonIcon,
                buttonText,
                DOWN_ARROW_ICON if downArrow else None
            ], id=self.ids.button(aio_id), className=f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle')

        # Drop down container

        _container = html.Div(
            dropdownEntries,
            id=self.ids.container(aio_id),
            className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')

        super().__init__(html.Div([_button, _container], className='dropdown'))

    @callback(Output(ids.container(MATCH), 'className'),
            Input(ids.button(MATCH), 'n_clicks'),
            Input(ids.button(MATCH), 'focus'),
            State(ids.container(MATCH), 'className'))
    def show_dropdown(button_clicks, button_focus, className):
        logging.info('show_dropdown: button_clicks=%s, className = %s', button_clicks, className)

        if not button_clicks:
            return className

        if 'show' in className and button_focus == False:
            return className.replace(' show', '')
        else:
            return className + ' show'