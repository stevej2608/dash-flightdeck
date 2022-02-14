from holoniq.utils import log
from dash import html, dcc, callback, ALL, callback_context
from dash_spa import match, prefix, isTriggered
from dash.exceptions import PreventUpdate

# https://dash.plotly.com/all-in-one-components#example-2:-datatableaio---sharing-data-between-__init__-and-callback


class Dict2Obj:
    def __init__(self, d=dict) -> object:
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


class TableAIOPagination(html.Ul):

    @staticmethod
    def createStore(range, current, max, aio_id=None):
        pid = prefix(aio_id)
        store_date = {'range': range, 'current': current, 'max': max}
        return dcc.Store(id=pid(), data=store_date)


    def __init__(self, store: dcc.Store, className=None, aio_id=None):

        pid = prefix(aio_id)

        log.info('TableAIOPagination id=%s', pid())

        range_match = match({'type': pid('li'), 'idx': ALL})

        def range_element(text):
            rng = self.range_element(text)
            rng.id = range_match.idx(text)
            return rng

        s = Dict2Obj(store.data)

        range_elements = [range_element(text) for text in s.range]

        @callback(store.output.data,
                  range_match.output.className,
                  range_match.input.n_clicks,
                  store.state.data,
                  range_match.state.className)
        def update_paginator(clicks, data, className):
            ctx = callback_context
            range_out = []
            for index, range_element in enumerate(range_elements):
                classNames = className[index].split()

                if 'active' in classNames:
                    classNames.remove('active')

                if isTriggered(range_element.input.n_clicks):
                    classNames.append('active')
                    data['current'] = ctx.inputs_list[0][index]['id']['idx']

                range_out.append(' '.join(classNames))

            log.info('TableAIOPagination data=%s', data)

            return data, range_out

        super().__init__(range_elements, id=pid(), className=className)

    def range_element(self, value):
        active = "active" if isinstance(value, int) and value == 3 else ""
        return html.Li([html.Span(value, className='page-link')], className=f'page-item {active}')


class TableAIOPaginatorView(html.Div):

    def __init__(self, store: dcc.Store, className, content, aio_id=None):
        pid = prefix(aio_id)

        log.info('TableAIOPaginatorView id=%s', pid())

        s = Dict2Obj(store.data)

        super().__init__(content(s.current, s.max), id=pid('container'), className=className)

        @callback(self.output.children, store.input.data)
        def update_view(data):

            log.info('TableAIOPaginatorView data=%s', data)

            if data is not None:
                s = Dict2Obj(data)
                return content(s.current, s.max)

            raise PreventUpdate


