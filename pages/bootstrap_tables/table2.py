from collections import OrderedDict
import pandas as pd
from dash import html
from dash_svg import Svg, Path
from components.table import TableAIO

data = OrderedDict([

    ('Country',['United States', 'Canada', 'United Kingdom', 'France', 'Japan', 'Germany']),
    ('All',['106', '76', '147', '112', '115', '220']),
    ('All Change',['5', '17', '10', '3', '12', '56']),
    ('Travel & Local',['3', '4', '5', '5', '6', '7']),
    ('Travel & Local Change',['=', '=', '=', '1', '1', '3']),
    ('Widgets',['32', '30', '34', '34', '37', '30']),
    ('Widgets Change',['3', '3', '7', '2', '5', '2']),
    ])

FLAGS = {
    "United States": '../../assets/img/flags/united-states-of-america.svg',
    "Canada": '../../assets/img/flags/canada.svg',
    "United Kingdom": '../../assets/img/flags/united-kingdom.svg',
    "France": '../../assets/img/flags/france.svg',
    "Japan": '../../assets/img/flags/japan.svg',
    "Germany": '../../assets/img/flags/germany.svg',
}

UP_ICON = Svg([
        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

DOWN_ICON = Svg([
        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


df = pd.DataFrame.from_dict(data)

def numberAndArrow(value):

    def normalise(v):
        if v == '=': return None, v, None
        if v[0] =='-': return DOWN_ICON, v[1:], 'text-danger'
        return UP_ICON, v, 'text-success'

    icon, text, text_colour = normalise(value)

    return html.Td([
        html.Div([
            icon,
            html.Span(text, className='fw-bold')
        ], className='d-flex align-items-center')
    ], className=text_colour)


class TravelTable(TableAIO):

    TABLE_CLASS_NAME = 'table table-centered table-nowrap mb-0 rounded'

    def tableHead(self, columns):

        names = [col['name'] for col in columns]

        beg = html.Th(names[0], className='border-0 rounded-start')
        mid = [html.Th(name, className='border-gray-200') for name in names[1:-1]]
        end = html.Th(names[-1], className='border-0 rounded-end')

        row = html.Tr([beg] + mid +[end])

        return html.Thead(row, className='thead-light')

    def tableRow(self, args):

        country, all, change, tal, talCh, widgets, widgetsCh = args.values()

        return  html.Tr([
            html.Td([
                html.A([
                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src=FLAGS[country]),
                    html.Div([
                        html.Span(country, className='h6')
                    ])
                ], href='#', className='d-flex align-items-center')
            ], className='border-0'),
            html.Td(all, className='border-0 fw-bold'),
            numberAndArrow(change),
            html.Td(tal, className='border-0 fw-bold'),
            numberAndArrow(talCh),
            html.Td(widgets, className='border-0'),
            numberAndArrow(widgetsCh),

        ])


def table2():

    table = TravelTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns])

    return html.Div([
        html.Div([
            html.Div(table, className='table-responsive')
        ], className='card-body')
    ], className='card border-0 shadow')
