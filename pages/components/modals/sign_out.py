from dash import html, dcc
from ...icons import ICON, FACEBOOK, TWITTER, GITHUB

def sign_out():
    return html.Div([
        # Button Modal
        html.Button("Sign Up", type='button', className='btn btn-block btn-gray-800 mb-3'),
        # Modal Content
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Button(type='button', className='btn-close ms-auto'),
                            html.Div([
                                html.H1("Create Account", className='mb-0 h4')
                            ], className='text-center text-md-center mb-4 mt-md-0'),
                            html.Form([
                                # Form
                                html.Div([
                                    html.Label("Your Email", htmlFor='email'),
                                    html.Div([
                                        html.Span(ICON.MAIL, className='input-group-text', id='basic-addon1'),
                                        dcc.Input(type='email', className='form-control', placeholder='example@company.com', id='email', required='')
                                    ], className='input-group')
                                ], className='form-group mb-4'),
                                # End of Form
                                html.Div([
                                    # Form
                                    html.Div([
                                        html.Label("Your Password", htmlFor='password'),
                                        html.Div([
                                            html.Span(ICON.LOCK_CLOSED, className='input-group-text', id='basic-addon2'),
                                            dcc.Input(type='password', placeholder='Password', className='form-control', id='password', required='')
                                        ], className='input-group')
                                    ], className='form-group mb-4'),
                                    # End of Form
                                    # Form
                                    html.Div([
                                        html.Label("Confirm Password", htmlFor='confirm_password'),
                                        html.Div([
                                            html.Span(ICON.LOCK_CLOSED, className='input-group-text', id='basic-addon2'),
                                            dcc.Input(type='password', placeholder='Confirm Password', className='form-control', id='confirm_password', required='')
                                        ], className='input-group')
                                    ], className='form-group mb-4'),
                                    # End of Form
                                    html.Div([
                                        html.Div([
                                            dcc.Input(className='form-check-input', type='checkbox', value='', id='remember'),
                                            html.Label([
                                                "I agree to the",
                                                html.A("terms and conditions", href='#', className='fw-bold')
                                            ], className='form-check-label fw-normal mb-0', htmlFor='remember')
                                        ], className='form-check')
                                    ], className='mb-4')
                                ], className='form-group'),
                                html.Div([
                                    html.Button("Sign up", type='submit', className='btn btn-gray-800')
                                ], className='d-grid')
                            ], action='#', className='mt-4'),
                            html.Div([
                                html.Span("or login with", className='fw-normal')
                            ], className='mt-3 mb-4 text-center'),
                            html.Div([
                                html.A(FACEBOOK.XXS, href='#', className='btn btn-icon-only btn-pill btn-outline-gray-500 me-2', title='facebook button'),
                                html.A(TWITTER.XXS, href='#', className='btn btn-icon-only btn-pill btn-outline-gray-500 me-2', title='twitter button'),
                                html.A(GITHUB.XXS, href='#', className='btn btn-icon-only btn-pill btn-outline-gray-500', title='github button')
                            ], className='d-flex justify-content-center my-3'),
                            html.Div([
                                html.Span([
                                    "Already have an account?",
                                    html.A("Login here", href='./sign-in', className='fw-bold')
                                ], className='fw-normal')
                            ], className='d-flex justify-content-center align-items-center mt-4')
                        ], className='card p-3 p-lg-4')
                    ], className='modal-body p-0')
                ], className='modal-content')
            ], className='modal-dialog modal-dialog-centered', role='document')
        ], className='modal fade', id='modal-form-signup', role='dialog'),
        # End of Modal Content
    ], className='col-lg-4')

