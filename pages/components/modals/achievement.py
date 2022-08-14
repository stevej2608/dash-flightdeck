
from dash import html
from ...icons import ICON

def achievement():
    MODAL_ID = 'modal-achievement'
    BTN_DATA = {"data-bs-toggle": "modal", "data-bs-target": f"#{MODAL_ID}"}
    DISMISS = {"data-bs-dismiss": "modal"}
    return  html.Div([
        # Button Modal
        html.Button("Achievement", type='button', className='btn btn-block btn-gray-800 mb-3', **BTN_DATA),
        # Modal Content
        html.Div([
            html.Div([
                html.Div([
                    html.Button(type='button', className='btn-close theme-settings-close fs-6 ms-auto', **DISMISS),
                    html.Div([
                        html.P("You just unlocked a new badge", className='lead mb-0 text-white')
                    ], className='modal-header mx-auto'),
                    html.Div([
                        html.Div([
                            html.Span(ICON.FIRE.LG, className='modal-icon display-1 text-white'),
                            html.H2("Author Level 5", className='h3 modal-title mb-3 text-white'),
                            html.P("One Thousand Dollars! Well done mate - heads are turning your way.", className='mb-4 text-white'),
                            html.Div([
                                html.Div(className='progress-bar bg-secondary', role='progressbar', style={'width': '50%'})
                            ], className='progress mb-0')
                        ], className='py-3 px-5 text-center')
                    ], className='modal-body pt-0'),
                    html.Div([
                        html.Button("Awesome!", type='button', className='btn btn-sm btn-white text-tertiary', **DISMISS)
                    ], className='modal-footer d-flex justify-content-center pt-0 pb-3')
                ], className='modal-content')
            ], className='modal-dialog modal-tertiary modal-dialog-centered', role='document')
        ], className='modal fade', id=MODAL_ID, role='dialog'),
        # End of Modal Content
    ], className='col-lg-4')
