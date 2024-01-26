import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],use_pages=True) #user pages = true allows it to be multipage IMPORTANT!


def menueCardCreator(title,icon):
    card = html.Div(
        dbc.Card(
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src=app.get_asset_url(icon),
                            className="img-fluid rounded-start",
                            style={"width": "150px", "height": "100px"},
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
            style={"height": "120px"}  # Adjust maxWidth and height for card size

        )
    )
    return card


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("View Opened Project", href="#")),
        dbc.NavItem(dbc.NavLink("Sync Projects", href="#")),
        dbc.NavItem(dbc.NavLink("Manage Projects", href="#")),
        dbc.NavItem(dbc.NavLink("Home", href="#")), #temporary replace with image


    ],
    brand="ARCANA",
    brand_href="#",
    color="primary",
    dark=True,
    className="fixed-top",
)

menueTitle =  html.Div(
    dbc.Row(
        dbc.Col(
  style={"fontSize": "30px", "color": "white", "fontFamily": "Arial, sans-serif", "marginRight": "100px"} 
         )
    )
)

app.layout = html.Div([
    navbar,
    dash.page_container,
])

if __name__ == '__main__':
    app.run(debug=True)