from dash import html
from dash_svg import Svg, Path

def teamMembers():
    return html.Div([
        html.Div([
            html.Div([
                html.H2("Team members", className='fs-5 fw-bold mb-0'),
                html.A("See all", href='#', className='btn btn-sm btn-primary')
            ], className='card-header border-bottom d-flex align-items-center justify-content-between'),
            html.Div([
                html.Ul([
                    html.Li([
                        html.Div([
                            html.Div([
                                # Avatar
                                html.A([
                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-1.jpg')
                                ], href='#', className='avatar')
                            ], className='col-auto'),
                            html.Div([
                                html.H4([
                                    html.A("Chris Wood", href='#')
                                ], className='h6 mb-0'),
                                html.Div([
                                    html.Div(className='bg-success dot rounded-circle me-1'),
                                    html.Small("Online")
                                ], className='d-flex align-items-center')
                            ], className='col-auto ms--2'),
                            html.Div([
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z', clipRule='evenodd')
                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Invite"
                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                            ], className='col text-end')
                        ], className='row align-items-center')
                    ], className='list-group-item px-0'),
                    html.Li([
                        html.Div([
                            html.Div([
                                # Avatar
                                html.A([
                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-2.jpg')
                                ], href='#', className='avatar')
                            ], className='col-auto'),
                            html.Div([
                                html.H4([
                                    html.A("Jose Leos", href='#')
                                ], className='h6 mb-0'),
                                html.Div([
                                    html.Div(className='bg-warning dot rounded-circle me-1'),
                                    html.Small("In a meeting")
                                ], className='d-flex align-items-center')
                            ], className='col-auto ms--2'),
                            html.Div([
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Message"
                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                            ], className='col text-end')
                        ], className='row align-items-center')
                    ], className='list-group-item px-0'),
                    html.Li([
                        html.Div([
                            html.Div([
                                # Avatar
                                html.A([
                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-3.jpg')
                                ], href='#', className='avatar')
                            ], className='col-auto'),
                            html.Div([
                                html.H4([
                                    html.A("Bonnie Green", href='#')
                                ], className='h6 mb-0'),
                                html.Div([
                                    html.Div(className='bg-danger dot rounded-circle me-1'),
                                    html.Small("Offline")
                                ], className='d-flex align-items-center')
                            ], className='col-auto ms--2'),
                            html.Div([
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Message"
                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                            ], className='col text-end')
                        ], className='row align-items-center')
                    ], className='list-group-item px-0'),
                    html.Li([
                        html.Div([
                            html.Div([
                                # Avatar
                                html.A([
                                    html.Img(className='rounded', alt='Image placeholder', src='../../assets/img/team/profile-picture-4.jpg')
                                ], href='#', className='avatar')
                            ], className='col-auto'),
                            html.Div([
                                html.H4([
                                    html.A("Neil Sims", href='#')
                                ], className='h6 mb-0'),
                                html.Div([
                                    html.Div(className='bg-danger dot rounded-circle me-1'),
                                    html.Small("Offline")
                                ], className='d-flex align-items-center')
                            ], className='col-auto ms--2'),
                            html.Div([
                                html.A([
                                    Svg([
                                        Path(fillRule='evenodd', d='M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z', clipRule='evenodd')
                                    ], className='icon icon-xxs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                                    "Message"
                                ], href='#', className='btn btn-sm btn-secondary d-inline-flex align-items-center')
                            ], className='col text-end')
                        ], className='row align-items-center')
                    ], className='list-group-item px-0')
                ], className='list-group list-group-flush list my--3')
            ], className='card-body')
        ], className='card border-0 shadow')


    ], className='col-12 col-xxl-6 mb-4')

