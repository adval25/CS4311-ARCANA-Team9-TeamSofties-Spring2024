import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, html,callback,State,dcc
from .  import eventNavbar
import dash_ag_grid as dag
import base64
import os
import nodeIconDropDown


dash.register_page(__name__, path='/iconLibrary')
sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

def dropDownMaker(menueId,menueContent,marginRight):
    return dbc.Select(
    id=menueId,
    options=menueContent,
    size="md",
    style={'display': 'inline-block',"width" : "8rem","margin-right" : marginRight})

def uploadElement():
    return dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
        )

def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.Img(src=contents),
        html.Hr(),
    ])

def generatedisplayIconCard(): 
    filenames = os.listdir("NodeIcons") if os.path.isdir("NodeIcons") else []
    dropdown_options = [{'label': filename, 'value': filename} for filename in filenames]
    return html.Div(
    dbc.Card(
       
        dbc.Row(
            id="nodeIconContent",
            children=[
                dbc.Col(width=1), #gives the card nice margin
                dbc.Col(
                    children=[
                        html.Img(
                        src=dash.get_asset_url("IconLibrary.png"),
                        className="img-fluid rounded-start",
                        style={"width": "60px", "height": "60px","margin-right": 0,'display': 'inline-block', "margin-bottom" : "0%"}, #inline alows for the html to stack on one line
                        ), 
                        html.P("Icon Library", style={"font-size": "40px","margin-left": 0,'display': 'inline-block' ,'padding-left': '20px'}),  
                    ],
                ),
                html.Br(),
                uploadElement(),
                html.Div(id="fileListDropDown", children=[nodeIconDropDown.nodeIconDropDownMaker()]),
                html.Div(id='output-image-upload'),
                  html.Div(
                        [
                            dbc.Button("+ Create Event", color="primary",href = "/addEvent"),
                            dbc.Button("Edit Event", color="primary",href = "/editEvent"),
                            dbc.Button("Delete Event", color="primary",href = "/displayEvents",id = "deleteButton"),
                        ],
                        className="d-grid gap-2 d-md-flex justify-content-md-end position-absolute bottom-0 end-0 m-3",
                        ), 

            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)

def displayEventLayout():
    return html.Div([
    html.Div([dag.AgGrid(id ="SelectedRowEvent"),],id='dummy-div', style={'display': 'none'}), #this is here to prevent an error that selectedRow does not exist
    html.Br(),
    eventNavbar.eventSidebar,
    dbc.Container([
       generatedisplayIconCard(),
    ], fluid=True,  className="mx-auto") 
])



layout = displayEventLayout

@callback([Output('output-image-upload', 'children'),Output('fileListDropDown','children')],
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        
        for content, filename in zip(list_of_contents, list_of_names):
            save_image(content, filename)
        return children,nodeIconDropDown.nodeIconDropDownMaker()
    return dash.no_update,dash.no_update
    


def save_image(content, filename):
    # Decode base64 image data
    _, content_string = content.split(',')
    image_data = base64.b64decode(content_string)
    
    # Create the NodeIcons directory if it doesn't exist
    directory = "NodeIcons"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Save the image as a PNG file in the NodeIcons directory
    with open(os.path.join(directory, filename), 'wb') as f:
        f.write(image_data)