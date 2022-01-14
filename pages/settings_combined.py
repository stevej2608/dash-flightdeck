from dash import html, dcc, register_page
from dash_svg import Svg, Path

from .sidebar import sideBar
from .mobile_nav import mobileNavBar
from .top_navbar import topNavBar
from .button_bar import buttonBar
from .profile_cards import card1, card2, card3

register_page(__name__, path="/volt", title="Volt Clone")

def layout():
    return  html.Div([

    mobileNavBar(),
    sideBar(),

    html.Main([
        topNavBar(),
        buttonBar(),

        # Main panel

        html.Div([

            # Left column

            html.Div([

                # General Form

                html.Div([
                    html.H2("General information", className='h5 mb-4'),
                    html.Form([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("First Name", htmlFor='first_name'),
                                    dcc.Input(className='form-control', id='first_name', type='text', placeholder='Enter your first name', required='')
                                ])
                            ], className='col-md-6 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Last Name", htmlFor='last_name'),
                                    dcc.Input(className='form-control', id='last_name', type='text', placeholder='Also your last name', required='')
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
                                    dcc.Input(className='form-control', id='birthday', type='text', placeholder='dd/mm/yyyy', required='')
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
                                    dcc.Input(className='form-control', id='email', type='email', placeholder='name@company.com', required='')
                                ], className='form-group')
                            ], className='col-md-6 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Phone", htmlFor='phone'),
                                    dcc.Input(className='form-control', id='phone', type='number', placeholder='+12-345 678 910', required='')
                                ], className='form-group')
                            ], className='col-md-6 mb-3')
                        ], className='row'),
                        html.H2("Location", className='h5 my-4'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("Address", htmlFor='address'),
                                    dcc.Input(className='form-control', id='address', type='text', placeholder='Enter your home address', required='')
                                ], className='form-group')
                            ], className='col-sm-9 mb-3'),
                            html.Div([
                                html.Div([
                                    html.Label("Number", htmlFor='number'),
                                    dcc.Input(className='form-control', id='number', type='number', placeholder='No.', required='')
                                ], className='form-group')
                            ], className='col-sm-3 mb-3')
                        ], className='row'),
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Label("City", htmlFor='city'),
                                    dcc.Input(className='form-control', id='city', type='text', placeholder='City', required='')
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
                                    dcc.Input(className='form-control', id='zip', type='tel', placeholder='ZIP', required='')
                                ], className='form-group')
                            ], className='col-sm-4')
                        ], className='row'),
                        html.Div([
                            html.Button("Save all", className='btn btn-gray-800 mt-2 animate-up-2', type='submit')
                        ], className='mt-3')
                    ])
                ], className='card card-body border-0 shadow mb-4'),

                # Alerts & Notifications

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
                                    dcc.Input(className='form-check-input', type='checkbox', id='user-notification-1'),
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
                                    dcc.Input(className='form-check-input', type='checkbox', id='user-notification-2', value=False),
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
                                    dcc.Input(className='form-check-input', type='checkbox', id='user-notification-3', value=False),
                                    html.Label(className='form-check-label', htmlFor='user-notification-3')
                                ], className='form-check form-switch')
                            ])
                        ], className='list-group-item d-flex align-items-center justify-content-between px-0')
                    ], className='list-group list-group-flush')
                ], className='card card-body border-0 shadow mb-4 mb-xl-0')

            ], className='col-12 col-xl-8'),

            # Right column

            html.Div([
                html.Div([
                    card1(),
                    card2(),
                    card3(),
                ], className='row')
            ], className='col-12 col-xl-4')


        ], className='row'),

        # Settings panel pop-up

        html.Div([
            html.Div([
                html.Button(type='button', className='btn-close theme-settings-close'),
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

        # Settings button (bottom right)

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

        # Footer

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
