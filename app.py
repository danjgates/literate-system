# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import base64
import io
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Input SSID'),
    dcc.Input(id='input-2-state', type='text', value='Date YYYY-MM-DD'),
    dcc.Input(id='input-3-state', type='text', value='Input Email'),
    dcc.Dropdown(['Sample type', 'Dried Biomass', 'Ferm Broth' , 'Oil' , 'Polyol' , 'Seed/Plant', 'Other'], 'Sample type', id='demo-dropdown'),
    dash_table.DataTable(
        columns=[
            {"name": ["Sample No."], "id": "sample", "clearable": "first" },
            {"name": ["Block"], "id": "block"},
            {"name": ["Sample ID"], "id": "sampleid"},
            {"name": ["Glucose Consumption"], "id": "gluc"},
            {"name": ["Sample Weight"], "id": "weight"},
            {"name": ["Unit"], "id": "unit"},
        ],
        data=[
            {
                "sample": i,
                "block": i * 0,
                "sampleid": i * 0,
                "gluc": i * 0,
                "weight": i * 0,
                "unit": i * 0,
            }
            for i in range(10)
        ],
        css=[
            {"selector": ".column-header--delete svg", "rule": 'display: "none"'},
            {"selector": ".column-header--delete::before", "rule": 'content: "X"'}
        ],
    editable=True
    ),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Div(id='output-state2'),
    html.Div(id='output-state3')
])


@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('demo-dropdown', 'value'),
              State('input-1-state', 'value'))
def update_output(n_clicks, dropdown, input1):
    if n_clicks==0:
        return u'''
                Please complete form and press submit
            '''.format(n_clicks, dropdown, input1)
    else:
        return u'''
            The Submit button has been pressed {} times,
            you have opened a submission for {},
            your SSID is {},
            '''.format(n_clicks, dropdown, input1)

@app.callback(Output('output-state2', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'))
def update_output2(n_clicks, date, email):
    if n_clicks == 0:
        return u'''
                '''.format(n_clicks, date, email)
    else:
        return u'''
            you submitted on {},
            A confirmation email has been sent to {},
            '''.format(date, email)

@app.callback(Output('output-state3', 'children'),
              Input('submit-button-state', 'n_clicks'))
def update_output3(n_clicks):
    if n_clicks == 0:
        return u'''
                '''.format(n_clicks)
    else:
        return u'''
            Please save a copy of your confirmation email and information for this SSID
            '''



if __name__ == '__main__':
    app.run_server(debug=True)