import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd

dash.register_page(__name__, path='/syncRequest')

def generateSyncCard():  
    return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("syncIcon.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Create Sync Request", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        html.Br(),
                        html.P("Enter a destination IP Address"),
                        html.P("IP Address"),
                        dbc.Form(
                        dbc.Row(dbc.Col(html.Div(dbc.Input(type="Ip adress", placeholder="0.0.0.0")),width = 3),)
                        ),
                        html.Br(),
                        html.Br(),
                        html.P("Select the projects you want to send to the destination IP Address"),
                        
                        
                        html.Div(
                        [
                            dbc.Label("Projects"),
                            dbc.Checklist(
                                options=[
                                    {"label": "Project A", "value": 1},
                                    {"label": "Project B", "value": 2},
                                    {"label": "Project C", "value": 3},
                                    {"label": "Project D", "value": 4},
                                ],
                                value=[1],
                                id="checklist-input",
                            ),
                        ],
                        ),
                        html.Div(
                        [
                            dbc.Button("Cancel", color="secondary"),
                            dbc.Button("Sync", color="primary"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                        ), 
                        dbc.Col(width=1), 
                            
                        
                    ],
                ),
            ],
        
        ),style={"height": 500, "width": 600,},
       
    )
)
layout = html.Div([
    dbc.Container([
       generateSyncCard()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "width": "80vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])
