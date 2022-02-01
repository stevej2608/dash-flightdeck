import logging
from dash import html, dcc, register_page
from dash_svg import Svg, Path

from .components import sideBar, mobileNavBar, topNavBar, footer


register_page(__name__, path="/pages/transactions.html", title="Dash/Flightdeck - Transactions")


def layout():
    logging.info('layout()')
    return  html.Div([
        mobileNavBar(),
        sideBar(),

        html.Main([
            topNavBar(),



        # Bread crumbs
        html.Div([
            html.Div([
                # Bread crumb
                html.Nav([
                    html.Ol([
                        html.Li([
                            html.A([
                                Svg([
                                    Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6')
                                ], className='icon icon-xxs', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg')
                            ], href='#')
                        ], className='breadcrumb-item'),
                        html.Li([
                            html.A("Volt", href='#')
                        ], className='breadcrumb-item'),
                        html.Li("Transactions", className='breadcrumb-item active', **{"aria-current": "page"})
                    ], className='breadcrumb breadcrumb-dark breadcrumb-transparent')
                ], className='d-none d-md-inline-block', **{"aria-label": "breadcrumb"}),
                html.H2("All Orders", className='h4'),
                html.P("Your web analytics dashboard template.", className='mb-0')
            ], className='d-block mb-4 mb-md-0'),
            # New plan, share, export buttons
            html.Div([
                html.A([
                    Svg([
                        Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M12 6v6m0 0v6m0-6h6m-6 0H6')
                    ], className='icon icon-xs me-2', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                    "New Plan"
                ], href='#', className='btn btn-sm btn-gray-800 d-inline-flex align-items-center'),
                html.Div([
                    html.Button("Share", type='button', className='btn btn-sm btn-outline-gray-600'),
                    html.Button("Export", type='button', className='btn btn-sm btn-outline-gray-600')
                ], className='btn-group ms-2 ms-lg-3')
            ], className='btn-toolbar mb-2 mb-md-0')
        ], className='d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center py-4'),
        # Table Header
        html.Div([
            html.Div([
                # Search orders
                html.Div([
                    html.Div([
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clipRule='evenodd')
                            ], className='icon icon-xs', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 20 20', fill='currentColor', **{"aria-hidden": "true"})
                        ], className='input-group-text'),
                        dcc.Input(type='text', className='form-control', placeholder='Search orders')
                    ], className='input-group me-2 me-lg-3 fmxw-400')
                ], className='col col-md-6 col-lg-3 col-xl-4'),
                # Table Settings
                html.Div([
                    html.Div([
                        html.Button([
                            Svg([
                                Path(fillRule='evenodd', d='M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', clipRule='evenodd')
                            ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            html.Span("Toggle Dropdown", className='visually-hidden')
                        ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-1', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                        html.Div([
                            html.Span("Show", className='small ps-3 fw-bold text-dark'),
                            html.A([
                                "10",
                                Svg([
                                    Path(fillRule='evenodd', d='M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z', clipRule='evenodd')
                                ], className='icon icon-xxs ms-auto', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='dropdown-item d-flex align-items-center fw-bold', href='#'),
                            html.A("20", className='dropdown-item fw-bold', href='#'),
                            html.A("30", className='dropdown-item fw-bold rounded-bottom', href='#')
                        ], className='dropdown-menu dropdown-menu-xs dropdown-menu-end pb-0')
                    ], className='dropdown')
                ], className='col-4 col-md-2 col-xl-1 ps-md-0 text-end')
            ], className='row align-items-center justify-content-between')
        ], className='table-settings mb-4'),
        # Table
        html.Div([
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
        ], className='card card-body border-0 shadow table-wrapper table-responsive'),








            footer()
        ], className='content')
    ])
