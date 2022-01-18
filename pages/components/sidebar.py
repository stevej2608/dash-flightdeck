from dash import html, dcc
from dash_svg import Svg, Path

from .mobile_nav import mobileSidebarHeader

def lightening_icon():
    return html.Img(src='../assets/img/brand/light.svg', height='20', width='20', alt='Volt Logo')

def clock_icon():
    return  Svg([
        Path(d='M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z'),
        Path(d='M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def settings_icon():
    return Svg([
        Path(d='M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def calenderIcon():
    return Svg([
        Path(fillRule='evenodd', d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z", clipRule='evenodd')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def pageIcon():
    return Svg([
        Path(fillRule='evenodd', d='M5 4a3 3 0 00-3 3v6a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H5zm-1 9v-1h5v2H5a1 1 0 01-1-1zm7 1h4a1 1 0 001-1v-1h-5v2zm0-4h5V8h-5v2zM9 8H4v2h5V8z', clipRule='evenodd')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def arrowIcon():
    return Svg([
        Path(fillRule='evenodd', d='M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', clipRule='evenodd')
    ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def fireIcon():
    return Svg([
        Path(fillRule='evenodd', d='M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z', clipRule='evenodd')
    ], className='icon icon-xs me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def crossIcon():
    return  Svg([
        Path(fillRule='evenodd', d='M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z', clipRule='evenodd')
    ], className='icon icon-xs', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def signoutIcon():
    return  Svg([
        Path(strokeLinecap='round', strokeLinejoin='round', strokeWidth='2', d='M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1')
    ], className='icon icon-xxs me-1', fill='none', stroke='currentColor', viewBox='0 0 24 24', xmlns='http://www.w3.org/2000/svg'),


def sidebarLink(text, icon, href, active=""):
    return  html.Li([
        dcc.Link([
            html.Span([
                icon()
            ], className='sidebar-icon'),
            html.Span(text, className='mt-1 ms-1 sidebar-text')
        ], href=href, className='nav-link d-flex align-items-center')
    ], className=f'nav-item {active}')


def sidebarButtonLink(text, icon, href, active=""):
    return  html.Li([
        html.A([
            html.Span([
                icon()
            ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
            html.Span(text)
        ], href=href, className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
    ], className=f'nav-item {active}')


def sidebarDropdown(text, icon, children):
    return html.Li([

        # Dropdown button

        html.Span([
            html.Span([
                html.Span([
                    icon()
                ], className='sidebar-icon'),
                html.Span(text, className='sidebar-text')
            ]),
            html.Span([
                arrowIcon()
            ], className='link-arrow')
        ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-pages"}),

        # Drop down content - example page links

        html.Div([
            html.Ul(children, className='flex-column nav')
        ], className='multi-level collapse', role='list', id='submenu-pages', **{"aria-expanded": "false"})
    ], className='nav-item')


def dropdownEntry(text, href):
    return html.Li([
        html.A([
            html.Span(text, className='sidebar-text')
        ], className='nav-link', href=href)
    ], className='nav-item')


def sideBar():
    return html.Nav([
        html.Div([

            mobileSidebarHeader(),

         # Sidebar List of entries

            html.Ul([
                sidebarLink("Volt Overview", lightening_icon, 'https://demo.themesberg.com/volt/pages/dashboard/dashboard.html'),
                sidebarLink("Dashboard", clock_icon, '/dashboard'),
                sidebarLink("Settings", settings_icon, '/settings'),
                sidebarLink("Calendar", calenderIcon, 'https://demo.themesberg.com/volt-pro/pages/calendar.html'),

                # Page examples drop down

                sidebarDropdown("Page examples", pageIcon, [
                    dropdownEntry("Sign In", '../pages/examples/sign-in.html'),
                    dropdownEntry("Sign Up", '../pages/examples/sign-up.html'),
                    dropdownEntry("Forgot password", '../pages/examples/forgot-password.html'),
                    dropdownEntry("Reset password", '../pages/examples/reset-password.html'),
                    dropdownEntry("Lock", '../pages/examples/lock.html'),
                    dropdownEntry("404 Not Found", '../pages/examples/404.html'),
                    dropdownEntry("500 Not Found", '../pages/examples/500.html'),
                ]),

                # Bottom Item

                sidebarButtonLink("Upgrade to Pro", fireIcon, '../pages/upgrade-to-pro.html')

            ], className='nav flex-column pt-3 pt-md-0')
        ], className='sidebar-inner px-4 pt-3')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse', **{"data-simplebar": ""})
