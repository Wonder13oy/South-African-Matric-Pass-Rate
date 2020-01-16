import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/matric-pass-rate.csv').set_index('Province')


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
            xaxis={'title': 'Years'},
            yaxis={'title': 'Percentage'},
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
