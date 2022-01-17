from dash import html, dcc
from dash_svg import Svg, Path

def sideBar():
    return html.Nav([
        html.Div([

            # Mobile Menu Header, visibility controlled by CSS media rules

            html.Div([
                html.Div([
                    html.Div([
                        html.A([
                            Svg([
                                Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1')
                            ], className='icon icon-xxs me-1', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                            "Sign Out"
                        ], href='../pages/examples/sign-in.html', className='btn btn-secondary btn-sm d-inline-flex align-items-center')
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

            # Sidebar List of entries

            html.Ul([

                # Overview

                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../assets/img/brand/light.svg', height='20', width='20', alt='Volt Logo')
                        ], className='sidebar-icon'),
                        html.Span("Volt Overview", className='mt-1 ms-1 sidebar-text')
                    ], href='https://demo.themesberg.com/volt/pages/dashboard/dashboard.html', className='nav-link d-flex align-items-center')
                ], className='nav-item'),
                # Sidebar & Mobile - menu links

                # Dashboard Link

                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(d='M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z'),
                                Path(d='M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span("Dashboard", className='sidebar-text')
                    ], href='../pages/dashboard/dashboard-ref.html', className='nav-link')
                ], className='nav-item active'),

                # Settings Link

                html.Li([
                    html.A([
                        html.Span([
                                Svg([
                                    Path(d='M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon'),
                        html.Span("Settings", className='sidebar-text')
                    ], href='../pages/settings-combined.html', className='nav-link')
                ], className='nav-item'),

                # Calendar Link

                html.Li([
                    html.A([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z", clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                            ], className='sidebar-icon'),
                            html.Span("Calendar", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Span("Pro", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ])
                    ], href='https://demo.themesberg.com/volt-pro/pages/calendar.html', target='_blank', className='nav-link d-flex justify-content-between')
                ], className='nav-item'),

                # Page examples drop down

                html.Li([

                    # Dropdown button

                    html.Span([
                        html.Span([
                            html.Span([
                                Svg([
                                    Path(fillRule='evenodd', d='M5 4a3 3 0 00-3 3v6a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H5zm-1 9v-1h5v2H5a1 1 0 01-1-1zm7 1h4a1 1 0 001-1v-1h-5v2zm0-4h5V8h-5v2zM9 8H4v2h5V8z', clipRule='evenodd')
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

                    # Drop down content - example page links

                    html.Div([
                        html.Ul([
                            html.Li([
                                html.A([
                                    html.Span("Sign In", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/sign-in.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Sign Up", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/sign-up.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Forgot password", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/forgot-password.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Reset password", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/reset-password.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("Lock", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/lock.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("404 Not Found", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/404.html')
                            ], className='nav-item'),
                            html.Li([
                                html.A([
                                    html.Span("500 Not Found", className='sidebar-text')
                                ], className='nav-link', href='../pages/examples/500.html')
                            ], className='nav-item')
                        ], className='flex-column nav')
                    ], className='multi-level collapse', role='list', id='submenu-pages', **{"aria-expanded": "false"})

                ], className='nav-item'),

                # Bottom Item

                html.Li([
                    html.A([
                        html.Span([
                            Svg([
                                Path(fillRule='evenodd', d='M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
                        html.Span("Upgrade to Pro")
                    ], href='../pages/upgrade-to-pro.html', className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
                ], className='nav-item')

            ], className='nav flex-column pt-3 pt-md-0')


        ], className='sidebar-inner px-4 pt-3')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse', **{"data-simplebar": ""})
