from dash import html

from ..components.dropdown_button import DropdownButton, dropdownLink
from ..icons.hero import ICON

def newButton():
    return DropdownButton([
        dropdownLink("Document", ICON.DOCUMENT),
        dropdownLink("Message", ICON.MESSAGE.ME2),
        dropdownLink("Product", ICON.UPLOAD),
        dropdownLink("My Plan", ICON.FIRE.ME2_DANGER),
    ], "New")

def calenderButton():
    return  html.Button([
        ICON.CALENDER
    ], type='button', className='btn btn-gray-800 d-inline-flex align-items-center me-2')
