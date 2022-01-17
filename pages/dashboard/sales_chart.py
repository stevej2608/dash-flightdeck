from dash import html
from dash_chartist import DashChartist

data = {
    "labels": ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
    "series": [ [1, 2, 4, 8, 6, -2, -1, -4, -6, -2] ]
}

options = {
    "high": 10,
    "low": -10,
}

chartType = 'Bar'


def salesChart():
    return  html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div("Sales Value", className='fs-5 fw-normal mb-2'),
                    html.H2("$10,567", className='fs-3 fw-extrabold'),
                    html.Div([
                        html.Span("Yesterday", className='fw-normal me-2'),
                        html.Span(className='fas fa-angle-up text-success'),
                        html.Span("10.57%", className='text-success fw-bold')
                    ], className='small mt-2')
                ], className='d-block mb-3 mb-sm-0'),
                html.Div([
                    html.A("Month", href='#', className='btn btn-secondary text-dark btn-sm me-2'),
                    html.A("Week", href='#', className='btn btn-sm me-3')
                ], className='d-flex ms-auto')
            ], className='card-header d-sm-flex flex-row align-items-center flex-0'),
            html.Div([
                DashChartist(className='ct-chart-sales-value ct-double-octave', type=chartType, options=options, data=data)
            ], className='card-body p-2')
        ], className='card bg-yellow-100 border-0 shadow')
    ], className='col-12 mb-4')
