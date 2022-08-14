from dash import html, dcc
from ...icons import ICON

def subscribe():
    return html.Div([
        # Button Modal
        html.Button("Subscribe", type='button', className='btn btn-block btn-gray-800 mb-3'),
        # Modal Content
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Button(type='button', className='btn-close btn-close-white text-white')
                    ], className='modal-header'),
                    html.Div([
                        html.Span(ICON.MAIL_OPEN, className='modal-icon'),
                        html.H3("Join our 1,360,462 subscribers", className='modal-title mb-3'),
                        html.P("Get exclusive access to freebies, premium products and news.", className='mb-4 lead'),
                        html.Div([
                            html.Div([
                                dcc.Input(type='text', id='subscribe', className='me-sm-1 mb-sm-0 form-control form-control-lg', placeholder='example@company.com'),
                                html.Div([
                                    html.Button("Subscribe", type='submit', className='ms-2 btn large-form-btn btn-secondary')
                                ])
                            ], className='d-flex mb-3 justify-content-center')
                        ], className='form-group px-lg-5')
                    ], className='modal-body text-center py-3'),
                    html.Div([
                        html.P([
                            "We’ll never share your details with third parties.",
                            html.Br(className='visible-md'),
                            "View our",
                            html.A("Privacy Policy", href='#'),
                            "for more info."
                        ], className='text-white font-small')
                    ], className='modal-footer z-2 mx-auto text-center')
                ], className='modal-content bg-dark text-white')
            ], className='modal-dialog modal-tertiary modal-dialog-centered modal-lg', role='document')
        ], className='modal fade', id='modal-subscribe', role='dialog'),
        # End of Modal Content
    ], className='col-lg-4')
