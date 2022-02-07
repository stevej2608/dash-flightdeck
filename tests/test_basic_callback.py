import time
from multiprocessing import Value, Array
from dash import Dash, Input, Output, html, ALL, MATCH

from dash_spa import prefix, match, isTriggered, css_id, AIOPrefix, AIOBase

def test_simple_ids(dash_duo):

    id = prefix('test')

    button = html.Button(id=id("input"))
    div = html.Div(id=id("output"))

    app = Dash(__name__)
    app.layout = html.Div([button, div])

    call_count = Value("i", 0)

    @app.callback(div.output.children, button.input.n_clicks)
    def update_output(n_clicks):
        call_count.value = call_count.value + 1
        if n_clicks == 1:
            time.sleep(1)
        return n_clicks

    dash_duo.start_server(app)
    dash_duo.multiple_click("#test_input", clicks=3)

    time.sleep(3)

    assert call_count.value == 4, "get called 4 times"
    assert dash_duo.find_element("#test_output").text == "3", "clicked button 3 times"

def test_pattern_ids(dash_duo):

    # https://dash.plotly.com/pattern-matching-callbacks

    pid = prefix(__name__)
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

    dash_duo.multiple_click(css_id(button1), clicks=1)
    dash_duo.multiple_click(css_id(button2), clicks=2)

    time.sleep(1)

    assert call_count[0] == 1
    assert call_count[1] == 2
    assert dash_duo.find_element(f"#{div.id}").text == "Button1.n_clicks=1, Button2.n_clicks=2"
