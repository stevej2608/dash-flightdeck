from dash import html
from dash_svg import Svg, Path

def acquisition():
    return html.Div([
        html.Div([
            html.Div([
                html.H2("Acquisition", className='fs-5 fw-bold mb-1'),
                html.P("Tells you where your visitors originated from, such as search engines, social networks or website referrals."),
                html.Div([
                    html.Div([
                        html.Div([
                            Svg([
                                Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z', clipRule='evenodd')
                            ], fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='icon-shape icon-sm icon-shape-danger rounded me-3'),
                        html.Div([
                            html.Label("Bounce Rate", className='mb-0'),
                            html.H4("33.50%", className='mb-0')
                        ], className='d-block')
                    ], className='d-flex align-items-center me-5'),
                    html.Div([
                        html.Div([
                            Svg([
                                Path(d='M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z')
                            ], fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='icon-shape icon-sm icon-shape-purple rounded me-3'),
                        html.Div([
                            html.Label("Sessions", className='mb-0'),
                            html.H4("9,567", className='mb-0')
                        ], className='d-block')
                    ], className='d-flex align-items-center pt-3')
                ], className='d-block')
            ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 px-0')

