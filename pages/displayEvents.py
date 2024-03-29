import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html,callback,State
from .  import eventNavbar
import dataBaseCommunicator
import dash_ag_grid as dag
import eventManager


dash.register_page(__name__, path='/displayEvents')
sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

def dropDownMaker(menueId,menueContent,marginRight):
    return dbc.Select(
    id=menueId,
    options=menueContent,
    size="md",
    style={'display': 'inline-block',"width" : "8rem","margin-right" : marginRight})

def generatedisplayEventCard(): 
    return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="page-content",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("syncIcon.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Events", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),  
                    ],
                ),
                html.Br(),
                 dbc.Row(
                dbc.Col([html.P("Sort:",style={'display': 'inline-block'}),
                         dropDownMaker("sortDropDown",sortDropDown,"4rem"),
                         dbc.Switch(id="standalone-switch",label="Filter",value=False,style={'display': 'inline-block'}),
                         dbc.Input(id="input", placeholder="Type something...", type="text",size="md",style={'display': 'inline-block',"width" : "30rem","margin-left" : "20rem"}),
                        dropDownMaker("logicDropDown",logicDropDown,"0rem"),
                         dbc.Button("Search", color="primary", className="me-1",size="md"),
                         ])
                         ),
                  html.Div(id='eventtableOutput'),
                  html.A(html.Button('Refresh Data'),href='/displayEvents'),
                  html.Div(
                        [
                            dbc.Button("+ Create Event", color="primary",href = "/addEvent"),
                            dbc.Button("Edit Event", color="primary",href = "/editEvent"),
                            dbc.Button("Delete Event", color="primary",href = "/displayEvents",id = "deleteButton"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                        ), 

            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)

@callback(
    Output('dummyDivEventManager', 'children'),
    [Input('deleteButton', 'n_clicks')],
     [State("SelectedRowEvent", "selectedRows")],
    [State('selected-project-store', 'data')]
)
def deleteEvent(n_clicks,activeEventInformation,activeProjectId):
    if n_clicks:
        eventManager.deleteEvent(activeEventInformation[0]["_id"],activeProjectId)
    return None

@callback(
    Output('eventtableOutput', 'children'),
    [Input('dummy-div', 'children')],  # Trigger callback on page load
    [State('selected-project-store', 'data')]
)
def display_store_data(dummyValue, storeData):
    if storeData != None:
        return createEvenTable(storeData) #loads the correct events from the project
    else:
        return ""

def createEvenTable(projectId):
    print(projectId)
    Selectedproject = dataBaseCommunicator.getProjectFromDb(projectId)
    columnDefsNames = ['malformed', 'eventTimeStamp', 'analystInitals', 'eventTeam', 'eventDescription', 'eventLocation', 'eventSourceHost', 'eventTargetHost', 'eventVectorId', 'eventDataSource', '_id']
    columnDefs = [{"field": i} for i in columnDefsNames]
    return dag.AgGrid(
            id="SelectedRowEvent",
            columnDefs=columnDefs,
            rowData= eventManager.eventListToDictionary(Selectedproject.getEventCollection()),
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
            persistence=True,        
            persisted_props=["data"], 
        )


@callback(
    Output('dummy-div', 'children'),
    [Input('selected-project-store', 'data')]
)
def trigger_page_load(data):
    return 'Page Loaded'  # Update the hidden div to trigger the page load

@callback(
    [Output('eventStore', 'data')],
    [Input("SelectedRowEvent", "selectedRows")],
    [State('eventStore', 'data')]
)
def output_selected_rows(selected_rows,current_data): #grabs the eventId of the selected Event for saving purposes
    if selected_rows is None:
        return (current_data,)
    else:
        selectedEvent = [f"{event['_id']}" for event in selected_rows]
        print( (f"{'s' if len(selected_rows) > 1 else ''}{', '.join(selectedEvent)}",))
        return (f"{'s' if len(selected_rows) > 1 else ''}{', '.join(selectedEvent)}",)

@callback(
    Output('dummyDivEventManagerReload', 'children'),
    [Input('selected-project-store', 'data')]
)
def trigger_page_load(data):
    return 'Page Loaded'

def displayEventLayout():
    return html.Div([
    html.Div([dag.AgGrid(id ="SelectedRowEvent"),],id='dummy-div', style={'display': 'none'}), #this is here to prevent an error that selectedRow does not exist
    html.Br(),
    eventNavbar.eventSidebar,
    dbc.Container([
        html.Div(id ="dummyDivEventManager"),
        html.Div(id ="dummyDivEventManagerReload"),
       generatedisplayEventCard(),
      html.Div(id='store-data-display'),

    ], fluid=True,  className="mx-auto") 
])



layout = displayEventLayout