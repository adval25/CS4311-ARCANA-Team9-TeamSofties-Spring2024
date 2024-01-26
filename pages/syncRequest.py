import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd



dash.register_page(__name__, path='/syncRequest')


def createTable():
    checklist = html.Div(
    [
        dbc.Label("Choose a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Project 1", "value": 1},
                {"label": "Project 2", "value": 2},
                {"label": "Project 3", "value": 3, "disabled": True},
            ],
            value=[1],
            id="checklist-input",
        ),
    ]
    )
    table_header = [
    html.Thead(html.Tr([html.Td("Ip Address"), html.Td("Projects"), html.Td("Actions")]))
    ]
    stackedButtons = dbc.Stack(
            [
               dbc.Button("Accept", color="primary", className="me-1 w-10"),
                dbc.Button("Reject All", color="secondary", className="me-1")
            ],
            gap=3,
        ),
    row1 = html.Tr([html.Td("Project 1"), html.Td(checklist), html.Td(stackedButtons, style={'width': '10px'})])
    row2 = html.Tr([html.Td("Project 2"), html.Td(checklist), html.Td(dbc.Button("Acknowledge", color="secondary", className="me-1 w-10"), style={'width': '10px'})])
    table_body = [html.Tbody([row1, row2])]

    return dbc.Table(table_header + table_body, bordered=True)

def generateSyncRequestCard():
   
   return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("fileImage.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "80px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Sync Projects", style={"font-size": "30px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px',"margin-top" : "0%"}),
                        html.Br(),
                        createTable(),
                        dbc.Button("Return to Sync Menue", color="primary",href = "/syncMenue", className="position-absolute bottom-0 end-0 m-3")
                        ],
                ),
                dbc.Col(width=1)
            ],
        
        ),style={"height": 500, "width": 900,},className="mx-auto"
       
    )
)






layout = html.Div([
    dbc.Container([
       generateSyncRequestCard()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])