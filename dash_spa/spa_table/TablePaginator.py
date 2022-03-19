from dash import html, dcc, callback
from dash.exceptions import PreventUpdate

from dash_spa import prefix, isTriggered, component_uuid
import math

class TablePaginator(html.Div):
    """Classic Table Paginator

            << < 2 / 6 > >>

    see https://dash.plotly.com/datatable/height
    """

    @property
    def state(self):
        return self.store.state.data

    @property
    def value(self):
        return self.store.input.data

    @property
    def page_size(self):
        return self._page_size

    def __init__(self, rows: int, page_size: int, id: str = None):
        pid = prefix(id)

        self._page_size = page_size
        self.pages =  int(math.ceil(rows / page_size))
        self.store = dcc.Store(id=pid('store'), data={'current_page': 1})

        # Create up/down buttons

        firstPage = self.Button("fas fa-angle-double-left","first-page", pid)
        previousPage = self.Button("fas fa-angle-left","previous-page", pid)
        nextPage = self.Button("fas fa-angle-right", "next-page", pid)
        lastPage = self.Button("fas fa-angle-double-right", "last-page", pid)

        # Create page number input with associated shadow and embed them in a container

        style = {'min-width': '4ch'}

        pageInput, pageInputShadow = self.pageInputWithShadow(1, style, id=pid('input'))

        currentPageContainer =  html.Div([
                pageInputShadow,
                pageInput,
            ], className='current-page-container', id=pid('current-page-container'))

        pageNumberLayout = self.pageNumberLayout(currentPageContainer, style)

        # Handle user input

        @callback(self.store.output.data,
                  currentPageContainer.output.children,
                  currentPageContainer.output.key,

                  firstPage.input.n_clicks,
                  previousPage.input.n_clicks,
                  nextPage.input.n_clicks,
                  lastPage.input.n_clicks,

                  pageInput.input.n_submit,
                  pageInput.state.value,

                  self.store.state.data)

        def _paginator_cb(firstPageButton, previousPageButton, nextPageButton, lastPageButton, submit, value, data):
            update = False
            page = data['current_page']

            if isTriggered(firstPage.input.n_clicks):
                page = 1
                update = True
            elif isTriggered(previousPage.input.n_clicks) and page > 1:
                page -= 1
                update = True
            elif isTriggered(nextPage.input.n_clicks) and page < self.pages:
                page += 1
                update = True
            elif isTriggered(lastPage.input.n_clicks):
                page = self.pages
                update = True
            if isTriggered(pageInput.input.n_submit):
                try:
                    input = int(value)
                    if input > 0 and input <= self.pages:
                        page = input
                        update = True
                except Exception:
                    pass

            if not update:
                raise PreventUpdate

            # Update the page value in the store

            data['current_page'] = page

            # Update the input box & shadow with the new value

            children = self.pageInputWithShadow(page, style, id=pid('input'))

            # Change the key value on the current-page-container. This is needed to
            # force the child input box and shadow to be re-rendered and most importantly
            # for the input box to blur (loose focus)

            key = component_uuid()

            return data, children, key


        paginator = [
            self.store,
            firstPage,
            previousPage,
            pageNumberLayout,
            nextPage,
            lastPage
            ]

        super().__init__(paginator, className="previous-next-container")

    def Button(self, icon, className, pid):
        return html.Button(html.I(className=icon), className=className, id=pid(className))

    def pageInputWithShadow(self, page:int, style: dict, id: str):
        pageInput = dcc.Input(className='current-page', placeholder=page, style=style, type='text', value='', id=id)
        pageInputShadow = html.Div(page, className='current-page-shadow', style=style)
        return pageInput, pageInputShadow

    def pageNumberLayout(self, currentPageContainer, style):
        return html.Div([
            currentPageContainer,
            "/",
            html.Div(self.pages, className='last-page', style=style)
        ], className='page-number')
