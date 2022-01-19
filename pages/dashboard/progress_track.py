from dash import html
from dash_svg import Svg, Path


def progressBar(value, color='success', margin='mb-0'):
    return html.Div([
        html.Div(role='progressbar', className=f'progress-bar bg-{color}', style={"width": f"{value}%"}, **{"aria-valuenow": f"{value}", "aria-valuemin": "0", "aria-valuemax": "100"}),
    ], className=f'{margin} progress')


def _progressBar(title, value, color="success"):
    return html.Div([
        html.Div([
            Svg([
                Path(d='M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'),
                Path(fillRule='evenodd', d='M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', clipRule='evenodd')
            ], className='icon icon-sm text-gray-500', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
        ], className='col-auto'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div(title, className='h6 mb-0'),
                    html.Div([
                        html.Span(f"{value} %")
                    ], className='small fw-bold text-gray-500')
                ], className='progress-info'),
                progressBar(value,color=color, margin='mb-0')
            ], className='progress-wrapper')
        ], className='col')
    ], className='row mb-4')



def progressTrack():
    return html.Div([
        html.Div([
            html.Div([
                html.H2("Progress track", className='fs-5 fw-bold mb-0'),
                html.A("See tasks", href='#', className='btn btn-sm btn-primary')
            ], className='card-header border-bottom d-flex align-items-center justify-content-between'),
            html.Div([
                _progressBar("Rocket - SaaS Template", 75),
                _progressBar("Themesberg - Design System", 60),
                _progressBar("Homepage Design in Figma", 45, color='warning'),
                _progressBar("Backend for Themesberg v2", 34, color='danger'),
            ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 col-xxl-6 mb-4')

