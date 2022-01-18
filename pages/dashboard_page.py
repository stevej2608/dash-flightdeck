from dash import html, dcc, register_page
from dash_svg import Svg, Path

from .components import sideBar, mobileNavBar, topNavBar, footer
from .components import buttonBar, newTasksButton

from .dashboard import salesChart, customers, revenue, bounceRate, pageVisitsTable, teamMembers, progressTrack, totalOrders, rankingPanel, acquisition

register_page(__name__, path="/dashboard", title="Dash/Flightdeck - Dashboard")

layout = html.Div([
    mobileNavBar(),
    sideBar(),
    html.Main([

        topNavBar(),
        buttonBar(
            lhs=newTasksButton()
        ),

        html.Div([
            salesChart(),
            customers(),
            revenue(),
            bounceRate()
        ], className='row'),

        html.Div([
            html.Div([
                html.Div([
                    pageVisitsTable(),
                    teamMembers(),
                    progressTrack()
                ], className='row')
            ], className='col-12 col-xl-8'),

            # Total orders, # Global Rank, Acquisition column

            html.Div([
                totalOrders(),
                rankingPanel(),
                acquisition(),
            ], className='col-12 col-xl-4')

        ], className='row'),

        #

        footer()

    ], className='content')

])
