import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

dash.register_page(__name__, path='/syncProject')

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
                        html.P("Sync Projects", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        html.Br(),
                        html.P("Enter an IP adress of your coumputer to use"),
                        html.P("use 0.0.0.0 to reffer to all IP adresses of your computer"),
                        html.Br(),
                        dbc.Form(
                        dbc.Row(
                                [
                                dbc.Label("Ip Adress", width="auto"),
                                dbc.Col(
                                dbc.Input(type="Ip adress", placeholder="0.0.0.0"),
                                className="me-3",
                                ),
                                dbc.Col(dbc.Button("Submit", color="primary", style={"margin-left": 0}), width="auto"),
                                dbc.Col(width=1)
                                ],
                        className="g-2",
                        )
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
