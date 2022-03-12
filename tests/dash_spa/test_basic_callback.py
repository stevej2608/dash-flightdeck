import time
from multiprocessing import Value
from dash import Dash, html

from dash_spa import prefix

def test_simple_ids(dash_duo):

    pfx = prefix()

    button = html.Button(id=pfx("input"))
    div = html.Div(id=pfx("output"))

    app = Dash(__name__)
    app.layout = html.Div([button, div])

    call_count = Value("i", 0)

    @app.callback(div.output.children, button.input.n_clicks)
    def _update_output(n_clicks):
        call_count.value = call_count.value + 1
        if n_clicks == 1:
            time.sleep(1)
        return n_clicks

    dash_duo.start_server(app)
    dash_duo.multiple_click(button.css_id, clicks=3)

    time.sleep(3)

    assert call_count.value == 4, "get called 4 times"
    assert dash_duo.find_element(div.css_id).text == "3", "clicked button 3 times"
