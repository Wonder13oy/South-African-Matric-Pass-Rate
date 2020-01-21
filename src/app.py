import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from sys import path

path.append('./controllers')

from controllers.src_html import tab_one, graph_bar, graph_line, graph_hist, results_pie, results_table

df = pd.read_csv('../data/matric-pass-rate.csv').set_index('Province')
app = dash.Dash()

year_options = []
provinces = ['National']
for year in df.columns:
    year_options.append({str(year): year})

for prov in df.index:
    provinces.append(({'label': prov, 'value': prov}))

# HTML STRUCTURE
app.title = 'Matric Pass Rate'
app.layout = html.Div([
    dcc.Tabs(id='navigator', value='tab-overall', children=[
        dcc.Tab(label='Overall', value='tab-overall', children=[
            dcc.Graph(
                id='graph-output-1',
                figure=results_table()
            ),
            dcc.Graph(
                id='overall-pie',
                figure=results_pie('National', '2009')
            )
        ]),
        dcc.Tab(id='breakdown', label='Breakdown', value='tab-breakdown', children=[
            dcc.Graph(
                id='top-graph',
                figure=graph_bar()
            ),
            dcc.Graph(
                id='line-graph',
                figure=graph_line()
            )
        ])
    ])
])

# START POINT
if __name__ == '__main__':
    app.run_server()
