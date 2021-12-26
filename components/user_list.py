from dash import Output, Input, State, html, callback, MATCH
import uuid

def userListItem(text, icon):
    return html.Li([
            html.Span([html.I(className=icon)], className="dropdown__icon"),
            html.Span(text, className="dropdown__title")
        ], className="dropdown__list-item" )

class UserListAIO(html.Div):

    class ids:
        title = lambda aio_id: {
            'component': 'UserListAIO',
            'subcomponent': 'title',
            'aio_id': aio_id
        }
        list = lambda aio_id: {
            'component': 'UserListAIO',
            'subcomponent': 'list',
            'aio_id': aio_id
        }

    class listVis:
        visible = "dropdown dropdown--active"
        hidden = "dropdown"

    def __init__(self, children, url, aio_id=None):
        """UserListAIO - Manage the on-click User list dropdown
        """

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        super().__init__([
                html.Div([
                    html.Ul(children, className="dropdown__list")
                ], id=self.ids.list(aio_id), className=UserListAIO.listVis.hidden)
            ] ,id=self.ids.title(aio_id), style={"background-image" : f"url({url})"}, className="header__avatar" )



    @callback(Output(ids.list(MATCH), 'className'),
              Input(ids.title(MATCH), 'n_clicks'),
              State(ids.list(MATCH), 'className')
              )
    def update_children(clicks, currentClassName):
        className=UserListAIO.listVis.hidden
        if clicks and currentClassName == className:
            className = UserListAIO.listVis.visible
        return className
