from dash import html, dcc
from icons.hero import LIGHTENING_ICON, CHART_PIE_ICON, VIEW_GRID_ICON, CALENDER_ICON, ARROW_ICON, TABLE_ICON, FIRE_ICON

from .mobile_nav import mobileSidebarHeader
from components.sidebar_aoi import DropdownAIO, dropdownEntry

def _sidebarLink(text, icon, href, active="", hyperlink=False):
    Element = html.A if hyperlink else dcc.Link
    return  html.Li([
        Element([
            html.Span([
                icon
            ], className='sidebar-icon'),
            html.Span(text, className='mt-1 ms-1 sidebar-text')
        ], href=href, className='nav-link d-flex align-items-center')
    ], className=f'nav-item {active}')


def _sidebarButtonLink(text, icon, href, active=""):
    return  html.Li([
        dcc.Link([
            html.Span([
                icon
            ], className='sidebar-icon d-inline-flex align-items-center justify-content-center'),
            html.Span(text)
        ], href=href, className='btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro')
    ], className=f'nav-item {active}')


def _sidebarDropdown(text, icon, children):
    return html.Li([

        # Dropdown button

        html.Span([
            html.Span([
                html.Span([
                    icon
                ], className='sidebar-icon'),
                html.Span(text, className='sidebar-text')
            ]),
            html.Span([
                ARROW_ICON
            ], className='link-arrow')
        ], className='nav-link collapsed d-flex justify-content-between align-items-center', **{"data-bs-toggle": "collapse", "data-bs-target": "#submenu-pages"}),

        # Drop down content - example page links

        html.Div([
            html.Ul(children, className='flex-column nav')
        ], className='multi-level collapse', role='list', id='submenu-pages', **{"aria-expanded": "false"})
    ], className='nav-item')


def sideBar():
    return html.Nav([
        html.Div([

            mobileSidebarHeader(),

            # Sidebar List of entries

            html.Ul([
                _sidebarLink("Volt Overview", LIGHTENING_ICON, 'https://demo.themesberg.com/volt/pages/dashboard/dashboard.html', hyperlink=True),
                _sidebarLink("Dashboard", CHART_PIE_ICON, '/pages/dashboard.html'),
                _sidebarLink("Settings", VIEW_GRID_ICON, '/pages/settings.html'),
                _sidebarLink("Calendar", CALENDER_ICON, 'https://demo.themesberg.com/volt-pro/pages/calendar.html'),

                # Page examples drop down

                DropdownAIO([
                    dropdownEntry("Sign In", '/pages/sign-in.html'),
                    dropdownEntry("Sign Up", '/pages/sign-up.html'),
                    dropdownEntry("Forgot password", '/pages/forgot-password.html'),
                    dropdownEntry("Reset password", '/pages/reset-password.html'),
                    dropdownEntry("Lock", '/pages/lock.html'),
                    dropdownEntry("404 Not Found", '/pages/???.html'),
                    dropdownEntry("500 Not Found", '/pages/500.html'),
                ], "Page examples", TABLE_ICON),

                # Bottom Item

                _sidebarButtonLink("Upgrade to Pro", FIRE_ICON, '../pages/upgrade-to-pro.html')

            ], className='nav flex-column pt-3 pt-md-0')
        ], className='sidebar-inner px-4 pt-3')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse', **{"data-simplebar": ""})
