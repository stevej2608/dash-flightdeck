from dash import html
from ...icons import ICON

def notification():

    MODAL_ID = 'modal-notification'
    BTN_DATA = {"data-bs-toggle": "modal", "data-bs-target": f"#{MODAL_ID}"}
    DISMISS = {"data-bs-dismiss": "modal"}

    return html.Div([
        # Button Modal
        html.Button("Notification", type='button', className='btn btn-block btn-gray-800 mb-3', **BTN_DATA),
        # Modal Content
        html.Div([
            html.Div([
                html.Div([
                    html.Button(type='button', className='btn-close theme-settings-close fs-6 ms-auto', **DISMISS),
                    html.Div([
                        html.P("A new experience, personalized for you.", className='modal-title text-gray-200', id='modal-title-notification')
                    ], className='modal-header'),
                    html.Div([
                        html.Div([
                            html.Span(ICON.INBOX_IN, className='modal-icon'),
                            html.H2("Important message!", className='h4 modal-title my-3'),
                            html.P("Do you know that you can assign status and relation to a company right in the visit list?")
                        ], className='py-3 text-center')
                    ], className='modal-body text-white'),
                    html.Div([
                        html.Button("Go to Inbox", type='button', className='btn btn-sm btn-white', **DISMISS)
                    ], className='modal-footer')
                ], className='modal-content bg-gradient-secondary')
            ], className='modal-dialog modal-info modal-dialog-centered', role='document')
        ], className='modal fade', id=MODAL_ID, role='dialog'),
        # End of Modal Content
    ], className='col-lg-4')
