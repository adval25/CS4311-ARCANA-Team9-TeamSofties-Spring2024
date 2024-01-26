import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

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
                        html.P("Enter a Destination IP Address"),
                        html.P("IP Address"),
                        #html.Br(),
                        dbc.Form(
                        dbc.Row(dbc.Col(html.Div(dbc.Input(type="Ip adress", placeholder="0.0.0.0")),width = 3),)
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
