import logging
from multiprocessing import Array
from dash import Dash, html, ALL, callback

from dash_spa import prefix, match, isTriggered
import dash_bootstrap_components as dbc

from server import serve_app

def layout():

    logging.info('layout')

    pid = prefix()
    btn = match({'type': pid('button'), 'idx': ALL})

    button1 = dbc.Button("Button1", id=btn.idx(1))
    button2 = dbc.Button("Button2", id=btn.idx(2))
    div = html.H2(id=pid("output"))


    call_count = Array("i", [0, 0])

    @callback(div.output.children, btn.input.n_clicks)
    def update_output(n_clicks):
        if isTriggered(button1.input.n_clicks):
            call_count[0] = n_clicks[0]

        if isTriggered(button2.input.n_clicks):
            call_count[1] = n_clicks[1]

        return f"Button1.n_clicks={call_count[0]}, Button2.n_clicks={call_count[1]}"

    return html.Div([button1, button2, div])

if __name__ == "__main__":

    logging.basicConfig(
        level= "INFO",
        # format='%(levelname)s %(asctime)s.%(msecs)03d %(module)10s/%(lineno)-5d %(message)s'
        format='%(levelname)s %(module)10s/%(lineno)-5d %(message)s'
    )

    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP], assets_folder='empty')
    app.layout = layout()

    serve_app(app, debug=False)
