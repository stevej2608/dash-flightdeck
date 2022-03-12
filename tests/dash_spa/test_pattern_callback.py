import time
from multiprocessing import Array
from dash import Dash, html, ALL

from dash_spa import prefix, match, isTriggered

def test_pattern_ids(dash_duo):

    # https://dash.plotly.com/pattern-matching-callbacks

    pid = prefix('i7dc776af_804d')
    btn = match({'type': pid('button'), 'idx': ALL})

    button1 = html.Button(id=btn.idx(1))
    button2 = html.Button(id=btn.idx(2))

    div = html.Div(id=pid("output"))

    app = Dash(__name__)
    app.layout = html.Div([button1, button2, div])

    call_count = Array("i", [0, 0])

    @app.callback(div.output.children, btn.input.n_clicks)
    def _update_output(n_clicks):
        if isTriggered(button1.input.n_clicks):
            call_count[0] = n_clicks[0]

        if isTriggered(button2.input.n_clicks):
            call_count[1] = n_clicks[1]

        return f"Button1.n_clicks={call_count[0]}, Button2.n_clicks={call_count[1]}"

    dash_duo.start_server(app)

    dash_duo.multiple_click(button1.css_id, clicks=1)
    dash_duo.multiple_click(button2.css_id, clicks=2)

    time.sleep(3)

    assert call_count[0] == 1
    assert call_count[1] == 2
    assert dash_duo.find_element(div.css_id).text == "Button1.n_clicks=1, Button2.n_clicks=2"
