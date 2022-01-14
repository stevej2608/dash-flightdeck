from dash import html, dcc
from dash_svg import Svg, Path

def card1():
    return html.Div([
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
    ], className='col-12 mb-4')

def card2():
    return html.Div([
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
                            dcc.Input(type='file'),
                            html.Div([
                                html.Div("Choose Image", className='fw-normal text-dark mb-1'),
                                html.Div("JPG, GIF or PNG. Max size of 800K", className='text-gray small')
                            ], className='d-md-block text-left')
                        ], className='d-flex')
                    ], className='d-flex justify-content-xl-center ms-xl-3')
                ], className='file-field')
            ], className='d-flex align-items-center')
        ], className='card card-body border-0 shadow mb-4')
    ], className='col-12')


def card3():
    return html.Div([
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
                            dcc.Input(type='file'),
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

