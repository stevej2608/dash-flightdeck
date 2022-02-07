from dash import Dash, dcc, html, Input, Output, State, MATCH
from server import serve_app

# https://dash.plotly.com/pattern-matching-callbacks#simple-example-with-match

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button("Add Filter", id="dynamic-add-filter", n_clicks=0),
    html.Div(id='dynamic-dropdown-container', children=[]),
])

@app.callback(
    Output('dynamic-dropdown-container', 'children'),
    Input('dynamic-add-filter', 'n_clicks'),
    State('dynamic-dropdown-container', 'children'))
def display_dropdowns(n_clicks, children):
    new_element = html.Div([
        dcc.Dropdown(
            ['NYC', 'MTL', 'LA', 'TOKYO'],
            id={
                'type': 'dynamic-dropdown',
                'index': n_clicks
            }
        ),
        html.Div(
            id={
                'type': 'dynamic-output',
                'index': n_clicks
            }
        )
    ])
    children.append(new_element)
    return children


@app.callback(
    Output({'type': 'dynamic-output', 'index': MATCH}, 'children'),
    Input({'type': 'dynamic-dropdown', 'index': MATCH}, 'value'),
    State({'type': 'dynamic-dropdown', 'index': MATCH}, 'id'),
)
def display_output(value, id):
    return html.Div('Dropdown {} = {}'.format(id['index'], value))


if __name__ == '__main__':
    serve_app(app, debug=False)
