import time
from multiprocessing import Value
from dash import Dash, Input, Output, State, callback_context, html, dcc, dash_table

def test_callback(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div([html.Button(id="input", n_clicks=0), html.Div(id="output")])

    call_count = Value("i", 0)

    @app.callback(Output("output", "children"), [Input("input", "n_clicks")])
    def update_output(n_clicks):
        call_count.value = call_count.value + 1
        if n_clicks == 1:
            time.sleep(1)
        return n_clicks

    dash_duo.start_server(app)
    dash_duo.multiple_click("#input", clicks=3)

    time.sleep(3)

    assert call_count.value == 4, "get called 4 times"
    assert dash_duo.find_element("#output").text == "3", "clicked button 3 times"

