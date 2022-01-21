
from dash import html
from dash_svg import Svg, Path
import pandas as pd

data = {
    "Page name":     { 0: "/demo/admin/index.html", 1: "/demo/admin/forms.html", 2: "/demo/admin/util.html", 3: "/demo/admin/validation.html", 4: "/demo/admin/modals.html"},
    "Page Views":    { 0: "3,225",                  1: "2,987",                  2: "2,844",                 3: "2,050",                       4: "1,483"},
    "Page Value":    { 0: "$20",                    1: "0",                      2: "294",                   3: "$147",                        4: "$19"},
    "Bounce rate":   { 0: "42,55%",                 1: "43,24%",                 2: "32,35%",                3: "50,87%",                      4: "26,12%"},
    "Bounce change": { 0: "Up",                     1: "Down",                   2: "Down",                  3: "Up",                          4: "Down"}
}

df = pd.DataFrame.from_dict(data)

UP_ICON = Svg([
        Path(fillRule='evenodd', d='M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z', clipRule='evenodd')
    ], className='icon icon-xs text-danger me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

DOWN_ICON = Svg([
        Path(fillRule='evenodd', d='M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z', clipRule='evenodd')
    ], className='icon icon-xs text-success me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def _tableHead():
    return html.Thead([
        html.Tr([
            html.Th(colTitle, className='border-bottom', scope='col') for colTitle in df.columns
        ])
    ], className='thead-light')

def _tableRow(name, views, value, rate, change):
    icon = UP_ICON if change == "Up" else DOWN_ICON
    return  html.Tr([
        html.Th(name, className='text-gray-900', scope='row'),
        html.Td(views, className='fw-bolder text-gray-500'),
        html.Td(value, className='fw-bolder text-gray-500'),
        html.Td([
            html.Div([
                icon,
                rate
            ], className='d-flex')
        ], className='fw-bolder text-gray-500')
    ])

def _tableBody():
    rows = df.values.tolist()
    return html.Tbody([
        _tableRow(name, views, value, rate, change) for name, views, value, rate, change in rows
    ])

def pageVisitsTable():
    thead = _tableHead()
    tbody = _tableBody()
    return html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H2("Page visits", className='fs-5 fw-bold mb-0')
                    ], className='col'),
                    html.Div([
                        html.A("See all", href='#', className='btn btn-sm btn-primary')
                    ], className='col text-end')
                ], className='row align-items-center')
            ], className='card-header'),
            html.Div([
                html.Table([
                    thead,
                    tbody
                ], className='table align-items-center table-flush')
            ], className='table-responsive')
        ], className='card border-0 shadow')
    ], className='col-12 mb-4')
