import logging
from multiprocessing import Value
from dash import Dash, html, ALL

from dash_spa import prefix, match

from server import serve_app

id = prefix('test')
btn = match({'type': id('button'), 'idx': ALL})

button1 = html.Button(id=btn.idx(1))
button2 = html.Button(id=btn.idx(2))

div = html.Div(id=id("output"))


call_count = Value("i", 0)

app = Dash(__name__)
app.layout = html.Div([button1, button2, div])

@app.callback(div.output.children, btn.input.n_clicks)
def update_output(n_clicks):
    call_count.value = call_count.value + 1
    return n_clicks

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

