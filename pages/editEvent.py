import dash
import dash_bootstrap_components as dbc
from dash import html,callback,Input, Output, State
from . import eventNavbar
import eventManager
from datetime import datetime
import nodeIconDropDown
import nodeManager
import graphManager

dash.register_page(__name__, path='/editEvent')

def generateEditEvent(eventDic,previousEvent = None):
    team_options = ["White", "Red", "Blue"]
    event_node_icons_options = {
        "White": "eventNodeIcon.png",
        "Red": "eventNodeIcon.png",
        "Blue": "eventNodeIcon.png",
    }
    eventDate = None
    eventHour = None
    eventMinute = None
    eventSecond = None
    if previousEvent != None:
        eventTime = previousEvent.converTimeStampToDateTime()
        eventDate = eventTime.date() if eventTime else None
        eventHour = eventTime.hour if eventTime else None
        eventMinute = eventTime.minute if eventTime else None
        eventSecond = eventTime.second if eventTime else None

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
                                        dbc.Input(type="date", id ="eventTimeStamp",value=eventDate),
                                        dbc.Row([
                                                    dbc.Col(dbc.Input(id='eventhour', type="number", min=0, max=24, placeholder='Hour',value=eventHour ,style={"margin-bottom": "10px"}), width=3),
                                                    dbc.Col(dbc.Input(id='eventminute', type='number', min=0, max=60, placeholder='Minute',value=eventMinute ,style={"margin-bottom": "10px"}), width=3),
                                                    dbc.Col(dbc.Input(id='eventsecond', type='number', min=0, max=59, placeholder='Second',value=eventSecond, style={"margin-bottom": "10px"}), width=3)
                                                ])
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("malformed"),
                                        dbc.Checkbox(id="malformedInputs", value=eventDic["malformed"])
                                    ], width = 3
                                    ),
                                    
                                ], className="g-3",
                                ),
                                dbc.Col(
                                [
                                    html.P("Initials"),
                                    dbc.Input(type="text", placeholder="|||", id = "intialsInputs",value = eventDic["analystInitals"]),
                                ], width =3 
                                  
                                  ),
                        
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("Team*"),
                                        dbc.Select(
                                            options=[{"label": i, "value": i} for i in team_options],
                                            value=eventDic["eventTeam"],
                                            id = "teamInputs",
                                        ), 
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("eventLocation"),
                                        dbc.Input(type="posture", id = "eventLocation", value = eventDic["eventLocation"]), 
                                          
                                    ], width = 3
                                    ),
                                    
                                ],  className="g-3", 
                                ),
                                
                                html.P("Vector ID"),
                                dbc.Input(type="text", placeholder="Vector ID", id = "vectorIdInputs", value = eventDic["eventVectorId"]),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                       html.P("Source Host"),
                                        dbc.Input(type="text", placeholder="0.0.0.0", id = "sourceHostInputs", value = eventDic["eventSourceHost"]),
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [   
                                        html.P("Target Host(s)"),
                                        dbc.Input(type="text", placeholder="0.0.0.0, 0.0.0.1", id = "targetHostInputs", value = eventDic["eventTargetHost"]), 
                                    ], width = 3
                                    ),  
                                    
                                ],  className="g-3", 
                                ),
                                
                                html.P("Description*"),
                                dbc.Textarea(placeholder="Description", style={"height": "100px"}, id ="descriptionInputs",value = eventDic["eventDescription"]),
                                
                                html.P("Event Node Icon*"),
                                nodeIconDropDown.nodeIconDropDownMaker('editEventIconDropDown'),
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
                                    dbc.Button("Edit",  id="edit-button",color="primary", href = "/displayEvents"),
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

@callback(
    [Output('editEventDiv', 'children'),Output('editEventIconDropDown','value')],
    [Input('dummy-divEdit', 'children')],  # Trigger callback on page load
    [State('eventStore', 'data')],
    [State('selected-project-store', 'data')]
)
def fillValuesForEditEvent(dummyValue, eventId,projectId):
    print(eventId)
    if eventId != None:
          previousEvent = eventManager.getEventFromProject(eventId,projectId)
          eventDic = previousEvent.eventToDictionary()
          return generateEditEvent(eventDic,previousEvent),eventDic['eventIcon']
    else:
        return "",None
temporaryDic = {'malformed': " ",'eventTimeStamp': "1/01/9999 1:01:01",'analystInitals': " ",'eventTeam': " ",'eventDescription':" ",'eventLocation': " ",'eventSourceHost': " ",'eventTargetHost': " ",'eventVectorId': " ",'eventDataSource': " ",'_id': " "} 
layout = html.Div(
    [
    dbc.Container(
    [
    html.Div(id = "dummy-divEdit"),
    html.Div([generateEditEvent(temporaryDic)],id = "dummy-divEditSend"), #stops an error from a callback not being able to find values
       eventNavbar.eventSidebar,
       html.Div(id = "editEventDiv"),
       html.Div(id="dummyDiv")
    ], 
    fluid=True, 
    style={"backgroundColor": "#D3D3D3", "margin": "auto", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ]
)


@callback(
    Output('dummy-divEditSend', 'children'),  # Update some output div with the result of your function
    [Input('edit-button', 'n_clicks')],
    [
        State('eventStore', 'data'),
        State('selected-project-store', 'data'),
        State('eventTimeStamp', 'value'),
        State('eventhour', 'value'),
        State('eventminute', 'value'),
        State('eventsecond', 'value'),
        State('malformedInputs', 'value'),
        State('intialsInputs', 'value'),
        State('vectorIdInputs', 'value'),
        State('sourceHostInputs', 'value'),
        State('targetHostInputs', 'value'),
        State('teamInputs','value'),
        State('descriptionInputs','value'),
        State('eventLocation', 'value'),
        State('editEventIconDropDown','value')

    ]
)

def handleEditButtonClick(n_clicks,eventId,projectId,eventDate,eventhour,eventminute,eventsecond, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,eventIcon):
    if n_clicks:
        eventDateTime = datetime.strptime(f"{eventDate} {eventhour}:{eventminute}:{eventsecond}", '%Y-%m-%d %H:%M:%S')
        eventTimeStamp = eventDateTime.strftime('%m/%d/%Y %H:%M:%S')
        previousEvent = eventManager.getEventFromProject(eventId,projectId)
        if eventIcon == None:
            eventIcon =""
        event = eventManager.createEvent(eventTimeStamp, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,previousEvent.getDataSource(),eventIcon,eventId)
        eventManager.addEventToProject(projectId,event)
        node = nodeManager.createNode(projectId,event)
        graphManager.addNodeToGraph(node,projectId)
        return ""
