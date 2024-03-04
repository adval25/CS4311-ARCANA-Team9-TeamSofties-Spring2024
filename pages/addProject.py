import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import callback,Output,Input,State
import dataBaseCommunicator
import logIngestor


dash.register_page(__name__, path='/addProject')

def generateCreateEvent():
    return html.Div(
        dbc.Card(
            dbc.Row(
                id="createProjectPage",
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
                                html.P("Create Project", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                                
                                dbc.Row(
                                [
                                    dbc.Col(
                                    [
                                        html.P("Project Name"),
                                        dbc.Input(type="text", placeholder="mm/dd/yyyy", id = "projectName"),   
                                    ], width =3 
                                    ),
                                    dbc.Col(
                                    [
                                        html.P("Initals"),
                                        dbc.Input(type="text", placeholder="|||" , id = "analystInitials"),   
                                    ], width = 3
                                    ),
                                    
                                ], className="g-3",
                                ),
                                html.P("logDirectory"),
                                dbc.Input(type="text", placeholder="", id = "logDirectory"),
                                html.Div(
                                [
                                    dbc.Button("Cancel", color="secondary",),
                                    dbc.Button("Create",  id="create-button",color="primary" , href = "/manageProjects"),
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
           style={"height": "42vw", "width": "90vw",},className="mx-auto"

        ),
    )



@callback(
    Output('dummyDivProject', 'children'),  # Update some output div with the result of your function
    [Input('create-button', 'n_clicks')],
    [
        State('projectName', 'value'),
        State('analystInitials', 'value'),
        State('logDirectory', 'value'),
    ]
)

def handleCreateButtonClick(n_clicks, projectName, analystInitials,logDirectory):
    if n_clicks:
        newProject = dataBaseCommunicator.createProject(projectName,analystInitials)
        newEventDic = logIngestor.eventDataListToEventList(logIngestor.csvsToEventDataList(logIngestor.getCsvPaths(logIngestor.get_wlogs())))
        for event in newEventDic:
            print(event._id)
        dataBaseCommunicator.addEventListToProject(newProject,newEventDic)
        print('hello')

def addProjectLayout(): 
    return html.Div(
        [
        dbc.Container(
        [
        generateCreateEvent(),
        html.Div(id="dummyDivProject")
        ], 
        fluid=True, 
        style={"backgroundColor": "#D3D3D3", "margin": "auto", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
        ]
    )

layout = addProjectLayout