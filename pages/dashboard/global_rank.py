from dash import html
from pages.components.hero_icons import EARTH_ICON, COUNTRY_ICON, CATEGORY_ICON, ICON1_ICON, ICON2_ICON, ICON3_ICON, UP_ICON

def _categoryRank(category, categoryIcon, rank, rankIcon):
    return html.Div([
        html.Div([
            html.Div([
                categoryIcon,
                category
            ], className='h6 mb-0 d-flex align-items-center')
        ]),
        html.Div([
            html.A([
                rank,
                rankIcon
            ], href='#', className='d-flex align-items-center fw-bold')
        ])
    ], className='d-flex align-items-center justify-content-between border-bottom pb-3')

def _categoryRankExt(category, categoryIcon, rank, notes, upDownIcon, rankIcon):
    return html.Div([
        html.Div([
            html.Div([
                categoryIcon,
                category
            ], className='h6 mb-0 d-flex align-items-center'),
            html.Div([
                notes,
                upDownIcon
            ], className='small card-stats')
        ]),
        html.Div([
            html.A([
                rank,
                rankIcon
            ], href='#', className='d-flex align-items-center fw-bold'),
        ])
    ], className='d-flex align-items-center justify-content-between border-bottom pb-3')


def rankingPanel():
    return html.Div([
        html.Div([
            html.Div([
                _categoryRank("Global Rank", EARTH_ICON, '#755', ICON1_ICON),
                _categoryRankExt("Country Rank", COUNTRY_ICON, '#32', "United States", UP_ICON, ICON2_ICON),
                _categoryRankExt("Category Rank", CATEGORY_ICON, '#11', "Computers Electronics > Technology", UP_ICON, ICON3_ICON),
           ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 px-0 mb-4')
