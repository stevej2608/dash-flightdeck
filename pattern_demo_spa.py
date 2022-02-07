from dash import Dash, dcc, html, MATCH
from server import serve_app
from dash_spa import prefix, match

# https://dash.plotly.com/pattern-matching-callbacks#simple-example-with-match

app = Dash(__name__, suppress_callback_exceptions=True)

pid = prefix(__name__)

button = html.Button("Add Filter", id=pid("dynamic-add-filter"), n_clicks=0)
container = html.Div(id=pid('dynamic-dropdown-container'), children=[])

dynamic_dropdown = match({'type': 'dynamic-dropdown','index': MATCH })
dynamic_output = match({'type': 'dynamic-output','index': MATCH })

app.layout = html.Div([button,container])

@app.callback(container.output.children, button.input.n_clicks, container.state.children)
def display_dropdowns(n_clicks, children):
    new_element = html.Div([
        html.H2(f'Filter {n_clicks}'),
        dcc.Dropdown( ['NYC', 'MTL', 'LA', 'TOKYO'], id=dynamic_dropdown.index(n_clicks)),
        html.Div(id=dynamic_output.index(n_clicks))
    ])
    children.append(new_element)
    return children

@app.callback(dynamic_output.output.children, dynamic_dropdown.input.value , dynamic_dropdown.state.id)
def display_output(value, id):
    return html.Div(f"Dropdown {id['index']} = {value}")


if __name__ == '__main__':
    serve_app(app, debug=False)
