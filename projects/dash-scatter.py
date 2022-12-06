import dash
import dash_core_components as dcc
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df= pd.read_excel("raw_data_last.xlsx")


app.layout = html.Div([
    html.Label("Choose 1:", style={'fontSize':30, 'textAlign':'center'}),
    dcc.Dropdown(
        id='states-dpdn',
        options=[{'label': s, 'value': s} for s in df.columns],
        value='x',
        clearable=False
    ),

    html.Label("Choose 2:", style={'fontSize':30, 'textAlign':'center'}),
    dcc.Dropdown(
        id='counties-dpdn',
        options=[{'label': s, 'value': s} for s in df.columns],
        value="y",
        clearable=False
    ),
    dcc.Graph(id='display-map')
])

@app.callback(
    Output('counties-dpdn', 'options'),
    Input('states-dpdn', 'value')
)

@app.callback(
    Output('counties-dpdn', 'value'),
    Input('counties-dpdn', 'options')
)
def set_cities_value(available_options):
    return [x['value'] for x in available_options]



@app.callback(
    Output('display-map', 'figure'),
    Input('counties-dpdn', 'value'),
    Input('states-dpdn', 'value')
)
def update_grpah(selected_counties, selected_state):
        fig = px.scatter(df, x=selected_counties, y=selected_state)
        return fig


if __name__ == '__main__':
    app.run_server(debug=True, port=3004)


