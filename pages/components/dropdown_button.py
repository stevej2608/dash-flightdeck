from dash import html
from dash_svg import Svg, Path

def plusIcon():
    return Svg([
        Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M12 6v6m0 0v6m0-6h6m-6 0H6')
    ], className='icon icon-xs me-2', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg')


def dropdownLink(title, icon, href='#'):
    return html.A([
        icon(),
        title
    ], className='dropdown-item d-flex align-items-center', href=href)


def dropdownButton(dropdownEntries, buttonText, buttonIcon=plusIcon, buttonColor='secondary'):
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
