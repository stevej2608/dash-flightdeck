from dash import html

def dropdownLink(title, icon, href='#'):
    return html.A([
        icon(),
        title
    ], className='dropdown-item d-flex align-items-center', href=href)


def dropdownButton(dropdownEntries, buttonText, buttonIcon, buttonColor='secondary'):
    return  html.Div([
        html.Div([
            html.Button([
                buttonIcon(),
                buttonText
            ], className=f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle',
            **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
            html.Div(dropdownEntries, className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')
        ], className='dropdown')
    ])
