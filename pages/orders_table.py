from dash import html

def OrdersTable():
    return html.Div([
        html.Table([
            html.Thead([
                html.Tr([
                    html.Th('Order', scope='col'),
                    html.Th('Product', scope='col'),
                    html.Th('Customer', scope='col'),
                    html.Th('Total', scope='col'),
                    html.Th('Date', scope='col'),
                    html.Th(scope='col')
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17371705', scope='row'),
                    html.Td('Volt Premium Bootstrap 5 Dashboard'),
                    html.Td('johndoe@gmail.com'),
                    html.Td('€61.11'),
                    html.Td('Aug 31 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ]),
                html.Tr([
                    html.Th('17370540', scope='row'),
                    html.Td('Pixel Pro Premium Bootstrap UI Kit'),
                    html.Td('jacob.monroe@company.com'),
                    html.Td('$153.11'),
                    html.Td('Aug 28 2020'),
                    html.Td([
                        html.A('View', href='#', className='btn btn-sm btn-primary')
                    ])
                ])
            ])
        ], className='table')
    ], className='table-responsive')
