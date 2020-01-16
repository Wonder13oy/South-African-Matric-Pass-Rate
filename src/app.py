import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from flask import Flask
import pandas as pd
import numpy as np

df = pd.read_csv('../data/matric-pass-rate.csv')

app = dash.Dash()
headers = df.columns


# @app.callback(Output('graph-output-1', 'figure'),
#               [Input('navigator', 'value')])
def display_all():
    overall_table = [
        go.Table(
            header=dict(values=df.columns),
            cells=dict(values=[df['Province'], df['2009'], df['2010'], df['2011'], df['2012'], df['2013']])
        )
    ]

    return {
        'data': overall_table,
        'layout': go.Layout(
            title='Table of pass rate over the years'
        )
    }


# @app.callback(Output('tabs-content-example', 'children'),
#               [Input('navigator', 'value')])
def graph_line():

    line_graph = [
        go.Scatter(
            x=df['Province'],
            y=df['2009'],
            marker={
                'size': 15,
                'symbol': 'circle',
                'line': {
                    'width': 0.5,
                    'color': 'white'
                }
            }
        )
    ]
    return {
        'data': line_graph,
        'layout': go.Layout(
            title=f'Change in Pass Rate',
            xaxis={'title': 'Province'},
            yaxis={'title': 'Years'},
        )
    }


def show_update():

    bar_graph = [
        go.Bar(
            x=df.Province.unique(),
            y=df['2009']
        )
    ]

    return {
        'data': bar_graph,
        'layout': go.Layout(
            xaxis={'title': 'Provinces'},
            yaxis={'title': '2009'},
        )
    }


# HTML STRUCTURE
app.title = 'Matric Pass Rate'
app.layout = html.Div([
    dcc.Tabs(id='navigator', value='tab-overall', children=[
        dcc.Tab(label='Overall', value='tab-overall', children=[
            dcc.Graph(id='graph-output-1')
        ]),
        dcc.Tab(id='breakdown', label='Breakdown', value='tab-breakdown', children=[
            dcc.Graph(id='top-graph')
        ])
    ]),
    html.Div(id='tabs-content-example')
])


@app.callback(Output('tabs-content-example', 'children'),
              [Input('navigator', 'value')])
def select_tab(tab):
    if tab == 'tab-overall':
        return display_all()
    elif tab == 'tab-breakdown':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])


# START POINT
if __name__ == '__main__':
    app.run_server()
