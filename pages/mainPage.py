import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

dash.register_page(__name__, path='/')

def menueCardCreator(title,icon):
    card = html.Div(
        dbc.Card(
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src= dash.get_asset_url(icon),
                            className="img-fluid rounded-start",
                            style={"width": "150px", "height": "90px"},
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H5(title, className=title,style={"fontSize": "40px"}),
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center", justify="center"), #centers the card
            className="w-75 mb-3 mx-auto clickable-card", #makes it clickable and sets its width
            style={"height": "100px"}  # Adjust maxWidth and height for card size

        )
    )
    return card

menueTitle =  html.Div(
    dbc.Row(
        dbc.Col(
  style={"fontSize": "30px", "color": "white", "fontFamily": "Arial, sans-serif", "marginRight": "100px"} 
         )
    )
)

layout = html.Div([
    dbc.Container([
       menueTitle,
       dcc.Link(menueCardCreator("Manage Projects","fileImage.png"), href="/manageProjects"),#set href to were the card redirects
       dcc.Link(menueCardCreator("Sync Projects","syncIcon.png"), href="/syncMenue"),
       dcc.Link(menueCardCreator("View User Activity Logs","activityLogs.png"), href="/viewUserActivityLog"),
       dcc.Link(menueCardCreator("Change Website Color","websiteColor.png"), href="/changeWebsiteColor")

    ], fluid=True, style={"backgroundColor": "#D3D3D3", "margin": "auto", "height": "100vh", "display": "flex", "flexDirection": "column", "justifyContent": "center"}) #justifyContent sets the content in the center of the screen
])
