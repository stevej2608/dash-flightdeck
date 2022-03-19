from dash import html, dash_table
from dash_spa import spa_table
import pandas as pd
from collections import OrderedDict

from app import create_app
from server import serve_app

# Dash Example
# https://dash.plotly.com/datatable/height

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

# Example using the Dash javascript DataTable component

layout_dash = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_size=10
)

# Example using the pure python  DataTable clone

layout_spa = spa_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    page_size=10
)

if __name__ == "__main__":
    layout = html.Div(layout_spa)
    app = create_app(layout, plugins=[])
    serve_app(app, debug=False)
