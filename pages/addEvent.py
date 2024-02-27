import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table,callback
from dash import html
from . import eventNavbar
from dash import Input, Output, State
from event import Event
import dataBaseCommunicator
from dataBaseCommunicator import dataBaseCleint


dash.register_page(__name__, path='/addEvent')

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
                                        dbc.Input(type="date", placeholder="mm/dd/yyyy", id = "dateInputs"),   
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("Time"),
                                        dbc.Input(type="time", placeholder="hh:mm:ss" , id = "timeInputs"),   
                                    ], width = 3
                                    ),
                                    
                                ], className="g-3",
                                ),
                                
                                html.P("Initials"),
                                dbc.Input(type="text", placeholder="|||", id = "intialsInputs"),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("Team*"),
                                        dbc.Select(
                                            options=[{"label": i, "value": i} for i in team_options],
                                            value=team_options[0],
                                            id = "teamInputs",
                                        ), 
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("Posture"),
                                        dbc.Input(type="posture", id = "postureInputs"), 
                                          
                                    ], width = 3
                                    ),
                                    
                                ],  className="g-3", 
                                ),
                                 
                                html.P("Location"),
                                dbc.Input(type="text", placeholder="Location", id = "locationInputs"),
                                
                                html.P("Vector ID"),
                                dbc.Input(type="text", placeholder="Vector ID", id = "vectorIdInputs"),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                       html.P("Source Host"),
                                        dbc.Input(type="text", placeholder="0.0.0.0", id = "sourceHostInputs"),
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [   
                                        html.P("Target Host(s)"),
                                        dbc.Input(type="text", placeholder="0.0.0.0, 0.0.0.1", id = "targetHostInputs"), 
                                    ], width = 3
                                    ),  
                                    
                                ],  className="g-3", 
                                ),
                                
                                html.P("Description*"),
                                dbc.Textarea(placeholder="Description", style={"height": "100px"}, id ="descriptionInputs"),
                                
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
                                    dbc.Button("Create",  id="create-button",color="primary"),
                                ],
                                className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                                ), 
                                dbc.Col(width=1), 
                            
                            ],                             
                            style={"display": "flex", "flexDirection": "column", "height": "100%"}  

                        ),
                    ),    
                ],                   
            ), 
            style={"margin-left": "18rem","margin-right": "2rem","margin-top": "8rem","padding": "2rem 1rem","height" : "65rem"}

        ),
    )

layout = html.Div(
    [
    dbc.Container(
    [
       eventNavbar.eventSidebar,
       generateCreateEvent(),
       html.Div(id="dummyDiv")
    ], 
    fluid=True, 
    style={"backgroundColor": "#D3D3D3", "margin": "auto", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ]
)


@callback(
    Output('dummyDiv', 'children'),  # Update some output div with the result of your function
    [Input('create-button', 'n_clicks')],
    [
        State('dateInputs', 'value'),
        State('timeInputs', 'value'),
        State('intialsInputs', 'value'),
        State('locationInputs', 'value'),
        State('vectorIdInputs', 'value'),
        State('sourceHostInputs', 'value'),
        State('targetHostInputs', 'value'),
        State('teamInputs','value'),
        State('postureInputs','value'),
        State('descriptionInputs','value')
    ]
)

def handle_create_button_click(n_clicks, date_value, time_value,intialsInput,locationInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,postureInput,descriptionInput):
    if n_clicks:
        print_input_values(date_value, time_value,intialsInput,locationInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,postureInput,descriptionInput)

def print_input_values(date_value, time_value, intialsInput, locationInput, vectorIdInput, sourceHostInput, targetHostInput, teamInput,postureInput,descriptionInput):
    event = Event(eventTimeStamp = str(date_value),
                        analystInitals = str(intialsInput),
                        eventTeam = str(teamInput),
                        eventDescription =str(descriptionInput), 
                        eventLocation = str(locationInput),
                        eventSourceHost = str(sourceHostInput),
                        eventTargetHost = str(targetHostInput),
                        eventVectorId = str(vectorIdInput),
                        eventDataSource = str(sourceHostInput),
                        )
    project = dataBaseCommunicator.getProjectFromDb(dataBaseCommunicator.getAllProjectsFromDb(dataBaseCleint)[0]["_id"])
    print(project)
    dataBaseCommunicator.addEventToProject(project,event)
    return 0
  