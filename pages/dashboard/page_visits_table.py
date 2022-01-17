
from dash import html
from dash_svg import Svg, Path

def pageVisitsTable():
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
                    html.Thead([
                        html.Tr([
                            html.Th("Page name", className='border-bottom', scope='col'),
                            html.Th("Page Views", className='border-bottom', scope='col'),
                            html.Th("Page Value", className='border-bottom', scope='col'),
                            html.Th("Bounce rate", className='border-bottom', scope='col')
                        ])
                    ], className='thead-light'),
                    html.Tbody([
                        html.Tr([
                            html.Th("/demo/admin/index.html", className='text-gray-900', scope='row'),
                            html.Td("3,225", className='fw-bolder text-gray-500'),
                            html.Td("$20", className='fw-bolder text-gray-500'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z', clipRule='evenodd')
                                    ], className='icon icon-xs text-danger me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "42,55%"
                                ], className='d-flex')
                            ], className='fw-bolder text-gray-500')
                        ]),
                        html.Tr([
                            html.Th("/demo/admin/forms.html", className='text-gray-900', scope='row'),
                            html.Td("2,987", className='fw-bolder text-gray-500'),
                            html.Td("0", className='fw-bolder text-gray-500'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z', clipRule='evenodd')
                                    ], className='icon icon-xs text-success me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "43,24%"
                                ], className='d-flex')
                            ], className='fw-bolder text-gray-500')
                        ]),
                        html.Tr([
                            html.Th("/demo/admin/util.html", className='text-gray-900', scope='row'),
                            html.Td("2,844", className='fw-bolder text-gray-500'),
                            html.Td("294", className='fw-bolder text-gray-500'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z', clipRule='evenodd')
                                    ], className='icon icon-xs text-success me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "32,35%"
                                ], className='d-flex')
                            ], className='fw-bolder text-gray-500')
                        ]),
                        html.Tr([
                            html.Th("/demo/admin/validation.html", className='text-gray-900', scope='row'),
                            html.Td("2,050", className='fw-bolder text-gray-500'),
                            html.Td("$147", className='fw-bolder text-gray-500'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z', clipRule='evenodd')
                                    ], className='icon icon-xs text-danger me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "50,87%"
                                ], className='d-flex')
                            ], className='fw-bolder text-gray-500')
                        ]),
                        html.Tr([
                            html.Th("/demo/admin/modals.html", className='text-gray-900', scope='row'),
                            html.Td("1,483", className='fw-bolder text-gray-500'),
                            html.Td("$19", className='fw-bolder text-gray-500'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z', clipRule='evenodd')
                                    ], className='icon icon-xs text-success me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "26,12%"
                                ], className='d-flex')
                            ], className='fw-bolder text-gray-500')
                        ])
                    ])
                ], className='table align-items-center table-flush')
            ], className='table-responsive')
        ], className='card border-0 shadow')
    ], className='col-12 mb-4')
