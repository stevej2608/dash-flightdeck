from dash import html
from app import create_app
from server import serve_app
from components.dropdown_aio import DropdownAIO
from icons.hero import TICK_ICON, GEAR_ICON


def settingsDropdown():

    button = DropdownAIO.Button([
       GEAR_ICON,html.Span("Toggle Dropdown", className='visually-hidden')
    ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-1')

    container =  html.Div([
        html.Span("Show", className='small ps-3 fw-bold text-dark'),
        html.Div(["10", TICK_ICON], className='dropdown-item d-flex align-items-center fw-bold'),
        html.Div("20", className='dropdown-item fw-bold'),
        html.Div("30", className='dropdown-item fw-bold rounded-bottom')
    ], className='dropdown-menu dropdown-menu-xs dropdown-menu-end pb-0')

    dropdown = DropdownAIO(button, container)

    return html.Div(dropdown, className='col-4 col-md-2 col-xl-1 ps-md-0 text-end')


def layout():
    dropdown = settingsDropdown()
    return html.Div([dropdown])


if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
