### dash-flightdeck

![](doc/img/flightdeck-1.png)

Plotly/Dash based Dashboard Template based on beautiful [Volt](https://demo.themesberg.com/volt/) Bootstrap 5 Template

**dash-flightdeck** Is 100% python. It demonstrates how a rich UI experience can be easily
created using Dash/SPA components and patterns.

**dash-flightdeck** Shows how easy it is to create great looking tables with optional search and pagination. Table cells
can contain text and active components. Table, search and pagination component layout is completely flexible.

![](./doc/img/tables-1.png)

```
class TrafficTable(BasicTable):

    def tableRow(self, index, args):

        cid, ts, st, cat, rank, share, change = args.values()

        return html.Tr([
            html.Td([
                html.A(cid, href='#', className='text-primary fw-bold')
            ]),
            html.Td([
                icons[ts],
                ts
            ], className='fw-bold d-flex align-items-center'),
            html.Td(st),
            html.Td(cat),
            html.Td(rank),
            progressBar(share),
            self.numberAndArrow(change)
        ])
```

![](./doc/img/tables-2.png)

### Usage

    pip install -r requirements.txt

    python app.py

or

    python waitress_server.py

### Links

* [demo](https://demo.themesberg.com/volt/pages/dashboard/dashboard.html)
* [docs](https://themesberg.com/docs/volt-bootstrap-5-dashboard/getting-started/quick-start/)
* [Volt Bootstrap 5 Dashboard](https://demo.themesberg.com/volt/)
* [github](https://github.com/themesberg/volt-bootstrap-5-dashboard)
* [heroicons](https://heroicons.dev/)