from dash import html, callback, ALL, callback_context
from dash_spa import match, prefix, isTriggered, NOUPDATE

# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback

class TableAIOPagination(html.Div):


    def __init__(self, range, current, max, aio_id=None):

        pid = prefix()

        range_match = match({'type': pid('li'), 'idx': ALL})

        def range_element(text):
            rng = self.range_element(text)
            rng.id = range_match.idx(text)
            return rng

        range_elements = [range_element(text) for text in range]

        showing = self.showing_container()
        showing.children = self.showing_content(current, max)
        showing.id = pid('showing')


        @callback(showing.output.children,
                  range_match.output.className,
                  range_match.input.n_clicks,
                  range_match.state.className)
        def update_pagination2(clicks, className):
            ctx = callback_context
            range_out = []
            showing = NOUPDATE
            for index, range_element in enumerate(range_elements):
                classNames = className[index].split()

                if 'active' in classNames:
                    classNames.remove('active')

                if isTriggered(range_element.input.n_clicks):
                    classNames.append('active')
                    current = ctx.inputs_list[0][index]['id']['idx']
                    showing = self.showing_content(current, max)

                range_out.append(' '.join(classNames))

            return showing, range_out


        div = html.Div([
            html.Nav(html.Ul(range_elements , className='pagination mb-0')),
            showing
        ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')

        super().__init__(div)

    def range_element(self, value):
        active = "active" if isinstance(value, int) and value == 3 else ""
        return html.Li([html.Span(value, className='page-link')], className=f'page-item {active}')

    def showing_container(self):
        return html.Div(className='fw-normal small mt-4 mt-lg-0')

    def showing_content(self, current, max):
        return ["Showing ",html.B(current)," out of ",html.B(max)," entries"]
