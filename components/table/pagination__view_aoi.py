from dash import html, callback
from dash.exceptions import PreventUpdate
from dash_spa import prefix

from .table_aio import Dict2Obj
from .pagination_aoi import TableAIOPaginator

class TableAIOPaginatorView(html.Div):

    def __init__(self, paginator: TableAIOPaginator, className= None):
        """Manages and updates the view component of the associated
        TableAIOPaginator. The TableAIOPaginatorView callback is triggered when the
        store component value changes. The callback calls the supplied
        'content' function. The function return value is rendered as the child
        element of the TableAIOPaginatorView

        Args:
            paginator (TableAIOPaginator): The associated paginator
            className (str): the className of the component

        Returns:
            html.Div: The view component

        Example:
        ```

            paginator = TableAIOPaginator(["Previous", 1, 2, 3, 4, 5, "Next"], 5, 25)
            viewer = TableAIOPaginatorView(paginator, render_content, className='fw-normal small mt-4 mt-lg-0' )
        ```

        Markup:
        ```
            <div class="fw-normal small mt-4 mt-lg-0">
                Showing <b>4</b> out of <b>25</b> entries
            </div>
        ```


        """
        pid = prefix(paginator.id)
        s = Dict2Obj(paginator.store.data)

        super().__init__(self.render_content(s.current_page, s.max), id=pid('TableAIOPaginatorView'), className=className)

        @callback(self.output.children, paginator.value)
        def update_view(data):

            if data is not None:
                s = Dict2Obj(data)
                return self.render_content(s.current_page, s.max)

            raise PreventUpdate

    def render_content(self, current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]
