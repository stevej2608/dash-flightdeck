from dash import html, dcc
from dash_svg import Svg, Path

def table():
    return html.Div([
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th("#", className='border-gray-200'),
                    html.Th("Bill For", className='border-gray-200'),
                    html.Th("Issue Date", className='border-gray-200'),
                    html.Th("Due Date", className='border-gray-200'),
                    html.Th("Total", className='border-gray-200'),
                    html.Th("Status", className='border-gray-200'),
                    html.Th("Action", className='border-gray-200')
                ])
            ]),
            html.Tbody([
                # Item
                html.Tr([
                    html.Td([
                        html.A("456478", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 May 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Jun 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Due", className='fw-bold text-warning')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456423", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Apr 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 May 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456420", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Mar 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Apr 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456421", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Feb 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Mar 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456420", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Jan 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Feb 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456479", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Dec 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Jan 2020", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                # Item
                html.Tr([
                    html.Td([
                        html.A("456478", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Platinum Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Nov 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Dec 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$799,00", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("453673", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Gold Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Oct 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Nov 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$533,42", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Cancelled", className='fw-bold text-danger')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456468", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Gold Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Sep 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Oct 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$533,42", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ]),
                # Item
                html.Tr([
                    html.Td([
                        html.A("456478", href='#', className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Flexible Subscription Plan", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Aug 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("1 Sep 2019", className='fw-normal')
                    ]),
                    html.Td([
                        html.Span("$233,42", className='fw-bold')
                    ]),
                    html.Td([
                        html.Span("Paid", className='fw-bold text-success')
                    ]),
                    html.Td([
                        html.Div([
                            html.Button([
                                html.Span([
                                    html.Span(className='fas fa-ellipsis-h icon-dark')
                                ], className='icon icon-sm'),
                                html.Span("Toggle Dropdown", className='visually-hidden')
                            ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-0', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    html.Span(className='fas fa-eye me-2'),
                                    "View Details"
                                ], className='dropdown-item rounded-top', href='#'),
                                html.A([
                                    html.Span(className='fas fa-edit me-2'),
                                    "Edit"
                                ], className='dropdown-item', href='#'),
                                html.A([
                                    html.Span(className='fas fa-trash-alt me-2'),
                                    "Remove"
                                ], className='dropdown-item text-danger rounded-bottom', href='#')
                            ], className='dropdown-menu py-0')
                        ], className='btn-group')
                    ])
                ])
            ])
        ], className='table table-hover'),
        html.Div([
            html.Nav([
                html.Ul([
                    html.Li([
                        html.A("Previous", className='page-link', href='#')
                    ], className='page-item'),
                    html.Li([
                        html.A("1", className='page-link', href='#')
                    ], className='page-item'),
                    html.Li([
                        html.A("2", className='page-link', href='#')
                    ], className='page-item active'),
                    html.Li([
                        html.A("3", className='page-link', href='#')
                    ], className='page-item'),
                    html.Li([
                        html.A("4", className='page-link', href='#')
                    ], className='page-item'),
                    html.Li([
                        html.A("5", className='page-link', href='#')
                    ], className='page-item'),
                    html.Li([
                        html.A("Next", className='page-link', href='#')
                    ], className='page-item')
                ], className='pagination mb-0')
            ], **{"aria-label": "Page navigation example"}),
            html.Div([
                "Showing ",
                html.B("5"),
                " out of ",
                html.B("25"),
                " entries"
            ], className='fw-normal small mt-4 mt-lg-0')
        ], className='card-footer px-3 border-0 d-flex flex-column flex-lg-row align-items-center justify-content-between')
    ], className='card card-body border-0 shadow table-wrapper table-responsive')

