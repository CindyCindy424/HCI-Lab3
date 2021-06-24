# -*- coding: utf-8 -*-
# @Author  : Deng Xinling
# @Time    : 2021/6/24 0:07
# @Function: Lab3 for HCI course in TONGJI SSE

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

app = dash.Dash()

df = pd.read_csv(r'./dataset/googleplaystore.csv')
df2 = pd.read_csv(r'./dataset/googleplaystore-byrating.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

available_indicators = df['Category'].unique()

app.layout = html.Div([
    dcc.Markdown('''
    ### Lab3 - Data Visualization
    #### Author: 1850477 邓欣凌
    ###### Dataset: Google Play Store Apps
    -------------------------
    ##### Visualization 1
    
    '''),
    html.Br(),
    html.Div("Choose a category for the app from the list below!"),
    html.Br(),
    dcc.Dropdown(id='category',
                 options=[{
                     'label': i,
                     'value': i
                 } for i in available_indicators],  # 下拉框的项为软件分类列表
                 value='ART_AND_DESIGN'),
    dcc.Graph(id='graph1'),
    dcc.Markdown('''
    -------
    ##### Visualization 2
    
    '''),
    html.Br(),
    dcc.Graph(id='graph2'),

    dcc.Markdown('''
    -------
    ##### Visualization 3

    '''),
    html.Br(),
    html.P("Select Distribution:"),
    dcc.RadioItems(
        id='dist-marginal',
        options=[{'label': x, 'value': x}
                 for x in ['box', 'violin', 'rug']],
        value='box'
    ),
    dcc.Graph(id="graph3"),
    dcc.Markdown('''
    -------
    ##### Visualization 4

    '''),
    html.Br(),
    dcc.Graph(id="pie-chart",
              figure=px.pie(df2, values='Number of Apps', names='Category', title='Proportion of different app types')),
    dcc.Markdown('''
    -------
    ##### Visualization 5
    '''),
    html.Br(),
    dcc.Graph(id='graph5',
              figure=px.bar_polar(df2, r='Number of Apps', theta='Category', color='Rating Range',
                                  color_discrete_sequence=px.colors.sequential.Plasma_r)
              )
])


@app.callback(
    Output('graph1', 'figure'),
    Input('category', 'value'))
def update_figure(selected_category):
    filtered_df = df[df['Category'] == selected_category]

    fig = px.scatter(filtered_df, x="Reviews", y="Rating",
                     size="Reviews", color="Type", hover_name="App",
                     size_max=100)

    fig.update_layout(transition_duration=500)

    return fig


@app.callback(
    Output('graph2', 'figure'),
    Input('category', 'value'))
def update_figure2(selected_category):
    fig = px.bar(df2, x='Category', y='Number of Apps', color='Rating Range', pattern_shape='Rating Range',
                 pattern_shape_sequence=[".", "x", "+"])
    return fig


@app.callback(
    Output("graph3", "figure"),
    [Input("dist-marginal", "value")])
def display_graph(marginal):
    fig = px.histogram(
        df, x="Content Rating", y="Reviews", color="Type",
        marginal=marginal,
        hover_data=df.columns)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
