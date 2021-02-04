import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from generate_epa_totals_plot import make_epa_totals_plot
from generate_epa_pie_plot import make_epa_total_pie
from generate_budget_line_graphs import make_program_area_line_plot
from generate_program_bar_charts import make_program_bar_chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

epa_totals_df = pd.read_csv('epa_totals.csv')
epa_totals_plot = make_epa_totals_plot(epa_totals_df)

df = pd.read_pickle('epa_budget.pkl')
program_area_totals = df.groupby(['Program Area', 'Year']).tail(1)[:-1]
program_areas = program_area_totals['Program Area'].unique()

#Begin app layout
app.layout = html.Div(children=[
    html.H1(children='EPA Budget (2011-2021) Visualization'),

    html.Div(children='''
        USAFacts Environmental Data Hackathon 2021
    '''),

    dcc.Graph(
        id='epa-total',
        figure=epa_totals_plot
    ),
    # html.Div([
    # dcc.Dropdown(
    #     id='year-dropdown',
    #     options=[{'label': i, 'value': i} for i in range(2011, 2022)],
    #     value=2021
    #     )]),

    # html.Div(id='year-dd-output-container'),
    html.Div(id='slider-output-container'),
    dcc.Slider(id='year-slider',
               min=df['Year'].min(),
               max=df['Year'].max(),
               step=1,
               value=df['Year'].max(),
               marks={str(year): str(year) for year in df['Year'].unique()}),

    # dcc.Graph(id='budget-by-program-area',
    #           figure=make_program_area_line_plot(program_area_totals)),
    html.Div([
            dcc.Dropdown(
                id='program-area-dd',
                options=[{'label': i, 'value': i} for i in program_areas],
                value='Science & Technology'
            ),
            dcc.RadioItems(
                id='bar-type',
                options=[{'label': i, 'value': i} for i in ['stack', 'group']],
                value='stack',
                labelStyle={'display': 'inline-block'}
            ),
            html.Div(id='program-area-dd-output-container')
        ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
    ])

# @app.callback(
#     dash.dependencies.Output('year-dd-output-container', 'children'),
#     [dash.dependencies.Input('year-dropdown', 'value')])
# def update_pie(value):
#     epa_pie = make_epa_total_pie(program_area_totals, value)
#     return html.Div(
#                 dcc.Graph(id='epa-pie',
#                           figure=epa_pie)
#     )

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_output(value):
    epa_pie = make_epa_total_pie(program_area_totals, value)
    return html.Div(
                    dcc.Graph(id='epa-pie', figure=epa_pie))

@app.callback(
    dash.dependencies.Output('program-area-dd-output-container', 'children'),
    [dash.dependencies.Input('program-area-dd', 'value'),
     dash.dependencies.Input('bar-type', 'value')])
def update_bar(program_area, barmode):
    program_area_bar = make_program_bar_chart(df, program_area, barmode)
    return html.Div(
                    dcc.Graph(id='program-area_bar', figure=program_area_bar))

if __name__ == '__main__':
    app.run_server(debug=True)
