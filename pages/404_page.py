layout = html.Body([
    # NOTICE: You can use the _analytics.html partial to include production code specific code & trackers
    html.Main([
        html.Section([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Img(className='img-fluid w-75', src='../../assets/img/illustrations/404.svg', alt='404 not found'),
                            html.H1([
                                "Page not",
                                html.Span("found", className='fw-bolder text-primary')
                            ], className='mt-5'),
                            html.P("Oops! Looks like you followed a bad link. If you think this is a problem with us,
                please tell us.", className='lead my-4'),
                            html.A([
                                html.Svg([
                                    html.Path(fillRule='evenodd', d='M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z', clipRule='evenodd')
                                ], className='icon icon-xs me-2', fill='currentColor', viewbox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                "Back to homepage"
                            ], href='../dashboard/dashboard-min.html', className='btn btn-gray-800 d-inline-flex align-items-center justify-content-center mb-4')
                        ])
                    ], className='col-12 text-center d-flex align-items-center justify-content-center')
                ], className='row')
            ], className='container')
        ], className='vh-100 d-flex align-items-center justify-content-center')
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
