from collections import OrderedDict
from dash import html
import pandas as pd
from components.table import TableAIO

data = OrderedDict([
    ('#',['456478', '456423', '456420', '456421', '456420', '456479', '456478', '453673', '456468', '456478']),
    ('Bill For',['Platinum Subscription Plan', 'Platinum Subscription Plan', 'Platinum Subscription Plan', 'Platinum Subscription Plan', 'Platinum Subscription Plan', 'Platinum Subscription Plan', 'Platinum Subscription Plan', 'Gold Subscription Plan', 'Gold Subscription Plan', 'Flexible Subscription Plan']),
    ('Issue Date',['1 May 2020', '1 Apr 2020', '1 Mar 2020', '1 Feb 2020', '1 Jan 2020', '1 Dec 2019', '1 Nov 2019', '1 Oct 2019', '1 Sep 2019', '1 Aug 2019']),
    ('Due Date',['1 Jun 2020', '1 May 2020', '1 Apr 2020', '1 Mar 2020', '1 Feb 2020', '1 Jan 2020', '1 Dec 2019', '1 Nov 2019', '1 Oct 2019', '1 Sep 2019']),
    ('Total',['$799.00', '$799.00', '$799.00', '$799.00', '$799.00', '$799.00', '$799.00', '$533.42', '$533.42', '$233.42']),
    ('Status',['Due', 'Paid', 'Paid', 'Paid', 'Paid', 'Paid', 'Paid', 'Cancelled', 'Paid', 'Paid']),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

def table():
    layout = TableAIO(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        page_size=7
    )
    return layout
