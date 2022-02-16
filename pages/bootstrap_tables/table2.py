import pandas as pd
from dash import html, dcc
from dash_svg import Svg, Path

TABLE_COLS = ["Country", "All", "All Change", "Travel & Local", "Travel & Local Change", "Widgets", "Widgets Change"]

TABLE_DATA = [
    "United States,  106, 5, 	3,	=, 32, 3",
    "Canada,         76,  17,   4,  =, 30, 3",
    "United Kingdom, 147, 10,	5,	=, 34, 7",
    "France,	     112, 3, 	5,  1, 34, 2",
    "Japan,	         115, 12,	6,  1, 37, 5",
    "Germany,	     220, 56,	7,  3, 30, 2"
]

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


def data2Dict():

    # Convert TABLE_DATA CSV into dict of dicts. The returned primary dict has
    # an entry for each column who's values are the row values for the column
    # indexed on row number

    data = {}
    for col in TABLE_COLS: data[col] = {}

    for irow, row in enumerate(TABLE_DATA):
        for icol, value in enumerate(row.split(',')):
            colName = TABLE_COLS[icol]
            data[colName][irow] = value.strip()
    return data

df = pd.DataFrame.from_dict(data2Dict())

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

def _tableHead():
    return html.Thead([
        html.Tr([
            html.Th(df.columns[0], className='border-0 rounded-start'),
            html.Th(df.columns[1], className='border-0'),
            html.Th(df.columns[2], className='border-0'),
            html.Th(df.columns[3], className='border-0'),
            html.Th(df.columns[4], className='border-0'),
            html.Th(df.columns[5], className='border-0'),
            html.Th(df.columns[6], className='border-0 rounded-end')
        ])
    ], className='thead-light')


def _tableRow(country, all, change, tal, talCh, widgets, widgetsCh):
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
        html.Td("32", className='border-0 fw-bold'),
        numberAndArrow(widgetsCh),

    ])


def _tableBody():
    rows = df.values.tolist()
    return html.Tbody([
        _tableRow(*args) for args in rows
    ])


def table2():
    thead = _tableHead()
    tbody = _tableBody()
    return html.Div([
        html.Div([
            html.Div([
                html.Table([
                    thead,
                    tbody,
                ], className='table table-centered table-nowrap mb-0 rounded')
            ], className='table-responsive')
        ], className='card-body')
    ], className='card border-0 shadow')
