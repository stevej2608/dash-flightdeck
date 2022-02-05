import logging
import uuid
from dash import Output, Input, State, html, dcc, callback, MATCH
import dash_holoniq_components as dhc
from icons.hero import DOWN_ARROW_ICON, PLUS_ICON, PRODUCTS_ICON, CUSTOMERS_ICON, CLIPBOARD_ICON
from app import create_app
from server import serve_app


def dropdownLink(title, icon, href='#'):
    return dcc.Link([
        icon,
        title
    ], className='dropdown-item d-flex align-items-center', href=href)

class DropdownButtonNewAIO(html.Div):

    class ids:
        button = lambda aio_id: {
            'component': 'DropdownButtonNewAIO',
            'subcomponent': 'button',
            'aio_id': aio_id
        }
        container = lambda aio_id: {
            'component': 'DropdownButtonNewAIO',
            'subcomponent': 'container',
            'aio_id': aio_id
        }

    ids = ids

    def __init__(self, dropdownEntries, buttonText, buttonIcon=PLUS_ICON, buttonColor='secondary', downArrow=False):

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



layout = html.H2([
    DropdownButtonNewAIO([
        dropdownLink("Products", PRODUCTS_ICON,href='#'),
        dropdownLink("Customers", CUSTOMERS_ICON, href='#'),
    ], "Reports", buttonIcon=CLIPBOARD_ICON, buttonColor="gray-800", downArrow=True)
])


if __name__ == "__main__":

    logging.basicConfig(
        level= "INFO",
        # format='%(levelname)s %(asctime)s.%(msecs)03d %(module)10s/%(lineno)-5d %(message)s'
        format='%(levelname)s %(module)10s/%(lineno)-5d %(message)s'
    )

    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    app = create_app(layout)

    serve_app(app, debug=False)
