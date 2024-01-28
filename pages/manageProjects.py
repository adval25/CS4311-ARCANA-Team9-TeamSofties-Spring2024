import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd



dash.register_page(__name__, path='/manageProjects')


def createTable():
    row0 = html.Tr(html.Td("Project A"),)
    row1 = html.Tr(html.Td("Project B"),)
    row2 = html.Tr(html.Td("Project C"),)
    row3 = html.Tr(html.Td("Project D"),)

    table_body = [html.Tbody([row0,row1, row2,row3])]
    
    return dbc.Table( table_body, bordered=True)

def generateManageProjectCard():
   return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col(
                    children=[
                        dbc.Col([
                        html.Img(
                        src=dash.get_asset_url("fileImage.png"),
                        className="img-fluid rounded-start",
                        style={"width": "90px", "height": "90px","margin-right": 0, "margin-bottom" : "0%", "padding-top" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Manage Projects", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        ]),
                        dbc.Button("+ Create Project", color="primary",href = "#", style={'display': 'inline-block'} , className="position-absolute top-0 end-0 m-3"),
                        html.Br(),

                        createTable(),
                        html.Div(
                        [
                            dbc.Button("Ingest Logs", color="primary",href = "#"),
                            dbc.Button("Delete Project", color="primary",href = "#"),
                            dbc.Button("Open Project", color="primary",href = "#"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                        ), 

                        ],
                ),
                dbc.Col(width=1)
            ],
        
        ),style={"height": 500, "width": 900,},className="mx-auto"
       
    )
)

layout = html.Div([
    dbc.Container([
       generateManageProjectCard()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])