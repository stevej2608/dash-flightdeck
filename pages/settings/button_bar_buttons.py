from dash import html

from pages.components import dropdownButton, dropdownLink
from pages.components.hero_icons import DOCUMENT_ICON, MESSAGE_ICON, UPLOAD_ICON, FIRE_ICON_DANGER, CALENDER_ICON

def newButton():
    return dropdownButton([
        dropdownLink("Document", DOCUMENT_ICON),
        dropdownLink("Message", MESSAGE_ICON),
        dropdownLink("Product", UPLOAD_ICON),
        dropdownLink("My Plan", FIRE_ICON_DANGER),
    ], "New")

def calenderButton():
    return  html.Button([
        CALENDER_ICON
    ], type='button', className='btn btn-gray-800 d-inline-flex align-items-center me-2')
