from dash import html, dcc, register_page
from dash_svg import Svg, Path

# This is a html2dash clone of the full volt dashboard

register_page(__name__, path="/dashboard-volt", title="Dash/Flightdeck - Dashboard")

layout = html.Div([
    # NOTICE: You can use the _analytics.html partial to include production code specific code & trackers
    # Mobile header - brand icon and burger navbar toggle button
    html.Nav([
        html.A([
            html.Img(src='../../assets/img/brand/light.svg', alt='Volt logo')
        ], className='navbar-brand me-lg-5', href='../../index.html'),
        html.Div([
            html.Button([
                html.Span(className='navbar-toggler-icon')
            ], className='navbar-toggler d-lg-none collapsed', type='button', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "false", "aria-label": "Toggle navigation"})
        ], className='d-flex align-items-center')
    ], className='navbar navbar-dark navbar-theme-primary px-4 col-12 d-lg-none'),
    html.Nav([
        html.Div([
            # Mobile Menu Header
            html.Div([
                # Mobile menu header
                html.Div([
                    html.Div([
                        html.Img(src='../../assets/img/team/profile-picture-3.jpg', className='card-img-top rounded-circle border-white', alt='Bonnie Green')
                    ], className='avatar-lg me-4'),
                    html.Div([
                        html.H2("Hi, Jane", className='h5 mb-3'),
                        html.A([
                            Svg([
                                Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1')
                            ], className='icon icon-xxs me-1', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                            "Sign Out"
                        ], href='../../pages/examples/sign-in.html', className='btn btn-secondary btn-sm d-inline-flex align-items-center')
                    ], className='d-block')
                ], className='d-flex align-items-center'),
                html.Div([
                    html.A([
                        Svg([
                            Path(fillRule='evenodd', d='M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z', clipRule='evenodd')
                        ], className='icon icon-xs', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                    ], href='#sidebarMenu', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "true", "aria-label": "Toggle navigation"})
                ], className='collapse-close d-md-none')
            ], className='user-card d-flex d-md-none align-items-center justify-content-between justify-content-md-center pb-4'),
            html.Ul([
                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../../assets/img/brand/light.svg', height='20', width='20', alt='Volt Logo')
                        ], className='sidebar-icon'),
                        html.Span("Volt Overview", className='mt-1 ms-1 sidebar-text')
                    ], href='../../index.html', className='nav-link d-flex align-items-center')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(d='M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z'),
                                Path(d='M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span("Dashboard", className='sidebar-text')
                    ], href='../../pages/dashboard/dashboard.html', className='nav-link')
                ], className='nav-item active'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(d='M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Kanban", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Span("Pro", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ])
                    ], href='https://demo.themesberg.com/volt-pro/pages/kanban.html', target='_blank', className='nav-link d-flex justify-content-between')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(d='M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z'),
                                Path(fillRule='evenodd', d='M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span("Transactions", className='sidebar-text')
                    ], href='../../pages/transactions.html', className='nav-link')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span("Settings", className='sidebar-text')
                    ], href='../../pages/settings-min.html', className='nav-link')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d='M12 1.586l-4 4v12.828l4-4V1.586zM3.707 3.293A1 1 0 002 4v10a1 1 0 00.293.707L6 18.414V5.586L3.707 3.293zM17.707 5.293L14 1.586v12.828l2.293 2.293A1 1 0 0018 16V6a1 1 0 00-.293-.707z', clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Calendar", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Span("Pro", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ])
                    ], href='https://demo.themesberg.com/volt-pro/pages/calendar.html', target='_blank', className='nav-link d-flex justify-content-between')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z', clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Map", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Span("Pro", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ])
                    ], href='https://demo.themesberg.com/volt-pro/pages/map.html', target='_blank', className='nav-link d-flex justify-content-between')
                ], className='nav-item'),
                html.Li([
                    html.Span([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d='M5 4a3 3 0 00-3 3v6a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H5zm-1 9v-1h5v2H5a1 1 0 01-1-1zm7 1h4a1 1 0 001-1v-1h-5v2zm0-4h5V8h-5v2zM9 8H4v2h5V8z', clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Tables", className='sidebar-text')
                        ]),
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', clipRule='evenodd')
                            ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='link-arrow')
                    ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-app"}),
                    html.Div([
                        html.Ul([
                            html.Li([
                                html.A([
                                    html.Span("Bootstrap Tables", className='sidebar-text')
                                ], className='nav-link', href='../../pages/tables/bootstrap-tables.html')
                            ], className='nav-item')
                        ], className='flex-column nav')
                    ], className='multi-level collapse', role='list', id='submenu-app', **{"aria-expanded": "false"})
                ], className='nav-item'),
                html.Li([
                    html.Span([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d='M2 5a2 2 0 012-2h8a2 2 0 012 2v10a2 2 0 002 2H4a2 2 0 01-2-2V5zm3 1h6v4H5V6zm6 6H5v2h6v-2z', clipRule='evenodd'),
                                    Path(d='M15 7h1a2 2 0 012 2v5.5a1.5 1.5 0 01-3 0V7z')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Page examples", className='sidebar-text')
                        ]),
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', clipRule='evenodd')
                            ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='link-arrow')
                    ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-pages"}),
                    html.Div([
                        html.Ul([
                            html.Li([
                                html.A([
                                    html.Span("Sign In", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/sign-in.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Sign Up", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/sign-up.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Forgot password", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/forgot-password.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Reset password", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/reset-password.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Lock", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/lock.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("404 Not Found", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/404.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("500 Not Found", className='sidebar-text')
                                ], className='nav-link', href='../../pages/examples/500.html')
                            ], className='nav-item')
                        ], className='flex-column nav')
                    ], className='multi-level collapse', role='list', id='submenu-pages', **{"aria-expanded": "false"})
                ], className='nav-item'),
                html.Li([
                    html.Span([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(d='M4 3a2 2 0 100 4h12a2 2 0 100-4H4z'),
                                    Path(fillRule='evenodd', d='M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z', clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Components", className='sidebar-text')
                        ]),
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', clipRule='evenodd')
                            ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='link-arrow')
                    ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-components"}),
                    html.Div([
                        html.Ul([
                            html.Li([
                                html.A([
                                    html.Span("All Components", className='sidebar-text')
                                ], className='nav-link', target='_blank', href='https://themesberg.com/docs/volt-bootstrap-5-dashboard/components/accordions/')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Buttons", className='sidebar-text')
                                ], className='nav-link', href='../../pages/components/buttons.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Notifications", className='sidebar-text')
                                ], className='nav-link', href='../../pages/components/notifications.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Forms", className='sidebar-text')
                                ], className='nav-link', href='../../pages/components/forms.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Modals", className='sidebar-text')
                                ], className='nav-link', href='../../pages/components/modals.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Typography", className='sidebar-text')
                                ], className='nav-link', href='../../pages/components/typography.html')
                            ], className='nav-item')
                        ], className='flex-column nav')
                    ], className='multi-level collapse', role='list', id='submenu-components', **{"aria-expanded": "false"})
                ], className='nav-item'),
                html.Li(role='separator', className='dropdown-divider mt-4 mb-3 border-gray-700'),
                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span([
                            "Documentation",
                            html.Span("v1.4", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ], className='sidebar-text')
                    ], href='https://themesberg.com/docs/volt-bootstrap-5-dashboard/getting-started/quick-start/', target='_blank', className='nav-link d-flex align-items-center')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../../assets/img/themesberg.svg', height='20', width='28', alt='Themesberg Logo')
                        ], className='sidebar-icon'),
                        html.Span("Themesberg", className='sidebar-text')
                    ], href='https://themesberg.com', target='_blank', className='nav-link d-flex align-items-center')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
                        html.Span("Upgrade to Pro")
                    ], href='../../pages/upgrade-to-pro.html', className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
                ], className='nav-item')
            ], className='nav flex-column pt-3 pt-md-0')
        ], className='sidebar-inner px-4 pt-3')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse', **{"data-simplebar": ""}),
    html.Main([
        html.Nav([
            html.Div([
                html.Div([
                    html.Div([
                        # Search form
                        html.Form([
                            html.Div([
                                html.Span([
                                    Svg([
                                        Path(fillRule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clipRule='evenodd')
                                    ], className='icon icon-xs', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 20 20', fill='currentColor', **{"aria-hidden": "true"})
                                ], className='input-group-text', id='topbar-addon'),
                                dcc.Input(type='text', className='form-control', id='topbarInputIconLeft', placeholder='Search')
                            ], className='input-group input-group-merge search-bar')
                        ], className='navbar-search form-inline', id='navbar-search-main'),
                        # / Search form
                    ], className='d-flex align-items-center'),
                    # Navbar links
                    html.Ul([
                        html.Li([
                            html.A([
                                Svg([
                                    Path(d='M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z')
                                ], className='icon icon-sm text-gray-900', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='nav-link text-dark notification-bell unread dropdown-toggle', href='#', role='button', **{"data-unread-notifications": "true", "data-bs-toggle": "dropdown", "data-bs-display": "static", "aria-expanded": "false"}),
                            html.Div([
                                html.Div([
                                    html.A("Notifications", href='#', className='text-center text-primary fw-bold border-bottom border-light py-3'),
                                    html.A([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.Img(alt='Image placeholder', src='../../assets/img/team/profile-picture-1.jpg', className='avatar-md rounded')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.Div([
                                                    html.Div([
                                                        html.H4("Jose Leos", className='h6 mb-0 text-small')
                                                    ]),
                                                    html.Div([
                                                        html.Small("a few moments ago", className='text-danger')
                                                    ], className='text-end')
                                                ], className='d-flex justify-content-between align-items-center'),
                                                html.P("Added you to an event \"Project stand-up\" tomorrow at 12:30 AM.", className='font-small mt-1 mb-0')
                                            ], className='col ps-0 ms-2')
                                        ], className='row align-items-center')
                                    ], href='#', className='list-group-item list-group-item-action border-bottom'),
                                    html.A([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.Img(alt='Image placeholder', src='../../assets/img/team/profile-picture-2.jpg', className='avatar-md rounded')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.Div([
                                                    html.Div([
                                                        html.H4("Neil Sims", className='h6 mb-0 text-small')
                                                    ]),
                                                    html.Div([
                                                        html.Small("2 hrs ago", className='text-danger')
                                                    ], className='text-end')
                                                ], className='d-flex justify-content-between align-items-center'),
                                                html.P("You've been assigned a task for \"Awesome new project\".", className='font-small mt-1 mb-0')
                                            ], className='col ps-0 ms-2')
                                        ], className='row align-items-center')
                                    ], href='#', className='list-group-item list-group-item-action border-bottom'),
                                    html.A([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.Img(alt='Image placeholder', src='../../assets/img/team/profile-picture-3.jpg', className='avatar-md rounded')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.Div([
                                                    html.Div([
                                                        html.H4("Roberta Casas", className='h6 mb-0 text-small')
                                                    ]),
                                                    html.Div([
                                                        html.Small("5 hrs ago")
                                                    ], className='text-end')
                                                ], className='d-flex justify-content-between align-items-center'),
                                                html.P("Tagged you in a document called \"Financial plans\",", className='font-small mt-1 mb-0')
                                            ], className='col ps-0 m-2')
                                        ], className='row align-items-center')
                                    ], href='#', className='list-group-item list-group-item-action border-bottom'),
                                    html.A([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.Img(alt='Image placeholder', src='../../assets/img/team/profile-picture-4.jpg', className='avatar-md rounded')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.Div([
                                                    html.Div([
                                                        html.H4("Joseph Garth", className='h6 mb-0 text-small')
                                                    ]),
                                                    html.Div([
                                                        html.Small("1 d ago")
                                                    ], className='text-end')
                                                ], className='d-flex justify-content-between align-items-center'),
                                                html.P("New message: \"Hey, what's up? All set for the presentation?\"", className='font-small mt-1 mb-0')
                                            ], className='col ps-0 ms-2')
                                        ], className='row align-items-center')
                                    ], href='#', className='list-group-item list-group-item-action border-bottom'),
                                    html.A([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.Img(alt='Image placeholder', src='../../assets/img/team/profile-picture-5.jpg', className='avatar-md rounded')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.Div([
                                                    html.Div([
                                                        html.H4("Bonnie Green", className='h6 mb-0 text-small')
                                                    ]),
                                                    html.Div([
                                                        html.Small("2 hrs ago")
                                                    ], className='text-end')
                                                ], className='d-flex justify-content-between align-items-center'),
                                                html.P("New message: \"We need to improve the UI/UX for the landing page.\"", className='font-small mt-1 mb-0')
                                            ], className='col ps-0 ms-2')
                                        ], className='row align-items-center')
                                    ], href='#', className='list-group-item list-group-item-action border-bottom'),
                                    html.A([
                                        Svg([
                                            Path(d='M10 12a2 2 0 100-4 2 2 0 000 4z'),
                                            Path(fillRule='evenodd', d='M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z', clipRule='evenodd')
                                        ], className='icon icon-xxs text-gray-400 me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        "View all"
                                    ], href='#', className='dropdown-item text-center fw-bold rounded-bottom py-3')
                                ], className='list-group list-group-flush')
                            ], className='dropdown-menu dropdown-menu-lg dropdown-menu-center mt-2 py-0')
                        ], className='nav-item dropdown'),
                        html.Li([
                            html.A([
                                html.Div([
                                    html.Img(className='avatar rounded-circle', alt='Image placeholder', src='../../assets/img/team/profile-picture-3.jpg'),
                                    html.Div([
                                        html.Span("Bonnie Green", className='mb-0 font-small fw-bold text-gray-900')
                                    ], className='media-body ms-2 text-dark align-items-center d-none d-lg-block')
                                ], className='media d-flex align-items-center')
                            ], className='nav-link dropdown-toggle pt-1 px-0', href='#', role='button', **{"data-bs-toggle": "dropdown", "aria-expanded": "false"}),
                            html.Div([
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z', clipRule='evenodd')
                                    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "My Profile"
                                ], className='dropdown-item d-flex align-items-center', href='#'),
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', clipRule='evenodd')
                                    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Settings"
                                ], className='dropdown-item d-flex align-items-center', href='#'),
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M5 3a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V5a2 2 0 00-2-2H5zm0 2h10v7h-2l-1 2H8l-1-2H5V5z', clipRule='evenodd')
                                    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Messages"
                                ], className='dropdown-item d-flex align-items-center', href='#'),
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-2 0c0 .993-.241 1.929-.668 2.754l-1.524-1.525a3.997 3.997 0 00.078-2.183l1.562-1.562C15.802 8.249 16 9.1 16 10zm-5.165 3.913l1.58 1.58A5.98 5.98 0 0110 16a5.976 5.976 0 01-2.516-.552l1.562-1.562a4.006 4.006 0 001.789.027zm-4.677-2.796a4.002 4.002 0 01-.041-2.08l-.08.08-1.53-1.533A5.98 5.98 0 004 10c0 .954.223 1.856.619 2.657l1.54-1.54zm1.088-6.45A5.974 5.974 0 0110 4c.954 0 1.856.223 2.657.619l-1.54 1.54a4.002 4.002 0 00-2.346.033L7.246 4.668zM12 10a2 2 0 11-4 0 2 2 0 014 0z', clipRule='evenodd')
                                    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Support"
                                ], className='dropdown-item d-flex align-items-center', href='#'),
                                html.Div(role='separator', className='dropdown-divider my-1'),
                                html.A([
                                    Svg([
                                        Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1')
                                    ], className='dropdown-icon text-danger me-2', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                                    "Logout"
                                ], className='dropdown-item d-flex align-items-center', href='#')
                            ], className='dropdown-menu dashboard-dropdown dropdown-menu-end mt-2 py-1')
                        ], className='nav-item dropdown ms-lg-3')
                    ], className='navbar-nav align-items-center')
                ], className='d-flex justify-content-between w-100', id='navbarSupportedContent')
            ], className='container-fluid px-0')
        ], className='navbar navbar-top navbar-expand navbar-dashboard navbar-dark ps-0 pe-2 pb-0'),
        html.Div([
            html.Div([
                html.Button([
                    Svg([
                        Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M12 6v6m0 0v6m0-6h6m-6 0H6')
                    ], className='icon icon-xs me-2', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                    "New Task"
                ], className='btn btn-gray-800 d-inline-flex align-items-center me-2 dropdown-toggle', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                html.Div([
                    html.A([
                        Svg([
                            Path(d='M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Add User"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(d='M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Add Widget"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(d='M5.5 13a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 13H11V9.413l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13H5.5z'),
                            Path(d='M9 13h2v5a1 1 0 11-2 0v-5z')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Upload Files"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(fillRule='evenodd', d='M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z', clipRule='evenodd')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Preview Security"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.Div(role='separator', className='dropdown-divider my-1'),
                    html.A([
                        Svg([
                            Path(fillRule='evenodd', d='M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z', clipRule='evenodd')
                        ], className='dropdown-icon text-danger me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Upgrade to Pro"
                    ], className='dropdown-item d-flex align-items-center', href='#')
                ], className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')
            ], className='dropdown')
        ], className='py-4'),
        html.Div([
            html.Div([
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
            ], className='col-12 mb-4'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    Svg([
                                        Path(d='M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z')
                                    ], className='icon', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                ], className='icon-shape icon-shape-primary rounded me-4 me-sm-0'),
                                html.Div([
                                    html.H2("Customers", className='h5'),
                                    html.H3("345,678", className='fw-extrabold mb-1')
                                ], className='d-sm-none')
                            ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
                            html.Div([
                                html.Div([
                                    html.H2("Customers", className='h6 text-gray-400 mb-0'),
                                    html.H3("345k", className='fw-extrabold mb-2')
                                ], className='d-none d-sm-block'),
                                html.Small([
                                    "Feb 1 - Apr 1,",
                                    Svg([
                                        Path(fillRule='evenodd', d='M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z', clipRule='evenodd')
                                    ], className='icon icon-xxs text-gray-500 ms-2 me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "USA"
                                ], className='d-flex align-items-center text-gray-500'),
                                html.Div([
                                    html.Div([
                                        "Since last month",
                                        Svg([
                                            Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                        ], className='icon icon-xs text-success', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        html.Span("22%", className='text-success fw-bolder')
                                    ])
                                ], className='small d-flex mt-1')
                            ], className='col-12 col-xl-7 px-xl-0')
                        ], className='row d-block d-xl-flex align-items-center')
                    ], className='card-body')
                ], className='card border-0 shadow')
            ], className='col-12 col-sm-6 col-xl-4 mb-4'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z', clipRule='evenodd')
                                    ], className='icon', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                ], className='icon-shape icon-shape-secondary rounded me-4 me-sm-0'),
                                html.Div([
                                    html.H2("Revenue", className='fw-extrabold h5'),
                                    html.H3("$43,594", className='mb-1')
                                ], className='d-sm-none')
                            ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
                            html.Div([
                                html.Div([
                                    html.H2("Revenue", className='h6 text-gray-400 mb-0'),
                                    html.H3("$43,594", className='fw-extrabold mb-2')
                                ], className='d-none d-sm-block'),
                                html.Small([
                                    "Feb 1 - Apr 1,",
                                    Svg([
                                        Path(fillRule='evenodd', d='M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z', clipRule='evenodd')
                                    ], className='icon icon-xxs text-gray-500 ms-2 me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "GER"
                                ], className='d-flex align-items-center text-gray-500'),
                                html.Div([
                                    html.Div([
                                        "Since last month",
                                        Svg([
                                            Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                                        ], className='icon icon-xs text-danger', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        html.Span("2%", className='text-danger fw-bolder')
                                    ])
                                ], className='small d-flex mt-1')
                            ], className='col-12 col-xl-7 px-xl-0')
                        ], className='row d-block d-xl-flex align-items-center')
                    ], className='card-body')
                ], className='card border-0 shadow')
            ], className='col-12 col-sm-6 col-xl-4 mb-4'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    Svg([
                                        Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
                                    ], className='icon', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                ], className='icon-shape icon-shape-tertiary rounded me-4 me-sm-0'),
                                html.Div([
                                    html.H2("Bounce Rate", className='fw-extrabold h5'),
                                    html.H3("50.88%", className='mb-1')
                                ], className='d-sm-none')
                            ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
                            html.Div([
                                html.Div([
                                    html.H2("Bounce Rate", className='h6 text-gray-400 mb-0'),
                                    html.H3("50.88%", className='fw-extrabold mb-2')
                                ], className='d-none d-sm-block'),
                                html.Small("Feb 1 - Apr 1", className='text-gray-500'),
                                html.Div([
                                    html.Div([
                                        "Since last month",
                                        Svg([
                                            Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                        ], className='icon icon-xs text-success', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        html.Span("4%", className='text-success fw-bolder')
                                    ])
                                ], className='small d-flex mt-1')
                            ], className='col-12 col-xl-7 px-xl-0')
                        ], className='row d-block d-xl-flex align-items-center')
                    ], className='card-body')
                ], className='card border-0 shadow')
            ], className='col-12 col-sm-6 col-xl-4 mb-4')
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
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
                    ], className='col-12 mb-4'),
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Team members", className='fs-5 fw-bold mb-0'),
                                html.A("See all", href='#', className='btn btn-sm btn-primary')
                            ], className='card-header border-bottom d-flex align-items-center justify-content-between'),
                            html.Div([
                                html.Ul([
                                    html.Li([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.A([
                                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-1.jpg')
                                                ], href='#', className='avatar')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.H4([
                                                    html.A("Chris Wood", href='#')
                                                ], className='h6 mb-0'),
                                                html.Div([
                                                    html.Div(className='bg-success dot rounded-circle me-1'),
                                                    html.Small("Online")
                                                ], className='d-flex align-items-center')
                                            ], className='col-auto ms--2'),
                                            html.Div([
                                                html.A([
                                                    Svg([
                                                        Path(fillRule='evenodd', d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z', clipRule='evenodd')
                                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                                    "Invite"
                                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                                            ], className='col text-end')
                                        ], className='row align-items-center')
                                    ], className='list-group-item px-0'),
                                    html.Li([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.A([
                                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-2.jpg')
                                                ], href='#', className='avatar')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.H4([
                                                    html.A("Jose Leos", href='#')
                                                ], className='h6 mb-0'),
                                                html.Div([
                                                    html.Div(className='bg-warning dot rounded-circle me-1'),
                                                    html.Small("In a meeting")
                                                ], className='d-flex align-items-center')
                                            ], className='col-auto ms--2'),
                                            html.Div([
                                                html.A([
                                                    Svg([
                                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                                    "Message"
                                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                                            ], className='col text-end')
                                        ], className='row align-items-center')
                                    ], className='list-group-item px-0'),
                                    html.Li([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.A([
                                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-3.jpg')
                                                ], href='#', className='avatar')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.H4([
                                                    html.A("Bonnie Green", href='#')
                                                ], className='h6 mb-0'),
                                                html.Div([
                                                    html.Div(className='bg-danger dot rounded-circle me-1'),
                                                    html.Small("Offline")
                                                ], className='d-flex align-items-center')
                                            ], className='col-auto ms--2'),
                                            html.Div([
                                                html.A([
                                                    Svg([
                                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                                    "Message"
                                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                                            ], className='col text-end')
                                        ], className='row align-items-center')
                                    ], className='list-group-item px-0'),
                                    html.Li([
                                        html.Div([
                                            html.Div([
                                                # Avatar
                                                html.A([
                                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-4.jpg')
                                                ], href='#', className='avatar')
                                            ], className='col-auto'),
                                            html.Div([
                                                html.H4([
                                                    html.A("Neil Sims", href='#')
                                                ], className='h6 mb-0'),
                                                html.Div([
                                                    html.Div(className='bg-danger dot rounded-circle me-1'),
                                                    html.Small("Offline")
                                                ], className='d-flex align-items-center')
                                            ], className='col-auto ms--2'),
                                            html.Div([
                                                html.A([
                                                    Svg([
                                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                                    "Message"
                                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                                            ], className='col text-end')
                                        ], className='row align-items-center')
                                    ], className='list-group-item px-0')
                                ], className='list-group list-group-flush list my--3')
                            ], className='card-body')
                        ], className='card border-0 shadow')
                    ], className='col-12 col-xxl-6 mb-4'),
                    html.Div([
                        html.Div([
                            html.Div([
                                html.H2("Progress track", className='fs-5 fw-bold mb-0'),
                                html.A("See tasks", href='#', className='btn btn-sm btn-primary')
                            ], className='card-header border-bottom d-flex align-items-center justify-content-between'),
                            html.Div([
                                # Project 1
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                                            Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                                        ], className='icon icon-sm text-gray-500', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='col-auto'),
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.Div("Rocket - SaaS Template", className='h6 mb-0'),
                                                html.Div([
                                                    html.Span("75 %")
                                                ], className='small fw-bold text-gray-500')
                                            ], className='progress-info'),
                                            html.Div([
                                                html.Div(className='progress-bar bg-success', role='progressbar', style='width: 75%;', **{"aria-valuenow": "75", "aria-valuemin": "0", "aria-valuemax": "100"})
                                            ], className='progress mb-0')
                                        ], className='progress-wrapper')
                                    ], className='col')
                                ], className='row mb-4'),
                                # Project 2
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                                            Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                                        ], className='icon icon-sm text-gray-500', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='col-auto'),
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.Div("Themesberg - Design System", className='h6 mb-0'),
                                                html.Div([
                                                    html.Span("60 %")
                                                ], className='small fw-bold text-gray-500')
                                            ], className='progress-info'),
                                            html.Div([
                                                html.Div(className='progress-bar bg-success', role='progressbar', style='width: 60%;', **{"aria-valuenow": "60", "aria-valuemin": "0", "aria-valuemax": "100"})
                                            ], className='progress mb-0')
                                        ], className='progress-wrapper')
                                    ], className='col')
                                ], className='row align-items-center mb-4'),
                                # Project 3
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                                            Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                                        ], className='icon icon-sm text-gray-500', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='col-auto'),
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.Div("Homepage Design in Figma", className='h6 mb-0'),
                                                html.Div([
                                                    html.Span("45 %")
                                                ], className='small fw-bold text-gray-500')
                                            ], className='progress-info'),
                                            html.Div([
                                                html.Div(className='progress-bar bg-warning', role='progressbar', style='width: 45%;', **{"aria-valuenow": "45", "aria-valuemin": "0", "aria-valuemax": "100"})
                                            ], className='progress mb-0')
                                        ], className='progress-wrapper')
                                    ], className='col')
                                ], className='row align-items-center mb-4'),
                                # Project 4
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                                            Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                                        ], className='icon icon-sm text-gray-500', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='col-auto'),
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.Div("Backend for Themesberg v2", className='h6 mb-0'),
                                                html.Div([
                                                    html.Span("34 %")
                                                ], className='small fw-bold text-gray-500')
                                            ], className='progress-info'),
                                            html.Div([
                                                html.Div(className='progress-bar bg-danger', role='progressbar', style='width: 34%;', **{"aria-valuenow": "34", "aria-valuemin": "0", "aria-valuemax": "100"})
                                            ], className='progress mb-0')
                                        ], className='progress-wrapper')
                                    ], className='col')
                                ], className='row align-items-center mb-3')
                            ], className='card-body')
                        ], className='card border-0 shadow')
                    ], className='col-12 col-xxl-6 mb-4')
                ], className='row')
            ], className='col-12 col-xl-8'),
            html.Div([
                html.Div([
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
                ], className='col-12 px-0 mb-4'),
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(fillRule='evenodd', d='M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z', clipRule='evenodd')
                                        ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        "Global Rank"
                                    ], className='h6 mb-0 d-flex align-items-center')
                                ]),
                                html.Div([
                                    html.A([
                                        #755
                                        Svg([
                                            Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
                                        ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], href='#', className='d-flex align-items-center fw-bold')
                                ])
                            ], className='d-flex align-items-center justify-content-between border-bottom pb-3'),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(fillRule='evenodd', d='M3 6a3 3 0 013-3h10a1 1 0 01.8 1.6L14.25 8l2.55 3.4A1 1 0 0116 13H6a1 1 0 00-1 1v3a1 1 0 11-2 0V6z', clipRule='evenodd')
                                        ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        "Country Rank"
                                    ], className='h6 mb-0 d-flex align-items-center'),
                                    html.Div([
                                        "United States",
                                        Svg([
                                            Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                        ], className='icon icon-xs text-success', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='small card-stats')
                                ]),
                                html.Div([
                                    html.A([
                                        #32
                                        Svg([
                                            Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
                                        ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], href='#', className='d-flex align-items-center fw-bold')
                                ])
                            ], className='d-flex align-items-center justify-content-between border-bottom py-3'),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        Svg([
                                            Path(fillRule='evenodd', d='M2 6a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1H8a3 3 0 00-3 3v1.5a1.5 1.5 0 01-3 0V6z', clipRule='evenodd'),
                                            Path(d='M6 12a2 2 0 012-2h8a2 2 0 012 2v2a2 2 0 01-2 2H2h2a2 2 0 002-2v-2z')
                                        ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                        "Category Rank"
                                    ], className='h6 mb-0 d-flex align-items-center'),
                                    html.Div([
                                        "Computers Electronics > Technology",
                                        Svg([
                                            Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
                                        ], className='icon icon-xs text-success', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='small card-stats')
                                ]),
                                html.Div([
                                    html.A([
                                        #11
                                        Svg([
                                            Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
                                        ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], href='#', className='d-flex align-items-center fw-bold')
                                ])
                            ], className='d-flex align-items-center justify-content-between pt-3')
                        ], className='card-body')
                    ], className='card border-0 shadow')
                ], className='col-12 px-0 mb-4'),
                html.Div([
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
            ], className='col-12 col-xl-4')
        ], className='row'),
        html.Div([
            html.Div([
                dcc.Input(type='button', className='btn-close theme-settings-close'),
                html.Div([
                    html.P([
                        "Open source",
                        html.Span("💛", role='img', **{"aria-label": "gratitude"})
                    ], className='m-0 mb-1 me-4 fs-7'),
                    html.A("Star", className='github-button', href='https://github.com/themesberg/volt-bootstrap-5-dashboard', **{"data-color-scheme": "no-preference: dark; light: light; dark: light;", "data-icon": "octicon-star", "data-size": "large", "data-show-count": "true", "aria-label": "Star themesberg/volt-bootstrap-5-dashboard on GitHub"})
                ], className='d-flex justify-content-between align-items-center mb-3'),
                html.A([
                    "Download",
                    Svg([
                        Path(fillRule='evenodd', d='M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z', clipRule='evenodd')
                    ], className='icon icon-xs ms-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                ], href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard', target='_blank', className='btn btn-secondary d-inline-flex align-items-center justify-content-center mb-3 w-100'),
                html.P("Available in the following technologies:", className='fs-7 text-gray-300 text-center'),
                html.Div([
                    html.A([
                        html.Img(src='../../assets/img/technologies/bootstrap-5-logo.svg', className='image image-xs')
                    ], className='me-3', href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard', target='_blank'),
                    html.A([
                        html.Img(src='../../assets/img/technologies/react-logo.svg', className='image image-xs')
                    ], href='https://demo.themesberg.com/volt-react-dashboard/#/', target='_blank')
                ], className='d-flex justify-content-center')
            ], className='card-body bg-gray-800 text-white pt-4')
        ], className='theme-settings card bg-gray-800 pt-2 collapse', id='theme-settings'),
        html.Div([
            html.Div([
                html.Span([
                    Svg([
                        Path(fillRule='evenodd', d='M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', clipRule='evenodd')
                    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                    "Settings"
                ], className='fw-bold d-inline-flex align-items-center h6')
            ], className='card-body bg-gray-800 text-white rounded-top p-3 py-2')
        ], className='card theme-settings bg-gray-800 theme-settings-expand', id='theme-settings-expand'),
        html.Footer([
            html.Div([
                html.Div([
                    html.P([
                        "© 2019-",
                        html.Span(className='current-year'),
                        html.A("Themesberg", className='text-primary fw-normal', href='https://themesberg.com', target='_blank')
                    ], className='mb-0 text-center text-lg-start')
                ], className='col-12 col-md-4 col-xl-6 mb-4 mb-md-0'),
                html.Div([
                    # List
                    html.Ul([
                        html.Li([
                            html.A("About", href='https://themesberg.com/about')
                        ], className='list-inline-item px-0 px-sm-2'),
                        html.Li([
                            html.A("Themes", href='https://themesberg.com/themes')
                        ], className='list-inline-item px-0 px-sm-2'),
                        html.Li([
                            html.A("Blog", href='https://themesberg.com/blog')
                        ], className='list-inline-item px-0 px-sm-2'),
                        html.Li([
                            html.A("Contact", href='https://themesberg.com/contact')
                        ], className='list-inline-item px-0 px-sm-2')
                    ], className='list-inline list-group-flush list-group-borderless text-md-end mb-0')
                ], className='col-12 col-md-8 col-xl-6 text-center text-lg-start')
            ], className='row')
        ], className='bg-white rounded shadow p-5 mb-4 mt-4')
    ], className='content')

])
