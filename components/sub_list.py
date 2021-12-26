from dash import Output, Input, State, html, callback, MATCH
import uuid

def sub_heading(heading, id=None, icon=None):
    return html.Div(
        [
            html.Span(
                [html.I(className=f"{icon}")],
                className="navList__subheading-icon",
            ),
            html.Span(heading, className="navList__subheading-title"),
        ], id=id, className="navList__subheading row row--align-v-center",
    )


def sub_list_entry(entry):
    return html.Li(entry, className="subList__item")


class SubListAIO(html.Div):

    class ids:
        title = lambda aio_id: {
            'component': 'SubListAIO',
            'subcomponent': 'title',
            'aio_id': aio_id
        }
        container = lambda aio_id: {
            'component': 'SubListAIO',
            'subcomponent': 'container',
            'aio_id': aio_id
        }

    class listVis:
        visible = "subList"
        hidden = "subList  subList--hidden"

    def __init__(self, heading, entries, icon=None, aio_id=None):
        """SubListAIO - Manage the on-click dropdown
        """

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        entries = [sub_list_entry(e) for e in entries]

        super().__init__([
            sub_heading(heading, id=self.ids.title(aio_id), icon=icon),
            html.Ul(entries, id=self.ids.container(aio_id), className=SubListAIO.listVis.hidden)
        ])

    @callback(Output(ids.container(MATCH), 'className'),
              Input(ids.title(MATCH), 'n_clicks'),
              State(ids.container(MATCH), 'className')
              )
    def update_children(clicks, currentClassName):
        className=SubListAIO.listVis.hidden
        if clicks and currentClassName == className:
            className = SubListAIO.listVis.visible
        return className
