layout = html.Body([
    # NOTICE: You can use the _analytics.html partial to include production code specific code & trackers
    html.Main([
        # Section
        html.Section([
            html.Div([
                html.Div([
                    html.P([
                        html.A([
                            html.Svg([
                                html.Path(fillRule='evenodd', d='M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z', clipRule='evenodd')
                            ], className='icon icon-xs me-2', fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                            "Back to log in"
                        ], href='./sign-in.html', className='d-flex align-items-center justify-content-center')
                    ], className='text-center'),
                    html.Div([
                        html.Div([
                            html.H1("Forgot your password?", className='h3'),
                            html.P("Don't fret! Just type in your email and we will send you a code to reset your password!", className='mb-4'),
                            html.Form([
                                # Form
                                html.Div([
                                    html.Label("Your Email", htmlFor='email'),
                                    html.Div([
                                        html.Input(type='email', className='form-control', id='email', placeholder='john@company.com', required='', autofocus='')
                                    ], className='input-group')
                                ], className='mb-4'),
                                # End of Form
                                html.Div([
                                    html.Button("Recover password", type='submit', className='btn btn-gray-800')
                                ], className='d-grid')
                            ], action='#')
                        ], className='signin-inner my-3 my-lg-0 bg-white shadow border-0 rounded p-4 p-lg-5 w-100 fmxw-500')
                    ], className='col-12 d-flex align-items-center justify-content-center')
                ], className='row justify-content-center form-bg-image')
            ], className='container')
        ], className='vh-lg-100 mt-5 mt-lg-0 bg-soft d-flex align-items-center')
    ]),
    # Core
    html.Script(src='../../vendor/@popperjs/core/dist/umd/popper.min.js'),
    html.Script(src='../../vendor/bootstrap/dist/js/bootstrap.min.js'),
    # Vendor JS
    html.Script(src='../../vendor/onscreen/dist/on-screen.umd.min.js'),
    # Slider
    html.Script(src='../../vendor/nouislider/distribute/nouislider.min.js'),
    # Smooth scroll
    html.Script(src='../../vendor/smooth-scroll/dist/smooth-scroll.polyfills.min.js'),
    # Charts
    html.Script(src='../../vendor/chartist/dist/chartist.min.js'),
    html.Script(src='../../vendor/chartist-plugin-tooltips/dist/chartist-plugin-tooltip.min.js'),
    # Datepicker
    html.Script(src='../../vendor/vanillajs-datepicker/dist/js/datepicker.min.js'),
    # Sweet Alerts 2
    html.Script(src='../../vendor/sweetalert2/dist/sweetalert2.all.min.js'),
    # Moment JS
    html.Script(src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.27.0/moment.min.js'),
    # Vanilla JS Datepicker
    html.Script(src='../../vendor/vanillajs-datepicker/dist/js/datepicker.min.js'),
    # Notyf
    html.Script(src='../../vendor/notyf/notyf.min.js'),
    # Simplebar
    html.Script(src='../../vendor/simplebar/dist/simplebar.min.js'),
    # Github buttons
    html.Script(async='', defer='', src='https://buttons.github.io/buttons.js'),
    # Volt JS
    html.Script(src='../../assets/js/volt.js')
])
