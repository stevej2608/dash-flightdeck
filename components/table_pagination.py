import logging
from dash import html, callback, ALL, callback_context
from dash_spa import match, prefix, isTriggered, NOUPDATE

class TableAIOPagination(html.Div):


    def __init__(self, range, current, max, aio_id=None):

        pid = prefix()

        logging.info('TableAIOPagination pid=%s', pid(''))

        range_match = match({'type': pid('li'), 'idx': ALL})

        def range_element(text):
            rng = self.range_element(text)
            rng.id = range_match.idx(text)
            return rng

        range_elements = [range_element(text) for text in range]

        showing = self.showing_container()
        showing.children = self.showing_content(current, max)
        showing.id = pid('showing')

        @callback(showing.output.children, range_match.input.n_clicks)
        def update_pagination(current):
            ctx = callback_context
            for index, element in enumerate(range_elements):
                if isTriggered(element.input.n_clicks):
                    current = ctx.inputs_list[0][index]['id']['idx']
                    return self.showing_content(current, max)
            return NOUPDATE

        div = html.Div([
            html.Nav(html.Ul(range_elements , className='pagination mb-0')),
            showing
        ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')

        super().__init__(div)

    def range_element(self, text):
        return html.Li([html.Span(text, className='page-link')], className='page-item')

    def showing_container(self):
        return html.Div(className='fw-normal small mt-4 mt-lg-0')

    def showing_content(self, current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]
