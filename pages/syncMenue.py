import dash
import dash_bootstrap_components as dbc
from dash import dcc,callback,Output,State,Input
from dash import html
import dash_ag_grid as dag
import projectManager
import dataBaseCommunicator
dash.register_page(__name__, path='/syncMenue')
modal = html.Div(
    [
        dbc.Button("Connect To remote Db", color="primary", style={'display': 'inline-block'} , className="position-absolute top-0 end-0 m-3", id = "openConnectModal", n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Get Projects from Ip")),
                dbc.ModalBody(
                    [
                        html.P("Enter Ip Adress"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Project Name", placeholder="0.0.0.0", id = "hostAdress" )),width = 12),)
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="closeConnect", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Connect", size = "lg", color="primary", id="connect", className="ms-auto",n_clicks=0)),
                            ]
                        ),
                    ],
                ),
                dbc.ModalFooter(
                    [
                        
                    ]
                ),
            ],
            id = "ipdConnectInput",
            is_open = False,
        ),
    ]
    
)

def createTable(projectList):
    columnDefs = [{"field": i} for i in ["projectName"]]
    return dag.AgGrid(
            id="SyncTable",
            columnDefs=columnDefs,
            rowData=projectList,
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
            persistence=True,        
            persisted_props=["data"], 
        )



@callback(
    [Output('selectedSync', 'data')],
    [Input("SyncTable", "selectedRows")],
    [State('selectedSync', 'data')]
)
def output_selected_rows(selected_rows,current_data):
    if selected_rows is None:
        return (current_data,)
    else:
        selectedProject = [f"{project['_id']}" for project in selected_rows]
        return (f"{'s' if len(selected_rows) > 1 else ''}{', '.join(selectedProject)}",)

def generateManageProjectCard():
   return html.Div(
    dbc.Card(
        
        dbc.Row(
            id="Synccontrol-card",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col([
                        dbc.Col([
                        html.Img(
                        src=dash.get_asset_url("fileImage.png"),
                        className="img-fluid rounded-start",
                        style={"width": "90px", "height": "90px","margin-right": 0, "margin-bottom" : "0%", "padding-top" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Sync Projects", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        ]),
                        modal,
                        html.Br(),
                        html.Div(id = "syncTable",children =[createTable([])]),
                        html.A(html.Button('Refresh Data'),href='/manageProjects'),
                        html.Br(),
                        html.Br(),
                        html.Div(
                        [
                            dbc.Button("Add Project +", color="primary",id = "addProject"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                    ), 
                html.P(id='placeholder')
                ]
                ),
                dbc.Col(width=1)
            ],
        
        ), style={"height": "42vw", "width": "90vw",},className="mx-auto"
        
       
    )
)

@callback(
    [Output("ipdConnectInput", "is_open"),Output("syncTable","children"),Output("hostName","data")],
    [Input("openConnectModal", "n_clicks"), Input("closeConnect", "n_clicks"),Input('connect', 'n_clicks')],
    [
        State("ipdConnectInput", "is_open"),
        State('hostAdress', 'value'),
        ],
)
def toggle_modal(n1, n2, n3, is_open,hostAdress):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if n1 or n2 or n3:
        if button_id == "connect":
            projectList = dataBaseCommunicator.getAllProjectsFromSeprateDb("projectsDB2",hostAdress)
            projectList = projectManager.projectObjectListToName(projectList) #filtering so the table can be displayed
            return not is_open,createTable(projectList),hostAdress
        return not is_open,dash.no_update,dash.no_update
    return not is_open,dash.no_update,dash.no_update

@callback(
    Output("alert-auto", "is_open"),
    [Input("addProject", "n_clicks"),Input("hostName", "data")],
    [State("alert-auto", "is_open")],
    [State('selectedSync', 'data')]
)
def toggle_alert(n,hostName,is_open,selectedSync):
    if n:
        if selectedSync != None and selectedSync != {}:
            project = dataBaseCommunicator.getProjectByIDFromSeprateDb("projectsDB2",hostName,selectedSync)
            dataBaseCommunicator.addProjectFromSerpateDb(project)
            return not is_open
        return dash.no_update
    return dash.no_update

def serveLayout():
    return html.Div([
        html.Div(id="hostname", style={"display": "none"}),
        dbc.Container([
              dbc.Alert(
                    "ADDED PROJECT TO LOCAL DATABASE",
                    id="alert-auto",
                    is_open=False,
                    duration=4000,
                ),
        generateManageProjectCard(),
        ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
    ])
layout = serveLayout


