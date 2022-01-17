from dash import html
from dash_svg import Svg, Path

def totalOrders():
    return html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div("Total orders", className='h6 fw-normal text-gray mb-2'),
                    html.H2("452", className='h3 fw-extrabold'),
                    html.Div([
                        html.Span(className='fas fa-angle-up text-success'),
                        html.Span("18.2%", className='text-success fw-bold')
                    ], className='small mt-2')
                ], className='d-block'),
                html.Div([
                    html.Div([
                        html.Span(className='dot rounded-circle bg-gray-800 me-2'),
                        html.Span("July", className='fw-normal small')
                    ], className='d-flex align-items-center text-end mb-2'),
                    html.Div([
                        html.Span(className='dot rounded-circle bg-secondary me-2'),
                        html.Span("August", className='fw-normal small')
                    ], className='d-flex align-items-center text-end')
                ], className='d-block ms-auto')
            ], className='card-header d-flex flex-row align-items-center flex-0 border-bottom'),
            html.Div([
                html.Div(className='ct-chart-ranking ct-golden-section ct-series-a')
            ], className='card-body p-2')
        ], className='card border-0 shadow')
    ], className='col-12 px-0 mb-4')


