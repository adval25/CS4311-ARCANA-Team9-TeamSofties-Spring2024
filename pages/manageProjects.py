import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table,callback
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
                dbc.ModalBody(
                    [
                        html.P("Project Name"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Project Name", placeholder="Project Name")),width = 12),)
                        ),
                        html.Br(),
                        html.P("Project Location"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Project Location", placeholder="Project Location")),width = 12),)
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Start Date")),
                                dbc.Col(html.P("End Date")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Start Date", placeholder="mm/dd/yyyy")))))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="End Date", placeholder="mm/dd/yyyy")))))),
                            ]
                        ),
                        html.Br(),
                        html.P("Initials"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Initials", placeholder="III")),width = 6),)
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="close", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Create Project", size = "lg", color="primary", id="create Project", className="ms-auto", n_clicks=0)),
                            ]
                        ),
                    ],
                ),
                dbc.ModalFooter(
                    [
                        
                    ]
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
                dbc.ModalBody(
                    [
                        html.P("Select a directory to ingest logs from."),
                        html.P("Log directory", style={"font-size": "20px",'display': 'inline-block'}),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Log Directory", placeholder="ex. /Location/folder"))))), width = 9),
                                dbc.Col(dbc.Button("Browse", color="primary",id = "Browse")),
                            ]
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="close modal_2", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Ingest Logs", size = "lg", color="primary", id="create Project", className="ms-auto", n_clicks=0)),
                            ]
                        ),
                    ]
                ),
                dbc.ModalFooter(),
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
                dbc.ModalHeader(),
                dbc.ModalBody(
                    [
                        html.P("Are you sure you want to delete Project D?", style={"font-size": "40px", "margin-left": "10px", 'display': 'inline-block'}),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="close modal_3", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Delete", size = "lg", color="primary", id="delete Project", className="ms-auto", n_clicks=0)),
                            ]
                        ),
                    ]
                ),
                dbc.ModalFooter(),
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

@callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("modal_2", "is_open"),
    [Input("open modal_2", "n_clicks"), Input("close modal_2", "n_clicks")],
    [State("modal_2", "is_open")],
)
def toggle_modal_2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("modal_3", "is_open"),
    [Input("open modal_3", "n_clicks"), Input("close modal_3", "n_clicks")],
    [State("modal_3", "is_open")],
)
def toggle_modal_3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output("modal_4", "is_open"),
    [Input("open modal_4", "n_clicks"), Input("close modal_4", "n_clicks")],
    [State("modal_4", "is_open")],
)
def toggle_modal_4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


layout = html.Div([
    dbc.Container([
       generateManageProjectCard()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])


