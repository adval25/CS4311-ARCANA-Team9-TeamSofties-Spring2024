import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path='/changeWebsiteColor')

def generateChangeColorCard():
   
   return html.Div(
    dbc.Card(
        dbc.Row(
            id="control-card",
            children=[
                dbc.Col(width=1), #gives the card nice margins
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("websiteColor.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Change Website Color", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '50px'}),
                        html.Br(),
                        html.P("Select a color scheme if you would like to apply the color scheme permantly click save", style={"margin-left": 300,'display': 'inline-block' ,'padding-left': '50px'}),
                        html.Br(),
                         html.Img(
                        src=dash.get_asset_url("defaultColor.png"),
                        className="img-fluid rounded-start",
                        style={"padding-right": 220,"margin-left": 400}

                    ),
                     html.Img(
                        src=dash.get_asset_url("monoColor.png"),
                        className="img-fluid rounded-start",
                    ),
                    html.Div(
                        [
                            dbc.RadioItems(
                                options=[
                                    {"label": "Default Color Scheme", "value": 1},
                                    {"label": "Monochromatic Color Scheme", "value": 2},
                                ],
                                value=1,
                                id="radioitems-inline-input",
                                inline=True,
                                labelStyle={"margin-right":"auto","margin-left":"auto"},#creates space between the two tik boxes                    
                                ),
                        ],
                        style={"margin-left": "433px"},
                        ),

                        html.Br(),
                        html.Div(
                            dbc.Button("Save", color="primary", className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3"),
                            style={"margin-left": "60vw"},

                        ),
                        dbc.Col(width=1),
                    ],
                ),
            ],
        
        ), style={"paddingRight": "300px"},className="mx-auto" #card size
       
    )
)

layout = html.Div([
    dbc.Container([
       generateChangeColorCard()
    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh",  "display": "flex", "flexDirection": "column", "justifyContent": "center"}) 
])
