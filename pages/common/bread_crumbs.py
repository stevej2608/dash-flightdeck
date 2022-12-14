from dash import html
from ..icons.hero import ICON

def breadCrumbs(trail: list):

    # TODO: Make this interactive

    def links():
        result = []
        trail.insert(0, ICON.HOME)
        for el in trail:
            if el != trail[-1]:
                link = html.Li(html.A(el, href='#'), className='breadcrumb-item')
            else:
                link = html.Li(el, className='breadcrumb-item active')
            result.append(link)
        return result

    return  html.Nav([
        html.Ol(links(), className='breadcrumb breadcrumb-dark breadcrumb-transparent')
    ], className='d-none d-md-inline-block')