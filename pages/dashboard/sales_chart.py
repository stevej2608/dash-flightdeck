from dash import html

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
                html.Div(className='ct-chart-sales-value ct-double-octave ct-series-g')
            ], className='card-body p-2')
        ], className='card bg-yellow-100 border-0 shadow')
    ], className='col-12 mb-4')