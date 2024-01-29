import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd

dash.register_page(__name__, path='/createEvent')

def generateCreateEvent():
    team_options = ["White", "Red", "Blue"]
    event_node_icons_options = {
        "White": "eventNodeIcon.png",
        "Red": "eventNodeIcon.png",
        "Blue": "eventNodeIcon.png",
    }
    
    return html.Div(
        dbc.Card(
            dbc.Row(
                id="create-event-page",
                children=[
                    dbc.Col(width=1), 
                    dbc.Col(
                        html.Div(
                            children=[
                                html.Img(
                                    src=dash.get_asset_url("activityLogs.png"),
                                    className="img-fluid rounded-start",
                                    style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"},
                                ), 
                                html.P("Create Event", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("Date"),
                                        dbc.Input(type="date", placeholder="mm/dd/yyyy"),   
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("Time"),
                                        dbc.Input(type="time", placeholder="hh:mm:ss"),   
                                    ], width = 3
                                    ),
                                    
                                ], className="g-3",
                                ),
                                
                                html.P("Initials"),
                                dbc.Input(type="text", placeholder="|||"),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("Team*"),
                                        dbc.Select(
                                            options=[{"label": i, "value": i} for i in team_options],
                                            value=team_options[0],
                                        ), 
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("Posture"),
                                        dbc.Input(type="posture"),   
                                    ], width = 3
                                    ),
                                    
                                ],  className="g-3", 
                                ),
                                 
                                html.P("Location"),
                                dbc.Input(type="text", placeholder="Location"),
                                
                                html.P("Vector ID"),
                                dbc.Input(type="text", placeholder="Vector ID"),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                       html.P("Source Host"),
                                        dbc.Input(type="text", placeholder="0.0.0.0"),
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [   
                                        html.P("Target Host(s)"),
                                        dbc.Input(type="text", placeholder="0.0.0.0, 0.0.0.1"), 
                                    ], width = 3
                                    ),  
                                    
                                ],  className="g-3", 
                                ),
                                
                                html.P("Description*"),
                                dbc.Textarea(placeholder="Description", style={"height": "100px"},),
                                
                                html.P("Event Node Icon*"),
                                html.Img(
                                    src=dash.get_asset_url("eventNodeIcon.png"),
                                    className="img-fluid rounded-start",
                                    style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"},
                                ), 
                                html.P("White Team Activity"),
                                # dbc.Select(
                                #     options=[{"label": i, "value": i} for i in event_node_icons_options.keys()],
                                #     value=list(event_node_icons_options.keys())[0],
                                # ),
                                
                                dbc.Checkbox(
                                    id="standalone-checkbox",
                                    label="Auto-create edges",
                                    value=False,
                                ),
                                
                                html.Div(
                                [
                                    dbc.Button("Cancel", color="secondary"),
                                    dbc.Button("Create", color="primary"),
                                ],
                                className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                                ), 
                                dbc.Col(width=1), 
                            
                            ],                             
                            style={"display": "flex", "flexDirection": "column", "alignItems": "center", "justifyContent": "center", "height": "100%"}  

                        ),
                    ),    
                ],                   
            ), 
            style={"margin": "auto", "width": "80%", "maxWidth": "800px"}  

        ),
    )

layout = html.Div(
    [
    dbc.Container(
    [
       generateCreateEvent()
    ], 
    fluid=True, 
    style={"backgroundColor": "#D3D3D3", "margin": "auto", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ]
)