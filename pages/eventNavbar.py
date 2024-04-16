import dash
import dash_bootstrap_components as dbc
from dash import html

# styke and navbar used all over the program
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


CONTENT_STYLE = {
    "margin-left": "14rem",
    "margin-right": "2rem",
     "margin-top": "8rem",
    "padding": "2rem 1rem",
    "height" : "42rem"
}

eventSidebar = html.Div(
    [
        html.P(""),
        html.Hr(),
        html.P(""),
        dbc.Nav(
            [
                dbc.NavLink("Events", href="/displayEvents", active="exact"),
                dbc.NavLink("Event Graph", href="/displayGraph", active="exact"),
                dbc.NavLink("Icon Library", href="/iconLibrary", active="exact"),
                dbc.NavLink("Save Project", href="/page-2", active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
