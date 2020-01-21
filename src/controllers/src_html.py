import plotly.graph_objs as go
import pandas as pd
import dash_core_components as dcc

df = pd.read_csv('../data/matric-pass-rate.csv').set_index('Province')


def tab_one():
    year_options = []
    for year in df.columns:
        year_options.append({'label': str(year), 'value': year})

    return [
        dcc.Dropdown(
            id='year-picker',
            options=year_options,
            value=df['2009'],
            multi=True,
            placeholder="Select a year",
        ),
        dcc.Graph(
            id='graph-output-1',
            figure=results_table()
        ),
        dcc.Graph(
            id='overall-pie',
            figure=results_pie('National', '2009')
        )
    ]


def results_table():
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


def results_pie(level, year):
    pass_rate = 0

    if level == 'National':
        pie_chart = [
            go.Pie(
                labels=df.index,
                values=df[year]
            )
        ]

        pass_rate = calculate_avg(df[year])

        return {
            'data': pie_chart,
            'layout': go.Layout(
                title=f'{level} average pass rate at {pass_rate}% in {year}'
            )
        }
    else:
        pie_chart = [
            go.Pie(
                labels=[level, 'other'],
                values=[df[year][level], 100 - df[year][level]]
            )
        ]

        pass_rate = df[year][level]

        return {
            'data': pie_chart,
            'layout': go.Layout(
                title=f'{level} average pass rate at {pass_rate}% in {year}'
            )
        }


def calculate_avg(results_list):
    result = 0

    for x in results_list:
        result += x

    return round(result / 9, 1)


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


def graph_hist():
    hist_graph = [
        go.Histogram(
            x=df['2009'],
            y=df.columns,
            xbins=20
        )
    ]

    return {
        'data': hist_graph,
        'layout': go.Layout(
            xaxis={'title': 'Percentages'},
            yaxis={'title': 'Quantity'},
        )
    }
