from holoniq.utils import log
from dash import Dash, dcc, html, MATCH, ALLSMALLER
import pandas as pd

from dash_spa import match
from server import serve_app

# https://dash.plotly.com/pattern-matching-callbacks#simple-example-with-allsmaller

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash(__name__, suppress_callback_exceptions=True)

button = html.Button("Add Filter", id="add-filter-ex3", n_clicks=0)
container = html.Div(id='container-ex3', children=[])
app.layout = html.Div([button, container])

# Define MATCH & ALLSMALLER factories for the filter components
# and associated callbacks

filter_output_match = match({'type': 'output-ex3','index': MATCH })
filter_dropdown_match = match({'type': 'filter-dropdown-ex3','index': MATCH })
filter_dropdown_smaller = match({'type': 'filter-dropdown-ex3','index': ALLSMALLER })

# Add initial and then additional filters in response to
# user clicking the 'Add Filter' button

@app.callback(container.output.children,button.input.n_clicks, container.state.children)
def display_dropdowns(n_clicks, existing_children):
    log.info('display_dropdowns %d', n_clicks)
    existing_children.append(html.Div([
        dcc.Dropdown(
            df['country'].unique(),
            df['country'].unique()[n_clicks],
            id=filter_dropdown_match.index(n_clicks)
        ),
        html.Div(id=filter_output_match.index(n_clicks))
    ]))
    return existing_children

# Following a filter dropdown selection by the user, this callback is
# called repeatedly by Dash, starting with dropdown/div pair that is
# at the bottom of the list and finishing with dropdown that
# was selected by the user.
#
# On each callback invocation, N, the callback's previous_values[] argument contains
# the values of the ALLSMALLER dropdown fillters [0..N-1]. That is the filter
# values starting with the top filter down to the filter N-1

@app.callback(
    filter_output_match.output.children,
    filter_dropdown_match.input.value,
    filter_dropdown_smaller.input.value,
    filter_output_match.state.id)
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
