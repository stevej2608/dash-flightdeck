from holoniq.utils import log
from dash import Dash, dcc, html, Input, Output, State, MATCH, ALLSMALLER
import pandas as pd

from server import serve_app

# https://dash.plotly.com/pattern-matching-callbacks#simple-example-with-allsmaller

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Button('Add Filter', id='add-filter-ex3', n_clicks=0),
    html.Div(id='container-ex3', children=[]),
])

# Add initial and then additional filters in response to
# use clicking the 'Add Filter' button

@app.callback(
    Output('container-ex3', 'children'),
    Input('add-filter-ex3', 'n_clicks'),
    State('container-ex3', 'children'))
def display_dropdowns(n_clicks, existing_children):
    log.info('display_dropdowns %d', n_clicks)
    existing_children.append(html.Div([
        dcc.Dropdown(
            df['country'].unique(),
            df['country'].unique()[n_clicks],
            id={
                'type': 'filter-dropdown-ex3',
                'index': n_clicks
            }
        ),
        html.Div(id={
            'type': 'output-ex3',
            'index': n_clicks
        })
    ]))
    return existing_children


# Following a filter selection by the user, this callback is
# called repeatedly by Dash, starting with dropdown/div pair that is
# at the bottom of the list and finishing with dropdown that
# was selected for update by the user.
#
# On each indexed invocation, N, the callback's previous_values[] argument contains
# the values of the ALLSMALLER dropdown fillters [0..N-1].


@app.callback(
    Output({'type': 'output-ex3', 'index': MATCH}, 'children'),
    Input({'type': 'filter-dropdown-ex3', 'index': MATCH}, 'value'),
    Input({'type': 'filter-dropdown-ex3', 'index': ALLSMALLER}, 'value'),
    State({'type': 'output-ex3', 'index': MATCH}, 'id')
)
def display_output(matching_value, previous_values, id):
    log.info('display_output %s, %s, %s', id['index'], matching_value, previous_values)
    previous_values_in_reversed_order = previous_values[::-1]
    all_values = [matching_value] + previous_values_in_reversed_order

    dff = df[df['country'].str.contains('|'.join(all_values))]
    avgLifeExp = dff['lifeExp'].mean()

    # Return a slightly different string depending on number of values
    if len(all_values) == 1:
        return html.Div('{:.2f} is the life expectancy of {}'.format(
            avgLifeExp, matching_value
        ))
    elif len(all_values) == 2:
        return html.Div('{:.2f} is the average life expectancy of {}'.format(
            avgLifeExp, ' and '.join(all_values)
        ))
    else:
        return html.Div('{:.2f} is the average life expectancy of {}, and {}'.format(
            avgLifeExp, ', '.join(all_values[:-1]), all_values[-1]
        ))

if __name__ == '__main__':
    serve_app(app, debug=False)
