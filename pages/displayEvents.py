import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,callback,dash_table,State
from .  import eventNavbar
import pandas as pd
import dataBaseCommunicator
from dataBaseCommunicator import dataBaseCleint


dash.register_page(__name__, path='/displayEvents')
eventDic = dataBaseCommunicator.getEventDictionaryFromDb(dataBaseCommunicator.getAllProjectsFromDb(dataBaseCleint)[0]["_id"],dataBaseCleint)
eventDic = [{key: value for key, value in d.items() if key != "_id"} for d in eventDic]

sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

df = pd.DataFrame(eventDic)


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
                dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],style_table={'height': '300px', 'overflowY': 'auto'}),
                  html.Div(
                        [
                            dbc.Button("+ Create Event", color="primary",href = "/addEvent"),
                            dbc.Button("Edit Event", color="primary",href = "/addEvent"),
                            dbc.Button("Delete Event", color="primary",href = "#"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                        ), 

            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)

@callback(
    Output('store-data-display', 'children'),
    [Input('dummy-div', 'children')],  # Trigger callback on page load
    [State('selected-project-store', 'data')]
)
def display_store_data(dummy_value, store_data):
    return store_data or "No data available"  # R

@callback(
    Output('dummy-div', 'children'),
    [Input('selected-project-store', 'data')]
)
def trigger_page_load(data):
    return 'Page Loaded'  # Update the hidden div to trigger the page load

layout = html.Div([
    html.Div(id='dummy-div', style={'display': 'none'}),
    html.Br(),
    eventNavbar.eventSidebar,
    dbc.Container([
       generatedisplayEventCard(),
      html.Div(id='store-data-display'),

    ], fluid=True,  className="mx-auto") 
])

