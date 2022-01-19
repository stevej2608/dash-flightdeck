
from dash import html, dcc
from dash_svg import Svg, Path

def clipBoard():
    return Svg([
        Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
        Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def downArrow():
    return  Svg([
        Path(fillRule='evenodd', d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z', clipRule='evenodd')
    ], className='icon icon-xs ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')



def productsIcon():
    return  Svg([
        Path(d='M4 3a2 2 0 100 4h12a2 2 0 100-4H4z'),
        Path(fillRule='evenodd', d='M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z', clipRule='evenodd')
    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def customersIcon():
    return  Svg([
        Path(d='M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z')
    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def ordersIcon():
    return  Svg([
        Path(fillRule='evenodd', d='M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z', clipRule='evenodd')
    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def consoleIcon():
    return  Svg([
        Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z', clipRule='evenodd')
    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def allReportsIcon():
    return  Svg([
        Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
        Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
    ], className='dropdown-icon text-gray-400 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def dropdownLink(icon, text, href):
    return html.A([
        icon(),
        text
    ], className='dropdown-item d-flex align-items-center', href=href)


def reportsDropdown():

    button = html.Button([
        clipBoard(),
        "Reports",
        downArrow()
        ], className='btn btn-gray-800 d-inline-flex align-items-center dropdown-toggle', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"})

    dropdown = html.Div([
        dropdownLink(productsIcon, "Products", href='#'),
        dropdownLink(customersIcon,"Customers", href='#'),
        dropdownLink(ordersIcon, "Orders", href='#'),
        dropdownLink(consoleIcon, "Console", href='#'),
        html.Div(role='separator', className='dropdown-divider my-1'),
        dropdownLink(allReportsIcon, "All Reports", href='#')
    ], className='dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1')

    return [button, dropdown]
