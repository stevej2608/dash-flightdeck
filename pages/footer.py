from dash import html

def Footer():
    return html.Footer([
        html.Span([
            'Copyright © 2019-2020 ',
            html.A('Themesberg', href='https://themesberg.com')
        ]),
        html.Ul([
            html.Li([
                html.A('Privacy Policy', className='nav-link text-secondary')
            ], className='nav-item'),
            html.Li([
                html.A('Terms and conditions', className='nav-link text-secondary', href='#')
            ], className='nav-item'),
            html.Li([
                html.A('Contact', className='nav-link text-secondary', href='#')
            ], className='nav-item')
        ], className='nav m-0')
    ], className='pt-5 d-flex justify-content-between')

