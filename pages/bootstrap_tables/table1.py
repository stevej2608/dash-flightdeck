import pandas as pd
from dash import html
from dash_svg import Svg, Path

EARTH_ICON =  Svg([
        Path(fillRule='evenodd', d='M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z', clipRule='evenodd')
    ], className='icon icon-xxs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

GOOGLE_ICON = Svg([
        Path(fill='currentColor', d='M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z')
    ], className='icon icon-xxs text-gray-500 me-2', role='img', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 488 512', **{"aria-hidden": "true", "data-prefix": "fab", "data-icon": "google"})

YOUTUBE_ICON = Svg([
        Path(fill='currentColor', d='M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z')
    ], className='icon icon-xxs text-gray-500 me-2', role='img', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 576 512', **{"aria-hidden": "true", "data-prefix": "fab", "data-icon": "youtube"})

YAHOO_ICON = Svg([
        Path(fill='currentColor', d='M223.69,141.06,167,284.23,111,141.06H14.93L120.76,390.19,82.19,480h94.17L317.27,141.06Zm105.4,135.79a58.22,58.22,0,1,0,58.22,58.22A58.22,58.22,0,0,0,329.09,276.85ZM394.65,32l-93,223.47H406.44L499.07,32Z')
    ], className='icon icon-xxs text-gray-500 me-2', role='img', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 512 512', **{"aria-hidden": "true", "data-prefix": "fab", "data-icon": "yahoo"})

TWITTER_ICON = Svg([
        Path(fill='currentColor', d='M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z')
    ], className='icon icon-xxs text-gray-500 me-2', role='img', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 512 512', **{"aria-hidden": "true", "data-prefix": "fab", "data-icon": "twitter"})

UP_ICON = Svg([
        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

DOWN_ICON = Svg([
        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

icons = {
    "Direct": EARTH_ICON,
    "Google Search": GOOGLE_ICON,
    "youtube.com": YOUTUBE_ICON,
    "yahoo.com": YAHOO_ICON,
    "twitter.com": TWITTER_ICON
}


TABLE_COLS = ["#", "Traffic Source", "Source Type", "Category", " Global Rank", "Traffic Share", "Change"]

TABLE_DATA = [
    "1,  Direct,        Direct,  	   -,	                   --,  51%, 2.45%",
    "2,  Google Search, Search/Organic, -,	                   --,  18%, 17.78%",
    "3,  youtube.com,   Social,	        Arts and Entertainment, #2,  18%, -",
    "4,  yahoo.com,	    Referral,	    News and Media,	        #11, 8%,  -9.45%",
    "5,  twitter.com,   Social,         Social Networks,	    #4,  4%,  -"
]



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


def progressBar(value):
    value = value[0:-1]
    return html.Td([
        html.Div([
            html.Div([
                html.Div(value, className='small fw-bold')
            ], className='col-12 col-xl-2 px-0'),
            html.Div([
                html.Div([
                    html.Div(className='progress-bar bg-dark',
                             role='progressbar',
                             style={"width": f"{value}%"}, **{"aria-valuenow": f"{value}", "aria-valuemin": "0", "aria-valuemax": "100"})
                ], className='progress progress-lg mb-0')
            ], className='col-12 col-xl-10 px-0 px-xl-1')
        ], className='row d-flex align-items-center')
    ])


def trafficChange(value):

    def normalise(v):
        if v == '-': return None, v, None
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

def _tableRow(cid, ts, st, cat, rank, share, change):
    return html.Tr([
        html.Td([
            html.A(cid, href='#', className='text-primary fw-bold')
        ]),
        html.Td([
            icons[ts],
            ts
        ], className='fw-bold d-flex align-items-center'),
        html.Td(st),
        html.Td(cat),
        html.Td(rank),
        progressBar(share),
        trafficChange(change)
    ])

def _tableBody():
    rows = df.values.tolist()
    return html.Tbody([
        _tableRow(cid, ts, st, cat, rank, share, change) for cid, ts, st, cat, rank, share, change in rows
    ])

def table1():
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
    ], className='card border-0 shadow mb-4')

