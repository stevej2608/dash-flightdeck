from dash import html, dcc, register_page
from dash_svg import Svg, Path

from .sidebar import sideBar
from .mobile_nav import mobileNavBar
from .top_navbar import topNavBar
from .button_bar import buttonBar
from .profile_cards import card1, card2, card3
from .general_form import generalForm
from .alerts_notifications import alertsNotifications
from .settings_popup import settingsPopupButton, settingsPopupPanel
from .footer import footer

register_page(__name__, path="/volt", title="Volt Clone")

def layout():
    return  html.Div([

    mobileNavBar(),
    sideBar(),

    html.Main([
        topNavBar(),
        buttonBar(),
        html.Div([
            html.Div([
                generalForm(),
                alertsNotifications()
            ], className='col-12 col-xl-8'),
            html.Div([
                html.Div([
                    card1(),
                    card2(),
                    card3(),
                ], className='row')
            ], className='col-12 col-xl-4')
        ], className='row'),

        settingsPopupPanel(),
        settingsPopupButton(),
        footer()
    ], className='content')
])
