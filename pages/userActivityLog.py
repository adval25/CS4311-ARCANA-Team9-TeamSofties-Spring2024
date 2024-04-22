import dash
import dash_bootstrap_components as dbc
from dash import dash_table,Input,Output,State,callback
from dash import html
import loggerManager
import dash_ag_grid as dag



dash.register_page(__name__, path='/viewUserActivityLog')

def getUserLoggingData():
   user_activity_logger = loggerManager.getUserLogs()
   return [{"log_description": log} for log in user_activity_logger]

def createActivityTable():
    columnDefs = [{"field": "log_description"}]
    return dag.AgGrid(
            id="SyncTable",
            columnDefs=columnDefs,
            rowData=getUserLoggingData(),
            columnSize="sizeToFit",
            defaultColDef={"filter": True},
            dashGridOptions={"rowSelection": "multiple", "animateRows": False},
            persistence=True,        
            persisted_props=["data"], 
        )




def generateActivityLog():
   return html.Div(
    dbc.Card(
        
        dbc.Row(
            id="logTableControlCard",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col([
                        dbc.Col([
                        html.Img(
                        src=dash.get_asset_url("activityLogs.png"),
                        className="img-fluid rounded-start",
                        style={"width": "90px", "height": "90px","margin-right": 0, "margin-bottom" : "0%", "padding-top" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("user Activity Log", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        ]),
                        html.Br(),
                        html.Div(id = "syncTable",children =[createActivityTable()]),
                        html.A(html.Button('Refresh Data'),href='/viewUserActivityLog'),
                        html.Br(),
                        html.Br(),
                        html.Div(
                        [
                            dbc.Button("Clear Logs", color="primary",id = "clearLogsButton"),
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
    Output("clearLogsDiv", "children"),  # Output placeholder, can be any component
    [Input("clearLogsButton", "n_clicks")],  # Input trigger, listens for button clicks
)
def clearLogs(n_clicks):
    if n_clicks is not None:
        loggerManager.clearLogs()  
    else:
        return dash.no_update 

def userActivityLogLayout():
   return html.Div([
    dbc.Container([
       html.Div(id="clearLogsDiv"),
       generateActivityLog()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])

layout = userActivityLogLayout
