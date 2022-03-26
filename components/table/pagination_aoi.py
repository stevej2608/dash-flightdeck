from math import ceil
from dash import html, callback, ALL
from dash.exceptions import PreventUpdate
from dash_spa import match, prefix, isTriggered
from components.store_aio import StoreAIO



# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback


class TableAIOPaginator(html.Ul):
    """Ellipses pagination logic

    Args:
        page (int, optional): The active page. Defaults to 1.
        adjacents (int, optional): How many adjacent pages should be shown on each side. Defaults to 2.
        page_size (int, optional): How many items to show per page. Defaults to 5.
        total_items (int): Total number of items to be grouped into pages

    Example:

    ```

            « previous [1] 2 3 4 5 6 7 ... 19 20 NEXT »
            « PREVIOUS 1 [2] 3 4 5 6 7 ... 19 20 NEXT »
            « PREVIOUS 1 2 [3] 4 5 6 7 ... 19 20 NEXT »
            « PREVIOUS 1 2 3 [4] 5 6 7 ... 19 20 NEXT »
            « PREVIOUS 1 2 ... 3 4 [5] 6 7 ... 19 20 NEXT »

            « PREVIOUS 1 2 ... 13 14 [15] 16 17 ... 19 20 NEXT »
            « PREVIOUS 1 2 ... 14 15 [16] 17 18 19 20 NEXT »

            « PREVIOUS 1 2 ... 14 15 16 17 18 [19] 20 NEXT »
            « PREVIOUS 1 2 ... 14 15 16 17 18 19 [20] next »

    ```
    """

    PREVIOUS = 'Previous'
    NEXT = 'Next'

    @property
    def state(self):
        return self.store.state.data

    @property
    def value(self):
        return self.store.input.data

    def __init__(self, page = 1, adjacents = 2, page_size = 5, total_items=None, className: str = None, aio_id=None):
        pid = prefix(aio_id)
        self.range_match = match({'type': pid('li'), 'idx': ALL})
        self.lastpage = ceil(total_items / page_size)
        self.store = StoreAIO.create_store({'page': page, 'max': self.lastpage}, id=pid('store'))

        pagination = self.select(page, adjacents)

        super().__init__(pagination, id=pid('TableAIOPaginator'), className=className)


        @callback(self.store.output.data,
                  self.output.children,
                  self.range_match.input.n_clicks,
                  self.range_match.state.id,
                  self.store.state.data)
        def update_cb(clicks, id, data):

            if not any(clicks):
                raise PreventUpdate

            # Set the selected element to active and update
            # store.data['current_page'] with the selected value

            page = data['page']

            selection = self.range_match.triggerIndex()
            if selection is not None:
                if selection == 'Previous':
                    page -=1
                elif selection == 'Next':
                    page += 1
                else:
                    page = selection

                data['page'] = page
                pagination = self.select(page, adjacents)
                return data, pagination

            raise PreventUpdate


    def select(self, page, adjacents=2):
        lastpage = self.lastpage
        first_pages = self.emit(1) + self.emit(2)
        last_pages = self.emit(lastpage - 1) + self.emit(lastpage)

        pagination = []

        # Previous button

        pagination += self.emit(self.PREVIOUS, disabled = page == 1)

        # Determin Pages

        # Test to see if we have enough pages to bother breaking it up

        if lastpage < 7 + (adjacents * 2):
            for i in range(1, lastpage+1):
                pagination += self.emit(i, i == page)
        elif lastpage > 5 + (adjacents * 2):

            # Test to see if we're close to beginning. If so only hide later pages

            if page < 1 + (adjacents * 2):

                # PREVIOUS 1 [2] 3 4 5 6 7 ... 19 20 NEXT

                for i in range(1, 4 + (adjacents * 2)):
                    pagination += self.emit(i, i == page)

                pagination += self.emit('...', disabled=True)
                pagination += last_pages

            elif lastpage - (adjacents * 2) > page and page > (adjacents * 2):

                # We're in the middle hide some front and some back
                # PREVIOUS 1 2 ... 5 6 [7] 8 9 ... 19 20 NEXT

                pagination += first_pages
                pagination += self.emit('...', disabled=True)

                for i in range(page - adjacents, page + adjacents + 1):
                    pagination += self.emit(i, i == page)

                pagination += self.emit('...', disabled=True)
                pagination += last_pages
            else:

                # Must be close to end only hide early pages
                # PREVIOUS 1 2 ... 14 15 16 17 [18] 19 20 NEXT

                pagination += first_pages
                pagination += self.emit('...', disabled=True)

                for i in range(lastpage - (2 + (adjacents * 2)), lastpage + 1):
                    pagination += self.emit(i, i == page)


        # Append the Next button

        pagination += self.emit(self.NEXT, disabled=(page == lastpage))

        if lastpage <= 1 :
            pagination = []

        return pagination

    def emit(self, page, active=False, disabled=False):
        element = html.Li([html.Span(page, className='page-link')], className='page-item')
        if disabled:
            element.disabled = True
        else:
            element.id = self.range_match.idx(page)
            if active:
                element.className += " active"

        return [element]
