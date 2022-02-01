from dash import html, dcc
from icons.hero import LIGHTENING_ICON, CHART_PIE_ICON, VIEW_GRID_ICON, CALENDER_ICON, TABLE_ICON, FIRE_ICON, CREDIT_CARD_ICON

from .mobile_nav import mobileSidebarHeader
from components.dropdown_folder_aoi import DropdownFolderAIO, dropdownFolderEntry

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


def sideBar():
    return html.Nav([
        html.Div([

            mobileSidebarHeader(),

            # Sidebar List of entries

            html.Ul([
                _sidebarLink("Volt Overview", LIGHTENING_ICON, 'https://demo.themesberg.com/volt/pages/dashboard/dashboard.html', hyperlink=True),
                _sidebarLink("Dashboard", CHART_PIE_ICON, '/pages/dashboard.html'),
                _sidebarLink("Tansactions", CREDIT_CARD_ICON, '/pages/transactions.html'),
                _sidebarLink("Settings", VIEW_GRID_ICON, '/pages/settings.html'),
                _sidebarLink("Calendar", CALENDER_ICON, 'https://demo.themesberg.com/volt-pro/pages/calendar.html'),

                # Page examples drop down

                DropdownFolderAIO([
                    dropdownFolderEntry("Sign In", '/pages/sign-in.html'),
                    dropdownFolderEntry("Sign Up", '/pages/sign-up.html'),
                    dropdownFolderEntry("Forgot password", '/pages/forgot-password.html'),
                    dropdownFolderEntry("Reset password", '/pages/reset-password.html'),
                    dropdownFolderEntry("Lock", '/pages/lock.html'),
                    dropdownFolderEntry("404 Not Found", '/pages/???.html'),
                    dropdownFolderEntry("500 Not Found", '/pages/500.html'),
                ], "Page examples", TABLE_ICON),

                # Bottom Item

                _sidebarButtonLink("Upgrade to Pro", FIRE_ICON, '../pages/upgrade-to-pro.html')

            ], className='nav flex-column pt-3 pt-md-0')
        ], className='sidebar-inner px-4 pt-3')
    ], id='sidebarMenu', className='sidebar d-lg-block bg-gray-800 text-white collapse', **{"data-simplebar": ""})
