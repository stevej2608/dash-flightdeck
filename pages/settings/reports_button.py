from dash import html

from pages.components import dropdownButton, dropdownLink
from pages.components.hero_icons import CLIPBOARD_ICON, PRODUCTS_ICON, CUSTOMERS_ICON, ORDERS_ICON, CONSOLE_ICON, ALL_REPORTS_ICON

def reportsDropdown():
    return dropdownButton([
        dropdownLink("Products", PRODUCTS_ICON,href='#'),
        dropdownLink("Customers", CUSTOMERS_ICON, href='#'),
        dropdownLink("Orders", ORDERS_ICON, href='#'),
        dropdownLink("Console", CONSOLE_ICON, href='#'),
        html.Div(role='separator', className='dropdown-divider my-1'),
        dropdownLink("All Reports", ALL_REPORTS_ICON, href='#')
    ], "Reports", buttonIcon=CLIPBOARD_ICON, buttonColor="gray-800", downArrow=True)
