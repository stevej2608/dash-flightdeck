from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from dash_svg import Svg, Path

register_page(__name__, path="/volt", title="Volt Clone")

layout = html.Div([
    # Mobile only navbar - Volt logo & burger button
    html.Nav([
        html.A([
            html.Img(src='../assets/img/brand/light.svg', alt='Volt logo')
        ], className='navbar-brand me-lg-5', href='../index.html'),
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
                html.Div([
                    html.Div([
                        html.A([
                            html.Img(className='icon icon-sm', src='../assets/img/icons/sign_out.svg', height='20', width='20', alt='upgrade'),
                            "Sign Out"
                        ], href='../pages/examples/sign-in.html', className='btn btn-secondary btn-sm d-inline-flex align-items-center')
                    ], className='d-block')
                ], className='d-flex align-items-center'),
                html.Div([
                    html.A([
                        html.Img(src='../assets/img/icons/cross.svg')
                    ], href='#sidebarMenu', **{"data-bs-toggle": "collapse", "data-bs-target": "#sidebarMenu", "aria-controls": "sidebarMenu", "aria-expanded": "true", "aria-label": "Toggle navigation"})
                ], className='collapse-close d-md-none')
            ], className='user-card d-flex d-md-none align-items-center justify-content-between justify-content-md-center pb-4'),
            # Sidebar Brand
            html.Ul([
                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../assets/img/brand/light.svg', height='20', width='20', alt='Volt Logo')
                        ], className='sidebar-icon'),
                        html.Span("Volt Overview", className='mt-1 ms-1 sidebar-text')
                    ], href='../pages/dashboard/dashboard-ref.html', className='nav-link d-flex align-items-center')
                ], className='nav-item'),
                # Sidebar & Mobile - menu links
                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../assets/img/icons/dashboard.svg', className='icon icon-xs me-2', height='20', width='20', alt='Dashboard')
                        ], className='sidebar-icon'),
                        html.Span("Dashboard", className='sidebar-text')
                    ], href='../pages/dashboard/dashboard-ref.html', className='nav-link')
                ], className='nav-item active'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Img(src='../assets/img/icons/settings.svg', className='icon icon-xs me-2', height='20', width='20', alt='Dashboard')
                        ], className='sidebar-icon'),
                        html.Span("Settings", className='sidebar-text')
                    ], href='../pages/settings-combined.html', className='nav-link')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        html.Span([
                            html.Span([
                                html.Img(src='../assets/img/icons/calender.svg', className='icon icon-xs me-2', height='20', width='20', alt='Calender')
                            ], className='sidebar-icon'),
                            html.Span("Calendar", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Span("Pro", className='badge badge-sm bg-secondary ms-1 text-gray-800')
                        ])
                    ], href='https://demo.themesberg.com/volt-pro/pages/calendar.html', target='_blank', className='nav-link d-flex justify-content-between')
                ], className='nav-item'),
                html.Li([
                    html.Span([
                        html.Span([
                            html.Span([
                                html.Img(src='../assets/img/icons/pages.svg', className='icon icon-xs me-2', height='20', width='20', alt='Calender')
                            ], className='sidebar-icon'),
                            html.Span("Page examples", className='sidebar-text')
                        ]),
                        html.Span([
                            html.Img(src='../assets/img/icons/link_arrow.svg', height='24', width='24', alt='arrow')
                        ], className='link-arrow')
                    ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-pages"}),
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
                            html.Img(className='icon icon-xs me-2', src='../assets/img/icons/upgrade.svg', height='20', width='20', alt='upgrade')
                        ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
                        html.Span("Upgrade to Pro")
                    ], href='../pages/upgrade-to-pro.html', className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
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
                                    html.Img(className='icon icon-sm', src='../assets/img/icons/search.svg', height='20', width='20', alt='upgrade')
                                ], className='input-group-text', id='topbar-addon'),
                                dbc.Input(type='text', className='form-control', id='topbarInputIconLeft', placeholder='Search')
                            ], className='input-group input-group-merge search-bar')
                        ], className='navbar-search form-inline', id='navbar-search-main'),
                        # / Search form
                    ], className='d-flex align-items-center')
                ], className='d-flex justify-content-between w-100', id='navbarSupportedContent')
            ], className='container-fluid px-0')
        ], className='navbar navbar-top navbar-expand navbar-dashboard navbar-dark ps-0 pe-2 pb-0'),
        html.Div([
            html.Div([
                html.Div([
                    html.Button([
                        Svg([
                            Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M12 6v6m0 0v6m0-6h6m-6 0H6')
                        ], className='icon icon-xs me-2', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),
                        "New"
                    ], className='btn btn-secondary d-inline-flex align-items-center me-2 dropdown-toggle', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                    html.Div([
                        html.A([
                            Svg([
                                Path(fillRule='evenodd', d='M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z', clipRule='evenodd')
                            ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            "Document"
                        ], className='dropdown-item d-flex align-items-center', href='#'),
                        html.A([
                            Svg([
                                Path(fillRule='evenodd', d='M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z', clipRule='evenodd')
                            ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            "Message"
                        ], className='dropdown-item d-flex align-items-center', href='#'),
                        html.A([
                            Svg([
                                Path(d='M5.5 13a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 13H11V9.413l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13H5.5z'),
                                Path(d='M9 13h2v5a1 1 0 11-2 0v-5z')
                            ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            "Product"
                        ], className='dropdown-item d-flex align-items-center', href='#'),
                        html.Div(role='separator', className='dropdown-divider my-1'),
                        html.A([
                            Svg([
                                Path(fillRule='evenodd', d='M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z', clipRule='evenodd')
                            ], className='dropdown-icon text-danger me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            "My Plan"
                        ], className='dropdown-item d-flex align-items-center', href='#')
                    ], className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')
                ], className='dropdown')
            ]),
            html.Div([
                dbc.Button([
                    Svg([
                        Path(fillRule='evenodd', d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z', clipRule='evenodd')
                    ], className='icon icon-xs', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                ], type='button', className='btn btn-gray-800 d-inline-flex align-items-center me-2'),
                html.Button([
                    Svg([
                        Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                        Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                    "Reports",
                    Svg([
                        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
                    ], className='icon icon-xs ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                ], className='btn btn-gray-800 d-inline-flex align-items-center dropdown-toggle', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                html.Div([
                    html.A([
                        Svg([
                            Path(d='M4 3a2 2 0 100 4h12a2 2 0 100-4H4z'),
                            Path(fillRule='evenodd', d='M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z', clipRule='evenodd')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Products"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(d='M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Customers"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(fillRule='evenodd', d='M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z', clipRule='evenodd')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Orders"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.A([
                        Svg([
                            Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z', clipRule='evenodd')
                        ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "Console"
                    ], className='dropdown-item d-flex align-items-center', href='#'),
                    html.Div(role='separator', className='dropdown-divider my-1'),
                    html.A([
                        Svg([
                            Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                            Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
                        ], className='dropdown-icon text-gray-800 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        "All Reports"
                    ], className='dropdown-item d-flex align-items-center', href='#')
                ], className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')
            ])
        ], className='d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center py-4'),
        html.Div([
            html.Div([
                html.Div([
                    html.H2("General information", className='h5 mb-4'),
                    html.Form([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("First Name", htmlFor='first_name'),
                                    dbc.Input(className='form-control', id='first_name', type='text', placeholder='Enter your first name', required='')
                                ])
                            ], className='col-md-6 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Last Name", htmlFor='last_name'),
                                    dbc.Input(className='form-control', id='last_name', type='text', placeholder='Also your last name', required='')
                                ])
                            ], className='col-md-6 mb-3')
                        ], className='row'),
                        html.Div([
                            html.Div([
                                html.Label("Birthday", htmlFor='birthday'),
                                html.Div([
                                    html.Span([
                                        Svg([
                                            Path(fillRule='evenodd', d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z', clipRule='evenodd')
                                        ], className='icon icon-xs', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                                    ], className='input-group-text'),
                                    dbc.Input(className='form-control', id='birthday', type='text', placeholder='dd/mm/yyyy', required='')
                                ], className='input-group')
                            ], className='col-md-6 mb-3'),
                            html.Div([
                                html.Label("Gender", htmlFor='gender'),
                                html.Select([
                                    html.Option("Gender", selected=''),
                                    html.Option("Female", value='1'),
                                    html.Option("Male", value='2')
                                ], className='form-select mb-0', id='gender', **{"aria-label": "Gender select example"})
                            ], className='col-md-6 mb-3')
                        ], className='row align-items-center'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("Email", htmlFor='email'),
                                    dbc.Input(className='form-control', id='email', type='email', placeholder='name@company.com', required='')
                                ], className='form-group')
                            ], className='col-md-6 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Phone", htmlFor='phone'),
                                    dbc.Input(className='form-control', id='phone', type='number', placeholder='+12-345 678 910', required='')
                                ], className='form-group')
                            ], className='col-md-6 mb-3')
                        ], className='row'),
                        html.H2("Location", className='h5 my-4'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("Address", htmlFor='address'),
                                    dbc.Input(className='form-control', id='address', type='text', placeholder='Enter your home address', required='')
                                ], className='form-group')
                            ], className='col-sm-9 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Number", htmlFor='number'),
                                    dbc.Input(className='form-control', id='number', type='number', placeholder='No.', required='')
                                ], className='form-group')
                            ], className='col-sm-3 mb-3')
                        ], className='row'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("City", htmlFor='city'),
                                    dbc.Input(className='form-control', id='city', type='text', placeholder='City', required='')
                                ], className='form-group')
                            ], className='col-sm-4 mb-3'),
                            html.Div([
                                html.Label("State", htmlFor='state'),
                                html.Select([
                                    html.Option("State", selected=''),
                                    html.Option("Alabama", value='AL'),
                                    html.Option("Alaska", value='AK'),
                                    html.Option("Arizona", value='AZ'),
                                    html.Option("Arkansas", value='AR'),
                                    html.Option("California", value='CA'),
                                    html.Option("Colorado", value='CO'),
                                    html.Option("Connecticut", value='CT'),
                                    html.Option("Delaware", value='DE'),
                                    html.Option("District Of Columbia", value='DC'),
                                    html.Option("Florida", value='FL'),
                                    html.Option("Georgia", value='GA'),
                                    html.Option("Hawaii", value='HI'),
                                    html.Option("Idaho", value='ID'),
                                    html.Option("Illinois", value='IL'),
                                    html.Option("Indiana", value='IN'),
                                    html.Option("Iowa", value='IA'),
                                    html.Option("Kansas", value='KS'),
                                    html.Option("Kentucky", value='KY'),
                                    html.Option("Louisiana", value='LA'),
                                    html.Option("Maine", value='ME'),
                                    html.Option("Maryland", value='MD'),
                                    html.Option("Massachusetts", value='MA'),
                                    html.Option("Michigan", value='MI'),
                                    html.Option("Minnesota", value='MN'),
                                    html.Option("Mississippi", value='MS'),
                                    html.Option("Missouri", value='MO'),
                                    html.Option("Montana", value='MT'),
                                    html.Option("Nebraska", value='NE'),
                                    html.Option("Nevada", value='NV'),
                                    html.Option("New Hampshire", value='NH'),
                                    html.Option("New Jersey", value='NJ'),
                                    html.Option("New Mexico", value='NM'),
                                    html.Option("New York", value='NY'),
                                    html.Option("North Carolina", value='NC'),
                                    html.Option("North Dakota", value='ND'),
                                    html.Option("Ohio", value='OH'),
                                    html.Option("Oklahoma", value='OK'),
                                    html.Option("Oregon", value='OR'),
                                    html.Option("Pennsylvania", value='PA'),
                                    html.Option("Rhode Island", value='RI'),
                                    html.Option("South Carolina", value='SC'),
                                    html.Option("South Dakota", value='SD'),
                                    html.Option("Tennessee", value='TN'),
                                    html.Option("Texas", value='TX'),
                                    html.Option("Utah", value='UT'),
                                    html.Option("Vermont", value='VT'),
                                    html.Option("Virginia", value='VA'),
                                    html.Option("Washington", value='WA'),
                                    html.Option("West Virginia", value='WV'),
                                    html.Option("Wisconsin", value='WI'),
                                    html.Option("Wyoming", value='WY')
                                ], className='form-select w-100 mb-0', id='state', name='state', **{"aria-label": "State select example"})
                            ], className='col-sm-4 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("ZIP", htmlFor='zip'),
                                    dbc.Input(className='form-control', id='zip', type='tel', placeholder='ZIP', required='')
                                ], className='form-group')
                            ], className='col-sm-4')
                        ], className='row'),
                        html.Div([
                            dbc.Button("Save all", className='btn btn-gray-800 mt-2 animate-up-2', type='submit')
                        ], className='mt-3')
                    ])
                ], className='card card-body border-0 shadow mb-4'),
                html.Div([
                    html.H2("Alerts & Notifications", className='h5 mb-4'),
                    html.Ul([
                        html.Li([
                            html.Div([
                                html.H3("Company News", className='h6 mb-1'),
                                html.P("Get Rocket news, announcements, and product updates", className='small pe-4')
                            ]),
                            html.Div([
                                html.Div([
                                    dbc.Input(className='form-check-input', type='checkbox', id='user-notification-1'),
                                    html.Label(className='form-check-label', htmlFor='user-notification-1')
                                ], className='form-check form-switch')
                            ])
                        ], className='list-group-item d-flex align-items-center justify-content-between px-0 border-bottom'),
                        html.Li([
                            html.Div([
                                html.H3("Account Activity", className='h6 mb-1'),
                                html.P("Get important notifications about you or activity you've missed", className='small pe-4')
                            ]),
                            html.Div([
                                html.Div([
                                    dbc.Checkbox(className='form-check-input', id='user-notification-2', value=False),
                                    html.Label(className='form-check-label', htmlFor='user-notification-2')
                                ], className='form-check form-switch')
                            ])
                        ], className='list-group-item d-flex align-items-center justify-content-between px-0 border-bottom'),
                        html.Li([
                            html.Div([
                                html.H3("Meetups Near You", className='h6 mb-1'),
                                html.P("Get an email when a Dribbble Meetup is posted close to my location", className='small pe-4')
                            ]),
                            html.Div([
                                html.Div([
                                    dbc.Checkbox(className='form-check-input', id='user-notification-3', value=False),
                                    html.Label(className='form-check-label', htmlFor='user-notification-3')
                                ], className='form-check form-switch')
                            ])
                        ], className='list-group-item d-flex align-items-center justify-content-between px-0')
                    ], className='list-group list-group-flush')
                ], className='card card-body border-0 shadow mb-4 mb-xl-0')
            ], className='col-12 col-xl-8'),
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div(className='profile-cover rounded-top', **{"data-background": "../assets/img/profile-cover.jpg"}),
                            html.Div([
                                html.Img(src='../assets/img/team/profile-picture-1.jpg', className='avatar-xl rounded-circle mx-auto mt-n7 mb-4', alt='Neil Portrait'),
                                html.H4("Neil Sims", className='h3'),
                                html.H5("Senior Software Engineer", className='fw-normal'),
                                html.P("New York, USA", className='text-gray mb-4'),
                                html.A([
                                    Svg([
                                        Path(d='M8 9a3 3 0 100-6 3 3 0 000 6zM8 11a6 6 0 016 6H2a6 6 0 016-6zM16 7a1 1 0 10-2 0v1h-1a1 1 0 100 2h1v1a1 1 0 102 0v-1h1a1 1 0 100-2h-1V7z')
                                    ], className='icon icon-xs me-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Connect"
                                ], className='btn btn-sm btn-gray-800 d-inline-flex align-items-center me-2', href='#'),
                                html.A("Send Message", className='btn btn-sm btn-secondary', href='#')
                            ], className='card-body pb-5')
                        ], className='card shadow border-0 text-center p-0')
                    ], className='col-12 mb-4'),
                    html.Div([
                        html.Div([
                            html.H2("Select profile photo", className='h5 mb-4'),
                            html.Div([
                                html.Div([
                                    # Avatar
                                    html.Img(className='rounded avatar-xl', src='../assets/img/team/profile-picture-3.jpg', alt='change avatar')
                                ], className='me-3'),
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            Svg([
                                                Path(fillRule='evenodd', d='M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z', clipRule='evenodd')
                                            ], className='icon text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                            dbc.Input(type='file'),
                                            html.Div([
                                                html.Div("Choose Image", className='fw-normal text-dark mb-1'),
                                                html.Div("JPG, GIF or PNG. Max size of 800K", className='text-gray small')
                                            ], className='d-md-block text-left')
                                        ], className='d-flex')
                                    ], className='d-flex justify-content-xl-center ms-xl-3')
                                ], className='file-field')
                            ], className='d-flex align-items-center')
                        ], className='card card-body border-0 shadow mb-4')
                    ], className='col-12'),
                    html.Div([
                        html.Div([
                            html.H2("Select cover photo", className='h5 mb-4'),
                            html.Div([
                                html.Div([
                                    # Avatar
                                    html.Img(className='rounded avatar-xl', src='../assets/img/profile-cover.jpg', alt='change cover')
                                ], className='me-3'),
                                html.Div([
                                    html.Div([
                                        html.Div([
                                            Svg([
                                                Path(fillRule='evenodd', d='M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z', clipRule='evenodd')
                                            ], className='icon text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                            dbc.Input(type='file'),
                                            html.Div([
                                                html.Div("Choose Image", className='fw-normal text-dark mb-1'),
                                                html.Div("JPG, GIF or PNG. Max size of 800K", className='text-gray small')
                                            ], className='d-md-block text-left')
                                        ], className='d-flex')
                                    ], className='d-flex justify-content-xl-center ms-xl-3')
                                ], className='file-field')
                            ], className='d-flex align-items-center')
                        ], className='card card-body border-0 shadow')
                    ], className='col-12')
                ], className='row')
            ], className='col-12 col-xl-4')
        ], className='row'),
        html.Div([
            html.Div([
                dbc.Button(type='button', className='btn-close theme-settings-close', href='#theme-settings'),
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
                        html.Img(src='../assets/img/technologies/bootstrap-5-logo.svg', className='image image-xs')
                    ], className='me-3', href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard', target='_blank'),
                    html.A([
                        html.Img(src='../assets/img/technologies/react-logo.svg', className='image image-xs')
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
