from dash import html, register_page

from .components import sideBar, mobileNavBar, topNavBar, buttonBar, footer
from .settings import card1, card2, card3, generalForm, alertsNotifications


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

        # settingsPopupPanel(),
        # settingsPopupButton(),
        footer()
    ], className='content')
])
