import logging
from dash import html, dcc, MATCH, callback, Output
import dash_holoniq_components as dhc
from icons.hero import DOWN_ARROW_ICON, PLUS_ICON, PRODUCTS_ICON, CUSTOMERS_ICON, CLIPBOARD_ICON
from app import create_app
from server import serve_app

from dash_spa import AIOPrefix, AIOBase

def test():

    aio_id = 1234

    container = lambda aio_id: {
        'component': 'DropdownButtonAIO',
        'subcomponent': 'container',
        'aio_id': aio_id
    }

    op1 = Output(container(MATCH), 'className')


    io = AIOPrefix('DropdownButtonNewAIO')
    id=io.id('container')
    container_spa = html.Div(id=id)
    op_spa = container_spa.output.className
    op1 = op_spa(MATCH)

    return op1, op_spa


ttt = test()

def dropdownLink(title, icon, href='#'):
    return dcc.Link([
        icon,
        title
    ], className='dropdown-item d-flex align-items-center', href=href)


class DropdownButtonNewAIO(AIOBase):

    def __init__(self, dropdownEntries,
                buttonText, buttonIcon=PLUS_ICON,
                buttonColor='secondary', downArrow=False):

        io = AIOPrefix('DropdownButtonNewAIO')

        button = dhc.Button([
                buttonIcon,
                buttonText,
                DOWN_ARROW_ICON if downArrow else None
            ], io.id('btn'), className=f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle')

        # Drop down container

        container = html.Div(
            dropdownEntries,
            id=io.id('container'),
            className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')

        super().__init__(html.Div([button, container], className='dropdown'))

        @callback(container.output.className(MATCH),
                  button.input.n_clicks(MATCH),
                  button.input.focus(MATCH),
                  container.state.className(MATCH))
        def _show_dropdown(button_clicks, button_focus, className):
            logging.info('show_dropdown: button_clicks=%s, className = %s', button_clicks, className)

            if not button_clicks:
                return className

            if 'show' in className and button_focus is False:
                return className.replace(' show', '')
            else:
                return className + ' show'



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
