from dash import html, dcc, callback, MATCH
import dash_holoniq_components as dhc
from dash_spa import match, component_uuid


class TableActionAIO(html.Div):

    class ids:
        button = match({'component': 'TableActionAIO', 'subcomponent': 'button', 'idx': MATCH})
        container = match({'component': 'TableActionAIO', 'subcomponent': 'container', 'idx': MATCH})

    # pylint: disable=no-self-argument

    @callback(ids.container.output.className, ids.button.input.n_clicks, ids.button.input.focus, ids.container.state.className)
    def show_dropdown(button_clicks, button_focus, className):

        if not button_clicks:
            return className

        classNames = className.split()

        if 'show' in classNames:
            if button_focus is False:
                classNames.remove('show')
        else:
            classNames.append('show')

        return ' '.join(classNames)


    def __init__(self, children, aio_id=None):
        """Table Action component, shows children in dropdown

        Args:
            children (list): The child elements
            aio_id (str, optional): The component ID. Defaults to None.
        """

        ids = TableActionAIO.ids
        aio_id = aio_id if aio_id else component_uuid()

        button = dhc.Button([
                html.Span([
                    html.Span(className='fas fa-ellipsis-h icon-dark')
                ], className='icon icon-sm'),
                html.Span("Toggle Dropdown", className='visually-hidden')
            ], id=ids.button.idx(aio_id), className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0')

        # Drop down container

        # dropdown bootom-left. Ripped from the Volt transactons table using Firefox debug tools

        style={"position": "absolute",
               "inset": "0px 0px auto auto",
               "margin": "0px",
               "transform": "translate3d(0px, 25.3333px, 0px)"
               }

        container = html.Div(
            children,
            id = ids.container.idx(aio_id),
            className='dropdown-menu py-0', style=style)

        super().__init__(html.Div([button, container], className='btn-group'))


