import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/matric-pass-rate.csv').set_index('Province')

app = dash.Dash()
headers = df.columns


def tab_one():
    overall_table = [
        go.Table(
            header=dict(values=df.columns.insert(0, 'Provinces')),
            cells=dict(values=[df.index, df['2009'], df['2010'], df['2011'], df['2012'], df['2013']])
        )
    ]

    return {
        'data': overall_table,
        'layout': go.Layout(
            title='Table of pass rate over the years'
        )
    }


def tab_two():
    return graph_bar()


def graph_line():

    line_graph = []

    for prov in df.index:
        line_graph.append(
            go.Scatter(
                x=df.columns,
                y=df.loc[prov],
                marker={
                    'size': 15,
                    'symbol': 'circle',
                    'line': {
                        'width': 0.5,
                        'color': 'white'
                    }
                },
                name=prov
            )
        )

    return {
        'data': line_graph,
        'layout': go.Layout(
            title=f'Change in Pass Rate',
            xaxis={'title': 'Province'},
            yaxis={'title': 'Years'},
        )
    }


def graph_bar():

    bar_graph = []

    for x in range(2009, 2014):

        bar_graph.append(go.Bar(
            x=df.index,
            y=df[str(x)],
            name=str(x)
        ))

    return {
        'data': bar_graph,
        'layout': go.Layout(
            xaxis={'title': 'Provinces'},
            yaxis={'title': 'Percentages'},
        )
    }


# HTML STRUCTURE
app.title = 'Matric Pass Rate'
app.layout = html.Div([
    dcc.Tabs(id='navigator', value='tab-overall', children=[
        dcc.Tab(label='Overall', value='tab-overall', children=[
            dcc.Graph(
                id='graph-output-1',
                figure=tab_one()
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
    ]),
    html.Div(id='tabs-content-example')
])

# START POINT
if __name__ == '__main__':
    app.run_server()
