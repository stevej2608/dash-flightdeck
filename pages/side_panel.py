from dash import  html
from flask import current_app

from components import SubListAIO

def Brand():
    return html.Div([
        html.A(' ⚡︎ Simple Dashboard', className='navbar-brand', href='#'),
        html.Button([
            html.Span(className='navbar-toggler-icon')
        ], className='navbar-toggler d-md-none collapsed mb-3', type='button', tabIndex='collapse')
    ], className='d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between')


def SideLink(title, icon=None, alt=None, active=False, href="#"):
    app = current_app.get_dash()
    active = " active" if active else ""
    return  html.Li([
        html.A([
            html.Img(src=app.get_asset_url(icon), className='feather feather-home', alt=alt),
            html.Span(title, className='ml-2')
        ], href=href, className='nav-link' + active)
    ], className='nav-item')

def SideButton(title, href="#", btn_style="btn-secondary"):
    return html.Li([
        html.A(title, className=f'btn btn-sm {btn_style} ml-3 mt-2', href=href)
    ], className='nav-item')

def SideIconButton(title, icon=None, alt=None, href="#", btn_style="btn-secondary"):
    app = current_app.get_dash()
    return html.Li([
        html.A([
            html.Img(src=app.get_asset_url(icon), className='bi-book', alt=alt),
            html.Span(title, className='ml-2')
        ], className=f'btn btn-sm {btn_style} ml-3 mt-2', href=href)
    ], className='nav-item')

def SideGroup(heading, icon, children):
    return html.Div([
        html.Li([heading, html.I(className=icon)], className="navList__heading"),
        html.Div(children)
    ])


def SidePanel():
    return  html.Div([
            html.Ul([
                Brand(),

                SideGroup("Documents", "far fa-file-alt", [
                    SubListAIO("insurance",["medical","vision","dental"], icon="fas fa-briefcase-medical"),
                    SubListAIO("travel",["domestic","foreign","misc"], icon="fas fa-plane-departure"),
                    SubListAIO("taxes",["current","archives"], icon="far fa-angry"),
                ]),

                SideLink('Dashboard', icon="feather-home.svg", alt="home", active=True),
                SideLink('Orders', icon="feather-file.svg", alt="file"),
                SideLink('Products', icon="feather-shopping-cart.svg", alt="shopping-cart"),
                SideLink('Customers', icon="feather-users.svg", alt="users"),
                SideLink('Reports', icon="feather-bar-chart-2.svg", alt="bar-chart-2"),
                SideLink('Integrations', icon="feather-layers.svg", alt="layers"),
                SideIconButton('Read tutorial', icon="bi_book.svg", alt="book", href='https://themesberg.com/blog/bootstrap/simple-bootstrap-5-dashboard-tutorial'),
                SideButton(' ⚡︎ Volt Dashboard', btn_style='btn-warning', href='https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard'),
                SideButton('By Themesberg ❤️', btn_style='btn-primary', href='https://themesberg.com')
            ], className='nav flex-column')
        ], className='position-sticky')
