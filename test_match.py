import logging
from multiprocessing import Array
from dash import Dash, html, ALL

from dash_spa import prefix, match, isTriggered
import dash_bootstrap_components as dbc

from server import serve_app

id = prefix('test')
btn = match({'type': id('button'), 'idx': ALL})

button1 = dbc.Button("Button1", id=btn.idx(1))
button2 = dbc.Button("Button2", id=btn.idx(2))
div = html.H2(id=id("output"))

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP], assets_folder='empty')
app.layout = html.Div([button1, button2, div])

call_count = Array("i", [0, 0])

@app.callback(div.output.children, btn.input.n_clicks)
def update_output(n_clicks):
    if isTriggered(button1.input.n_clicks):
        logging.info('Button1')
        call_count[0] += 1

    if isTriggered(button2.input.n_clicks):
        logging.info('Button2')
        call_count[1] += 1

    return f"Button1.n_clicks={call_count[0]}, Button2.n_clicks={call_count[1]}"

if __name__ == "__main__":

    logging.basicConfig(
        level= "INFO",
        # format='%(levelname)s %(asctime)s.%(msecs)03d %(module)10s/%(lineno)-5d %(message)s'
        format='%(levelname)s %(module)10s/%(lineno)-5d %(message)s'
    )

    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    serve_app(app, debug=False)
