import dash
import dash_bootstrap_components as dbc
from dash import html,callback,Input, Output, State,dcc
import dash_ag_grid as dag
import projectManager
import os

dash.register_page(__name__, path='/manageProjects')

modal = html.Div(
    [
        dbc.Button("+ Create Project", color="primary", style={'display': 'inline-block'} , className="position-absolute top-0 end-0 m-3", id = "openProjectButton", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create Project")),
                dbc.ModalBody(
                    [
                        html.P("Project Name"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Project Name", placeholder="Project Name", id = "projectName" )),width = 12),)
                        ),
                        html.Br(),
                        html.P("Log Location"),
                        dcc.Dropdown(
                            id="logDirectory",
                            options=[],
                            placeholder="Select a log file",
                        ),
                        html.Br(),
                        html.P("Initials"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Initials", placeholder="III", id = "analystInitals")),width = 6),)
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="close", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Create Project", size = "lg", color="primary", id="createProject", className="ms-auto",n_clicks=0)),
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
                        html.P("Are you sure you want to delete Project D?", style={"font-size": "40px", "margin-left": "10px", 'display': 'inline-block'}, id = "deleteMessage"),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Button("Delete", size="lg", color="primary", id="deleteProject", className="ms-auto", n_clicks=0),
                                    width={"size": 6, "order": 2}  # Positions in the opposite corner
                                ),
                                dbc.Col(
                                    dbc.Button("Cancel", size="lg", color="secondary", id="closemodal_3", className="me-auto", n_clicks=0),
                                    width={"size": 6, "order": 1}  # Positions in the opposite corner
                                ),
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
                dbc.Button("Open Project", color="primary",id = "openProject"),
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
    projectDict = projectManager.getProjectDict()
    projectList = projectManager.projectObjectListToName(projectDict) #filtering so the table can be displayed
    columnDefs = [{"field": i} for i in ["projectName"]]
    return dag.AgGrid(
            id="row-selection-selected-rows",
            columnDefs=columnDefs,
            rowData=projectList,
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
            persistence=True,        
            persisted_props=["data"], 
        )



@callback(
    [Output('selected-project-store', 'data', allow_duplicate=True)],
    [Input("row-selection-selected-rows", "selectedRows")],
    [State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def output_selected_rows(selected_rows,current_data):
    if selected_rows is None:
        raise dash.exceptions.PreventUpdate
    else:
        selectedProject = [f"{project['_id']}" for project in selected_rows]
        return (f"{'s' if len(selected_rows) > 1 else ''}{', '.join(selectedProject)}",)

def generateManageProjectCard():
   return html.Div(
    dbc.Card(
        
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col([
                        dbc.Col([
                        html.Img(
                        src=dash.get_asset_url("fileImage.png"),
                        className="img-fluid rounded-start",
                        style={"width": "90px", "height": "90px","margin-right": 0, "margin-bottom" : "0%", "padding-top" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Manage Projects", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        ]),
                        modal,
                        modal_3,
                        modal_4,
                        html.Br(),
                        createTable(),
                        html.A(html.Button('Refresh Data'),href='/manageProjects'),
                        html.P(id='placeholder')
                ]
                ),
                dbc.Col(width=1)
            ],
        
        ), style={"height": "42vw", "width": "90vw",},className="mx-auto"
        
       
    )
)

@callback(
    [Output("modal", "is_open"),Output('location', 'href',allow_duplicate=True),Output('NoLog', 'displayed')],
    [Input("openProjectButton", "n_clicks"), Input("close", "n_clicks"),Input('createProject', 'n_clicks')],
    [
        State("modal", "is_open"),
        State('projectName', 'value'),
        State('analystInitals', 'value'),
        State('logDirectory', 'value'),
    ],
     prevent_initial_call=True
)
def toggle_modal(n1, n2, n3, is_open,projectName, analystInitals,logDirectory):
    if n1 or n2:
        if n3:
           if logDirectory == None:
               return dash.no_update,dash.no_update,True
           else:
            projectManager.createProject(projectName,analystInitals,"../logRepository/"+logDirectory)
            return not is_open,"/manageProjects",dash.no_update
        return not is_open, dash.no_update,dash.no_update
    return is_open, dash.no_update,dash.no_update

@callback(
    [Output("modal_3", "is_open", allow_duplicate=True), Output("deleteMessage", "children")],
    [Input("open modal_3", "n_clicks"), Input("closemodal_3", "n_clicks")],
    [State("modal_3", "is_open"), State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def toggle_modal_3(n1, n2, is_open,selectedProect):
    if (n1 or n2) and (selectedProect != None and selectedProect != {}):
        print(selectedProect)
        return not is_open, [html.P("Are you sure you want to delete " + projectManager.getProjectName(selectedProect) + "?", style={"font-size": "15px", "margin-left": "10px", 'display': 'inline-block'}, id = "deleteMessage"),html.Br(),]
    return is_open, html.P("TEST", style={"font-size": "40px", "margin-left": "10px", 'display': 'inline-block'}, id = "deleteMessage")

@callback(
      [Output('selected-project-store', 'data', allow_duplicate=True),Output("modal_3", "is_open", allow_duplicate=True),Output('location', 'href',allow_duplicate=True),],
      Input("deleteProject", "n_clicks"),
      State('selected-project-store', 'data'),
      prevent_initial_call=True
)
def deleteProject(n_click,selectedProject):
    if n_click:
        projectManager.deleteProject(selectedProject)
        return {},False,"/manageProjects"
    raise dash.exceptions.PreventUpdate

@callback(
        Output('location', 'href',allow_duplicate=True),
        Input("openProject","n_clicks"),
        State('selected-project-store', 'data'),
        prevent_initial_call=True
)
def checkIfProjectExists(n_clicks,selectedProject):
    if n_clicks:
        if projectManager.checkIfProjectExists(selectedProject):
            print("THING " + selectedProject)
            return "/displayEvents"
    raise dash.exceptions.PreventUpdate

def serveLayout():
    return html.Div([
        dbc.Container([
            dcc.ConfirmDialog(id='NoLog',message='NO LOG INPUT',),
            html.Div(id ="dummyDivManageProject"),
            html.Div(id ="dummyDivRedirectProject"),
        generateManageProjectCard(),
        ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ])

def get_log_files():
    log_directory = '../logRepository'
    return [f for f in os.listdir(log_directory)]


@callback(
    Output("logDirectory", "options"),
    [Input("modal", "is_open")],
    prevent_initial_call=True
)
def update_log_files_dropdown(is_open):
    if is_open:
        log_files = get_log_files()
        print(log_files)
        return [{'label': f, 'value': f} for f in log_files]
    raise dash.exceptions.PreventUpdate

layout = serveLayout


