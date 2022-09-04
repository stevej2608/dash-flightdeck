from dash import html

from ..components.dropdown_button import DropdownButton, dropdownLink
from ..icons.hero import ICON

def reportsDropdown():
    return DropdownButton([
        dropdownLink("Products", ICON.PRODUCTS,href='#'),
        dropdownLink("Customers", ICON.CUSTOMERS, href='#'),
        dropdownLink("Orders", ICON.ORDERS, href='#'),
        dropdownLink("Console", ICON.CONSOLE, href='#'),
        html.Div(role='separator', className='dropdown-divider my-1'),
        dropdownLink("All Reports", ICON.ALL_REPORTS, href='#')
    ], "Reports", buttonIcon=ICON.CLIPBOARD, buttonColor="gray-800", downArrow=True)
