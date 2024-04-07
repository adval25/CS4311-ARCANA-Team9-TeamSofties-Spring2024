import dash
import dash_bootstrap_components as dbc
from dash import html,callback,Input, Output, State
from . import eventNavbar
import eventManager
from datetime import datetime



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
                id="edit-event-page",
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
                                html.P("Edit Event", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("eventTimeStamp"),
                                        dbc.Input(type="date", id ="eventTimeStamp"),
                                        dbc.Row([
                                                    dbc.Col(dbc.Input(id='nodehour', type="number", min=0, max=24, placeholder='Hour' ,style={"margin-bottom": "10px"}), width=3),
                                                    dbc.Col(dbc.Input(id='nodeminute', type='number', min=0, max=60, placeholder='Minute',style={"margin-bottom": "10px"}), width=3),
                                                    dbc.Col(dbc.Input(id='nodesecond', type='number', min=0, max=59, placeholder='Second', style={"margin-bottom": "10px"}), width=3)
                                                ])
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("malformed"),
                                        dbc.Checkbox(id="malformedInputs")
                                    ], width = 3
                                    ),
                                    
                                ], className="g-3",
                                ),
                                dbc.Col(
                                [
                                    html.P("Initials"),
                                    dbc.Input(type="text", placeholder="|||", id = "intialsInputs"),
                                ], width =3 
                                  
                                  ),
                        
                                
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
                                        html.P("eventLocation"),
                                        dbc.Input(type="posture", id = "eventLocation"), 
                                          
                                    ], width = 3
                                    ),
                                    
                                ],  className="g-3", 
                                ),
                                
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
                                        dbc.Input(type="text", placeholder="0.0.0.1", id = "targetHostInputs"), 
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
                                    dbc.Button("Cancel", color="secondary", href = "/displayEvents"),
                                    dbc.Button("create",  id="create-button",color="primary"),
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
    html.Div(id = "dummy-divAddSend"),
       eventNavbar.eventSidebar,
       generateCreateEvent(),
    ], 
    fluid=True, 
    style={"backgroundColor": "#D3D3D3", "margin": "auto", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ]
)


@callback(
    Output('location', 'href'),  #changes the location of the page
    [Input('create-button', 'n_clicks')],
    [
        State('selected-project-store', 'data'),
        State('eventTimeStamp', 'value'),
        State('nodehour', 'value'),
        State('nodeminute', 'value'),
        State('nodesecond', 'value'),
        State('malformedInputs', 'value'),
        State('intialsInputs', 'value'),
        State('vectorIdInputs', 'value'),
        State('sourceHostInputs', 'value'),
        State('targetHostInputs', 'value'),
        State('teamInputs','value'),
        State('descriptionInputs','value'),
        State('eventLocation', 'value')

    ]
)

def handleEditButtonClick(n_clicks,projectId,eventDate,nodehour,nodeminute,nodesecond, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation):
    if n_clicks:
        eventDateTime = datetime.strptime(f"{eventDate} {nodehour}:{nodeminute}:{nodesecond}", '%Y-%m-%d %H:%M:%S') #date passes back as YMD we need it as MDY
        eventTimeStamp = eventDateTime.strftime('%m/%d/%Y %H:%M:%S')
        event = eventManager.createEvent(eventTimeStamp, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,"")
        eventManager.addEventToProject(projectId,event)
        return "/displayEvents" #url that is redirected too