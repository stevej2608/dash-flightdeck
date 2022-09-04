from dash_spa.components.dropdown_button_aoi import DropdownButtonAIO, dropdownLink

class DropdownButton(DropdownButtonAIO):

    container_className = 'dropdown-menu dashboard-dropdown dropdown-menu-start mt-2 py-1'

    def button_className(self, buttonColor):
        return f'btn btn-{buttonColor} d-inline-flex align-items-center me-2 dropdown-toggle'