import logging
from dash import html, dcc
from dash_svg import Svg, Path

def table2():
    return html.Div([
        html.Div([
            html.Div([
                html.Table([
                    html.Thead([
                        html.Tr([
                            html.Th("Country", className='border-0 rounded-start'),
                            html.Th("All", className='border-0'),
                            html.Th("All Change", className='border-0'),
                            html.Th("Travel & Local", className='border-0'),
                            html.Th("Travel & Local Change", className='border-0'),
                            html.Th("Widgets", className='border-0'),
                            html.Th("Widgets Change", className='border-0 rounded-end')
                        ])
                    ], className='thead-light'),
                    html.Tbody([
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/united-states-of-america.svg'),
                                    html.Div([
                                        html.Span("United States", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("106", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("5", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger'),
                            html.Td("3", className='border-0 fw-bold'),
                            html.Td("=", className='border-0'),
                            html.Td("32", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("3", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success')
                        ]),
                        # End of Item
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/canada.svg'),
                                    html.Div([
                                        html.Span("Canada", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("76", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("17", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success'),
                            html.Td("4", className='border-0 fw-bold'),
                            html.Td("=", className='border-0'),
                            html.Td("30", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("3", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success')
                        ]),
                        # End of Item
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/united-kingdom.svg'),
                                    html.Div([
                                        html.Span("United Kingdom", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("147", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("10", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success'),
                            html.Td("5", className='border-0 fw-bold'),
                            html.Td("=", className='border-0'),
                            html.Td("34", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("7", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success')
                        ]),
                        # End of Item
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/france.svg'),
                                    html.Div([
                                        html.Span("France", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("112", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("3", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success'),
                            html.Td("5", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("1", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success'),
                            html.Td("34", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("2", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger')
                        ]),
                        # End of Item
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/japan.svg'),
                                    html.Div([
                                        html.Span("Japan", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("115", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("12", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger'),
                            html.Td("6", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("1", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger'),
                            html.Td("37", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("5", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger')
                        ]),
                        # End of Item
                        # Item
                        html.Tr([
                            html.Td([
                                html.A([
                                    html.Img(className='me-2 image image-small rounded-circle', alt='Image placeholder', src='../../assets/img/flags/germany.svg'),
                                    html.Div([
                                        html.Span("Germany", className='h6')
                                    ])
                                ], href='#', className='d-flex align-items-center')
                            ], className='border-0'),
                            html.Td("220", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("56", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger'),
                            html.Td("7", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("3", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-danger'),
                            html.Td("30", className='border-0 fw-bold'),
                            html.Td([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    html.Span("2", className='fw-bold')
                                ], className='d-flex align-items-center')
                            ], className='border-0 text-success')
                        ]),
                        # End of Item
                    ])
                ], className='table table-centered table-nowrap mb-0 rounded')
            ], className='table-responsive')
        ], className='card-body')
    ], className='card border-0 shadow')
