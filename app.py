import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],use_pages=True) #user pages = true allows it to be multipage IMPORTANT!

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("View Opened Project", href="#")),
        dbc.NavItem(dbc.NavLink("Sync Projects", href="/syncMenue")),
        dbc.NavItem(dbc.NavLink("Manage Projects", href="/manageProjects")),
        dbc.NavItem(dbc.NavLink("Home", href="/")), #temporary replace with image


    ],
    brand="ARCANA",
    brand_href="#",
    color="primary",
    dark=True,
    className="fixed-top",
)

app.layout = html.Div([
    navbar,
    dash.page_container,
])

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_2", "is_open"),
    [Input("open modal_2", "n_clicks"), Input("close modal_2", "n_clicks")],
    [State("modal_2", "is_open")],
)
def toggle_modal_2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_3", "is_open"),
    [Input("open modal_3", "n_clicks"), Input("close modal_3", "n_clicks")],
    [State("modal_3", "is_open")],
)
def toggle_modal_3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modal_4", "is_open"),
    [Input("open modal_4", "n_clicks"), Input("close modal_4", "n_clicks")],
    [State("modal_4", "is_open")],
)
def toggle_modal_4(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run(debug=True)
