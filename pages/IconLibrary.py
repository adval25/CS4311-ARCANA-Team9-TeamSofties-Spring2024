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


def editIconModal():
   return html.Div(
        [
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Edit Icon Name")),
                    dbc.ModalBody(dbc.Input(type="text", id = "editIconName",)),
                    dbc.ModalFooter([
                        dbc.Button(
                            "Close", id="closeIconModal", className="ms-auto", n_clicks=0
                        ),
                        dbc.Button(
                            "Edit Icon Name", id="editIconNameModalButton", className="ms-auto", n_clicks=0
                        )]
                    ),
                ],
                id="editIconModal",
                is_open=False,
            ),
        ]
    )


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
                editIconModal(),
                html.Div(id="fileListDropDown", children=[nodeIconDropDown.nodeIconDropDownMaker('nodeIconDropDown')]),
                html.Div(id="displayDropDownImage"),
                html.Div(id='output-image-upload'),
                  html.Div(
                        [
                            dbc.Button("Edit Icon", color="primary", id="editIconButton"),
                            dbc.Button("Delete Icon", color="primary",id = "deleteIconButton"),
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
       html.Div(id="dummyDivIcons"),
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
        return children,nodeIconDropDown.nodeIconDropDownMaker('nodeIconDropDown')
    return dash.no_update,dash.no_update
    


def save_image(content, filename):
    _, content_string = content.split(',')
    image_data = base64.b64decode(content_string)
    node_icons_directory = os.path.join("assets", "NodeIcons")
    if not os.path.exists(node_icons_directory):
        os.makedirs(node_icons_directory)

    with open(os.path.join(node_icons_directory, filename), 'wb') as f:
        f.write(image_data)


@callback(Output('displayDropDownImage','children'),
          Input('nodeIconDropDown', 'value'),
          )
def displayNodeIcon(selectedImage):
    if selectedImage is not None:
        image_path = f"assets/NodeIcons/{selectedImage}"
        return html.Img(src=image_path, style={'width': '200px', 'height': 'auto'})

    return dash.no_update

@callback(
    Output('displayDropDownImage', 'children',allow_duplicate=True),
    [Input('deleteIconButton', 'n_clicks')],
    [State('nodeIconDropDown', 'value')],
    prevent_initial_call=True
)
def delete_image(n_clicks, selected_image):
    if n_clicks > 0 and selected_image is not None:
        # Delete the selected image file
        image_path = f"assets/NodeIcons/{selected_image}"
        if os.path.exists(image_path):
            os.remove(image_path)
        # Return an empty div after deleting the image
        return html.Div()
    else:
        return dash.no_update
    
@callback(
    [Output("editIconModal", "is_open"), Output("editIconName",'value')],
    [Input('editIconButton', 'n_clicks'),Input('closeIconModal', 'n_clicks')],
    [State("editIconModal", "is_open"),State('nodeIconDropDown', 'value'),],
)
def toggle_modal(edit_clicks,closeIconModal,is_open,dropDownValue):
    ctx = dash.callback_context
    if not ctx.triggered or dropDownValue == None:
        return dash.no_update,dash.no_update

    if ctx.triggered[0]['prop_id'].split('.')[0] == 'editIconButton':
        return not is_open,dropDownValue
    else:
        return False
    

@callback(
    Output("dummyDivIcons","children"),
    [Input("editIconNameModalButton","n_clicks")],
    [State('nodeIconDropDown', 'value'),
    State("editIconName",'value')]
)
def editNodeIconName(editButton,dropDownValue,editIconName):
    if editButton:
        if dropDownValue != None:
            old_path = f"assets/NodeIcons/{dropDownValue}"
            new_path = f"assets/NodeIcons/{editIconName}"
            os.rename(old_path, new_path)

    return dash.no_update
