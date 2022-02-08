import logging
from dash import html, dcc, callback, MATCH
import dash_holoniq_components as dhc
from dash_spa import match, component_uuid
from icons.hero import DOWN_ARROW_ICON, PLUS_ICON

def dropdownLink(title, icon, href='#'):
    return dcc.Link([
        icon,
        title
    ], className='dropdown-item d-flex align-items-center', href=href)

class DropdownButtonAIO(html.Div):

    class ids:
        button = match({'component': 'DropdownButtonAIO', 'subcomponent': 'button', 'idx': MATCH})
        container = match({'component': 'DropdownButtonAIO', 'subcomponent': 'container', 'idx': MATCH})

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

        logging.info('DropdownButtonAIO')

        ids = DropdownButtonAIO.ids
        aio_id = component_uuid()

        button = dhc.Button([
                buttonIcon,
                buttonText,
                DOWN_ARROW_ICON if downArrow else None
            ], id=ids.button.idx(aio_id), className=f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle')

        logging.info('DropdownButtonAIO.button.id=%s', button.id)

        # Drop down container

        container = html.Div(
            dropdownEntries,
            id = ids.container.idx(aio_id),
            className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')

        logging.info('DropdownButtonAIO.container.id=%s', container.id)

        super().__init__(html.Div([button, container], className='dropdown'))


    @callback(ids.container.output.className, ids.button.input.n_clicks, ids.button.input.focus, ids.container.state.className)
    def show_dropdown(button_clicks, button_focus, className):  # pylint: disable=no-self-argument
        # logging.info('show_dropdown: button_clicks=%s, className = %s', button_clicks, className)

        if not button_clicks:
            return className

        if 'show' in className and button_focus is False:
            return className.replace(' show', '')
        else:
            return className + ' show'
