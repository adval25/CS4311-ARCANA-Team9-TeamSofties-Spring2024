import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd
from dash import Input, Output, State


dash.register_page(__name__, path='/manageProjects')

modal = html.Div(
    [
        dbc.Button("+ Create Project", color="primary", style={'display': 'inline-block'} , className="position-absolute top-0 end-0 m-3", id = "open", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create Project")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ms-auto", n_clicks=0)
                ),
            ],
            id = "modal",
            is_open = False,
        ),
    ]
    
)

modal_2 = html.Div(
    [
        html.Div(
            [
                dbc.Button("Ingest Logs", color="primary",id = "open modal_2"),
                dbc.Button("Delete Project", color="primary",href = "#"),
                dbc.Button("Open Project", color="primary",href = "#"),
            ],
            className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
        ), 
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Ingest Logs")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close modal_2", className="ms-auto", n_clicks=0)
                ),
            ],
            id = "modal_2",
            is_open = False,
        ),
    ]
    
)

modal_3 = html.Div(
    [
        html.Div(
            [
                dbc.Button("Delete Project", color="primary",id = "open modal_3"),
                dbc.Button("Open Project", color="primary"),
            ],
            className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
        ), 
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Delete Project")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close modal_3", className="ms-auto", n_clicks=0)
                ),
            ],
            id = "modal_3",
            is_open = False,
        ),
    ]
    
)

modal_4 = html.Div(
    [
        html.Div(
            [
                dbc.Button("Open Project", color="primary",id = "open modal_4",href="/displayEvents"),
            ],
            className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
        ), 
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Open Project")),
                dbc.ModalBody("This is the content of the modal"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close modal_4", className="ms-auto", n_clicks=0)
                ),
            ],
            id = "modal_4",
            is_open = False,
        ),
    ]
    
)

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

                        modal,
                        modal_2,
                        modal_3,
                        modal_4,
                        html.Br(),
                        
                        createTable(),
                        html.Div(
                        [
                            #dbc.Button("Ingest Logs", color="primary",href = "#"),
                            #dbc.Button("Delete Project", color="primary",href = "#"),
                            #dbc.Button("Open Project", color="primary",href = "#"),
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


