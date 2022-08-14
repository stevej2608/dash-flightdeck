from dash import html

def default():
    return  html.Div([
        # Button Modal
        html.Button("Default", type='button', className='btn btn-block btn-gray-800 mb-3'),
        # Modal Content
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H2("Terms of Service", className='h6 modal-title'),
                        html.Button(type='button', className='btn-close')
                    ], className='modal-header'),
                    html.Div([
                        html.P("With less than a month to go before the European Union enacts new consumer privacy laws for its citizens, companies around the world are updating their terms of service agreements to comply."),
                        html.P("The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant to ensure a common set of data rights in the European Union. It requires organizations to notify users as soon as possible of high-risk data breaches that could personally affect them.")
                    ], className='modal-body'),
                    html.Div([
                        html.Button("Accept", type='button', className='btn btn-secondary'),
                        html.Button("Close", type='button', className='btn btn-link text-gray-600 ms-auto')
                    ], className='modal-footer')
                ], className='modal-content')
            ], className='modal-dialog modal-dialog-centered', role='document')
        ], className='modal fade', id='modal-default', role='dialog'),
        # End of Modal Content
    ], className='col-lg-4')
