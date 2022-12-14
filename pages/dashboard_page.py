from dash import html
from dash_spa import register_page

from .common import topNavBar, footer, buttonBar
from .dashboard import salesChart, customers, revenue, bounceRate, pageVisitsTable, teamMembers, progressTrack, totalOrdersBarChart, rankingPanel, acquisition, newTasksButton

register_page(__name__, path="/pages/dashboard", title="Dash/Flightdeck - Dashboard")

layout = html.Main([
        topNavBar(),
        buttonBar(
            newTasksButton()
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
            html.Div([
                totalOrdersBarChart(),
                rankingPanel(),
                acquisition(),
            ], className='col-12 col-xl-4')

        ], className='row'),
        footer()
    ], className='content')

