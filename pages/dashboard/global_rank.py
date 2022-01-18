from dash import html
from dash_svg import Svg, Path

def earthIcon():
    return Svg([
        Path(fillRule='evenodd', d='M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z', clipRule='evenodd')
    ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def countryIcon():
    return Svg([
        Path(fillRule='evenodd', d='M3 6a3 3 0 013-3h10a1 1 0 01.8 1.6L14.25 8l2.55 3.4A1 1 0 0116 13H6a1 1 0 00-1 1v3a1 1 0 11-2 0V6z', clipRule='evenodd')
    ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def categoryIcon():
    return Svg([
        Path(fillRule='evenodd', d='M2 6a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1H8a3 3 0 00-3 3v1.5a1.5 1.5 0 01-3 0V6z', clipRule='evenodd'),
        Path(d='M6 12a2 2 0 012-2h8a2 2 0 012 2v2a2 2 0 01-2 2H2h2a2 2 0 002-2v-2z')
    ], className='icon icon-xs text-gray-500 me-2', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def icon1():
    return  Svg([
        Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
    ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def icon2():
    return  Svg([
        Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
    ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def icon3():
    return  Svg([
        Path(fillRule='evenodd', d='M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11.707 4.707a1 1 0 00-1.414-1.414L10 9.586 8.707 8.293a1 1 0 00-1.414 0l-2 2a1 1 0 101.414 1.414L8 10.414l1.293 1.293a1 1 0 001.414 0l4-4z', clipRule='evenodd')
    ], className='icon icon-xs text-gray-500 ms-1', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')

def upIcon():
    return Svg([
        Path(fillRule='evenodd', d='M14.707 12.707a1 1 0 01-1.414 0L10 9.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 010 1.414z', clipRule='evenodd')
    ], className='icon icon-xs text-success', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')


def categoryRank(category, categoryIcon, rank, rankIcon):
    return html.Div([
        html.Div([
            html.Div([
                categoryIcon(),
                category
            ], className='h6 mb-0 d-flex align-items-center')
        ]),
        html.Div([
            html.A([
                rank,
                rankIcon()
            ], href='#', className='d-flex align-items-center fw-bold')
        ])
    ], className='d-flex align-items-center justify-content-between border-bottom pb-3')

def categoryRankExt(category, categoryIcon, rank, notes, upDownIcon, rankIcon):
    return html.Div([
        html.Div([
            html.Div([
                categoryIcon(),
                category
            ], className='h6 mb-0 d-flex align-items-center'),
            html.Div([
                notes,
                upDownIcon()
            ], className='small card-stats')
        ]),
        html.Div([
            html.A([
                rank,
                rankIcon()
            ], href='#', className='d-flex align-items-center fw-bold'),
        ])
    ], className='d-flex align-items-center justify-content-between border-bottom pb-3')


def globalRank():
    return html.Div([
        html.Div([
            html.Div([
                categoryRank("Global Rank", earthIcon, '#755', icon1),
                categoryRankExt("Country Rank", countryIcon, '#32', "United States", upIcon, icon2),
                categoryRankExt("Category Rank", categoryIcon, '#11', "Computers Electronics > Technology", upIcon, icon3),
           ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 px-0 mb-4')
