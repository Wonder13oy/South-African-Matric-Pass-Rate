import dash
import dash_core_components as dcc
import dash_html_components as html

from sys import path

path.append('./controllers')

from controllers.src_html import tab_one, graph_bar, graph_line, graph_hist

app = dash.Dash()

# HTML STRUCTURE
app.title = 'Matric Pass Rate'
app.layout = html.Div([
    dcc.Tabs(id='navigator', value='tab-overall', children=[
        dcc.Tab(label='Overall', value='tab-overall', children=tab_one()),
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
