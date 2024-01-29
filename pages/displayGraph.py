import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html,callback,dash_table
from .  import eventNavbar
import pandas as pd
import dash_cytoscape as cyto



dash.register_page(__name__, path='/displayGraph')

sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


def dropDownMaker(menueId,menueContent,marginRight):
    return dbc.Select(
    id=menueId,
    options=menueContent,
    size="md",
    style={'display': 'inline-block',"width" : "8rem","margin-right" : marginRight})

def generateSyncCard(): 
    return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="page-content",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                 dbc.Row(
                dbc.Col([html.P("Sort:",style={'display': 'inline-block'}),
                         dropDownMaker("sortDropDown",sortDropDown,"4rem"),
                         dbc.Switch(id="standalone-switch",label="Filter",value=False,style={'display': 'inline-block'}),
                         dbc.Input(id="input", placeholder="Type something...", type="text",size="md",style={'display': 'inline-block',"width" : "30rem","margin-left" : "15rem"}),
                         dbc.Button("Export Event Graph", color="primary", className="me-1",size="md"),
                         dbc.Button("Import Event Graph", color="primary", className="me-1",size="md"),
                         ])
                         ),
                          html.Div([cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},elements=[{'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 75, 'y': 75}},{'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},{'data': {'source': 'one', 'target': 'two'}}])
])

            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)



layout = html.Div([
    html.Br(),
    eventNavbar.eventSidebar,
    generateSyncCard()
])

