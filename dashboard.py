# -*- coding: utf-8 -*-
# @Author  : Deng Xinling
# @Time    : 2021/6/24 0:07
# @Function:

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

app = dash.Dash()

# df1 = pd.read_csv(r'./dataset/degrees-that-pay-back.csv')
# # df1 = df1.T  # 转置df1
# df2 = pd.read_csv(r'./dataset/salaries-by-college-type.csv')
# df3 = pd.read_csv(r'./dataset/salaries-by-region.csv')

df = pd.read_csv(r'./dataset/googleplaystore.csv')
df2 = pd.read_csv(r'./dataset/googleplaystore-byrating.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

available_indicators = df['Category'].unique()

app.layout = html.Div([
    dcc.Dropdown(id='category',
                 options=[{
                     'label': i,
                     'value': i
                 } for i in available_indicators],  # 下拉框的项为软件分类列表
                 value='ART_AND_DESIGN'),
    dcc.Graph(id='graph1'),
    dcc.Graph(id='graph2'),
    html.P("Select Distribution:"),
    dcc.RadioItems(
        id='dist-marginal',
        options=[{'label': x, 'value': x}
                 for x in ['box', 'violin', 'rug']],
        value='box'
    ),
    dcc.Graph(id="graph3"),
    dcc.Graph(id="pie-chart",
              figure=px.pie(df2, values='Number of Apps', names='Category', title='Proportion of different app types'))

])


@app.callback(
    Output('graph1', 'figure'),
    Input('category', 'value'))
def update_figure(selected_category):
    filtered_df = df[df['Category'] == selected_category]

    fig = px.scatter(filtered_df, x="Installs", y="Rating",
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
