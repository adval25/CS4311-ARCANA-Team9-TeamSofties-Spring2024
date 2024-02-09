import dash
import dash_bootstrap_components as dbc
from dash import dcc,dash_table
from dash import html
from collections import OrderedDict
import pandas as pd



dash.register_page(__name__, path='/viewUserActivityLog')

data = OrderedDict(
    [
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)

def generateActivityLog():
   
   return html.Div(
    dbc.Card(
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margins
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("activityLogs.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("User Activity Log", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),
                        dbc.Button("Reload", color="primary", className="me-1",style={"margin-left": 20,"margin-top": -5,"margin-bottom": 0}),
                        html.Br(),
                        html.P("Select a color scheme if you would like to apply the color scheme permantly click save"),
                        html.Br(),
                        dbc.Row(
                           [
                        dbc.Col(width = 1),
                        dbc.Col(dash_table.DataTable(
                            data=df.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df.columns],
                            fixed_rows={'headers': True},
                            style_table={'height': 200,'marginLeft': 'auto', 'marginRight': 'auto'},  # defaults to 500
                        )),
                        dbc.Col(width = 2),
                        ]),
                    html.Div(
                        [
                        ]
                        ),
                        html.Br(),
                        dbc.Col(width=1),
                    ],
                ),
            ],
        
        ),style={"height": "42vw", "width": "98vw", "justifyContent": "center"},
       
    )
)

layout = html.Div([
    dbc.Container([
       generateActivityLog()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])
