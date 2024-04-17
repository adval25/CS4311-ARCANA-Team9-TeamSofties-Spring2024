import dash
import dash_bootstrap_components as dbc
from dash import  html
from .  import eventNavbar
import dash_cytoscape as cyto
from dash import Input, Output, html,callback,State
import projectManager
import eventManager
import graphManager
import nodeManager
from datetime import datetime
import nodeIconDropDown




dash.register_page(__name__, path='/displayGraph')

sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

def editNodeModal(eventDic = {}):
    team_options = ["White", "Red", "Blue"]
    event_node_icons_options = {
        "White": "eventNodeIcon.png",
        "Red": "eventNodeIcon.png",
        "Blue": "eventNodeIcon.png",
    }
    if "nodeTimeStamp" in eventDic:
        nodeTimeStamp = eventDic.get("nodeTimeStamp")
        if len(nodeTimeStamp) == 15:  # Check if the string has no seconds
            nodeTimeStamp += ":00"  # Add seconds
        nodeTimeStamp = datetime.strptime(nodeTimeStamp,'%m/%d/%Y %H:%M:%S')
    else:
        nodeTimeStamp = datetime.now()
    return  html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Edit Node")),
                dbc.ModalBody(
                    [
                        html.P("eventTimeStamp"),
                        dbc.Form(
                        [
                        dbc.Input(type="date", id="editnodeTimeStamp",value = nodeTimeStamp.date()),
                        dbc.Row([
                            dbc.Col(dbc.Input(id='editnodehour', type="number", min=0, max=24, placeholder='Hour', style={"margin-bottom": "10px"},value = nodeTimeStamp.hour), width=3),
                            dbc.Col(dbc.Input(id='editnodeminute', type='number', min=0, max=60, placeholder='Minute', style={"margin-bottom": "10px"},value = nodeTimeStamp.minute), width=3),
                            dbc.Col(dbc.Input(id='editnodesecond', type='number', min=0, max=59, placeholder='Second', style={"margin-bottom": "10px"},value = nodeTimeStamp.second), width=3)
                            ])
                        ]),
                        html.Br(),
                        dbc.Row(
                        [
                        dbc.Col([html.P("Team*"),dbc.Select(options=[{"label": i, "value": i} for i in team_options],value=eventDic.get("nodeTeam"," "),id = "editteamInputs",),], width =3 ),
                        dbc.Col([html.P("eventLocation"),dbc.Input(type="posture", id = "editeventLocation",value=eventDic.get("nodePosture"," ")),], width = 3),
                        dbc.Col([html.P("malformed"),dbc.Checkbox(id="editmalformedInputs", value=eventDic.get("malformed"," ")),], width = 3),
                        
                        ], className="g-3"),
                        
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Source Host")),
                                dbc.Col(html.P("Target Host")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="0.0.0.0",value=eventDic.get("nodeSourceHost"," "),id = "editsourceHostInputs")))))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="0.0.0.0", id = "edittargetHostInputs",value=eventDic.get("nodetargetHost"," "))))))),
                            ]
                        ),
                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Intials")),
                                dbc.Col(html.P("Vector Id")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="|||",id = "editintialsInputs",value=eventDic.get("nodeIntials"," "))),width =8)))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="", id = "editvectorIdInputs",value=eventDic.get("nodeVectorId"," "))))))),
                            ]
                        ),

                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Description")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(placeholder="",id = "editdescriptionInputs",value=eventDic.get("nodeDescription"," "),style={"height": "100px"})),)))),
                            ]
                        ),
                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Node Icon")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(nodeIconDropDown.nodeIconDropDownMaker('graphNodeIconDropDown')),)))),
                                html.Div(dbc.Input(id='nodeId', type='text', value=""),style={'display': 'none'})

                            ]
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="editCloseNodeModalButton", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Edit Node", size = "lg", color="primary", id="editNodeModalButton", className="ms-auto",n_clicks=0)),
                            ]
                        ),
                    ],
                ),
                dbc.ModalFooter(
                    [
                        
                    ]
                ),
            ],
            id = "editNodeModal",
            is_open = False,
        ),
    ]
   
    )

def addNodeModal(eventDic = {}):
    team_options = ["White", "Red", "Blue"]
    event_node_icons_options = {
        "White": "eventNodeIcon.png",
        "Red": "eventNodeIcon.png",
        "Blue": "eventNodeIcon.png",
    }
    if "nodeTimeStamp" in eventDic:
        nodeTimeStamp = eventDic.get("nodeTimeStamp")
        if len(nodeTimeStamp) == 15:  # Check if the string has no seconds
            nodeTimeStamp += ":00"  # Add seconds
        nodeTimeStamp = datetime.strptime(nodeTimeStamp,'%m/%d/%Y %H:%M:%S')
    else:
        nodeTimeStamp = datetime.now()
    return  html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create Node")),
                dbc.ModalBody(
                    [
                        html.P("eventTimeStamp"),
                        dbc.Form(
                        [
                        dbc.Input(type="date", id="nodeTimeStamp",value = nodeTimeStamp.date()),
                        dbc.Row([
                            dbc.Col(dbc.Input(id='nodehour', type="number", min=0, max=24, placeholder='Hour', style={"margin-bottom": "10px"},value = nodeTimeStamp.hour), width=3),
                            dbc.Col(dbc.Input(id='nodeminute', type='number', min=0, max=60, placeholder='Minute', style={"margin-bottom": "10px"},value = nodeTimeStamp.minute), width=3),
                            dbc.Col(dbc.Input(id='nodesecond', type='number', min=0, max=59, placeholder='Second', style={"margin-bottom": "10px"},value = nodeTimeStamp.second), width=3)
                            ])
                        ]),
                        html.Br(),
                        dbc.Row(
                        [
                        dbc.Col([html.P("Team*"),dbc.Select(options=[{"label": i, "value": i} for i in team_options],value=eventDic.get("nodeTeam"," "),id = "teamInputs",),], width =3 ),
                        dbc.Col([html.P("eventLocation"),dbc.Input(type="posture", id = "eventLocation",value=eventDic.get("nodePosture"," ")),], width = 3),
                        dbc.Col([html.P("malformed"),dbc.Checkbox(id="malformedInputs", value=eventDic.get("malformed"," ")),], width = 3),
                        
                        ], className="g-3"),
                        
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Source Host")),
                                dbc.Col(html.P("Target Host")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="0.0.0.0",value=eventDic.get("nodeSourceHost"," "),id = "sourceHostInputs")))))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="0.0.0.0", id = "targetHostInputs",value=eventDic.get("nodetargetHost"," "))))))),
                            ]
                        ),
                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Intials")),
                                dbc.Col(html.P("Vector Id")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="|||",id = "intialsInputs",value=eventDic.get("nodeIntials"," "))),width =8)))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Text", placeholder="", id = "vectorIdInputs",value=eventDic.get("nodeVectorId"," "))))))),
                            ]
                        ),

                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Description")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(placeholder="",id = "descriptionInputs",value=eventDic.get("nodeDescription"," "),style={"height": "100px"})),)))),
                            ]
                        ),
                        html.Br(),
                         dbc.Row(
                            [
                                dbc.Col(html.P("Node Icon")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(nodeIconDropDown.nodeIconDropDownMaker('addGraphNodeIconDropDown')),)))),
                            ]
                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="closeNodeModalButton", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Create Node", size = "lg", color="primary", id="createNodeModal", className="ms-auto",n_clicks=0)),
                            ]
                        ),
                    ],
                ),
                dbc.ModalFooter(
                    [
                        
                    ]
                ),
            ],
            id = "addNodeModal",
            is_open = False,
        ),
    ]
   
    )

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
                         dbc.Button("Save Event Graph", color="primary", className="me-1",size="md", id = "exportButton"),
                         dbc.Button("Add Edge", color="primary", className="me-1",size="md", id = "addEdge"),
                         dbc.Button("Delete Edge", color="primary", className="me-1",size="md", id = "deleteEdge"),
                         dbc.Button("Delete Node", color="primary", className="me-1",size="md", id = "deleteNode"),
                         dbc.Button("Add Node", color="primary", className="me-1",size="md", id = "addNode"),
                         dbc.Button("Edit Node", color="primary", className="me-1",size="md", id = "editNode"),
                         dbc.Button("Export Graph", color="primary", className="me-1",size="md", id = "exportGraph"),


                         ])
                         ),
                          html.Div([cyto.Cytoscape(id='eventGraphGui',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},elements=[])],id = "graphDisplayer"),

                dbc.Col([html.Div(id = "node-info")],width=12),

            


            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)
@callback(
    Output("addNodeModal", "is_open",allow_duplicate=True),
    [Input("addNode", "n_clicks"), Input("closeNodeModalButton", "n_clicks")],
    [State("addNodeModal", "is_open"),State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def toggle_modal(add_node_clicks, close_clicks, is_open,projectId):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if button_id == "addNode":
            return True
        elif button_id == "closeNodeModalButton":
            return False
    return is_open

@callback(
    Output("node-info", "children"),
    [Input("eventGraphGui", "tapNode")],
    [State('selected-project-store', 'data')]

)
def update_node_info(selected_node,projectId):
    if selected_node:
        node = graphManager.getNode(selected_node['data']['id'],projectId)
        return [html.P(f"Node: {selected_node['data']['label']} TimeStamp: {node.getNodeTimeStamp()}"),
                html.P(f"Vector Id: {node.getNodeVectorId()}  Location: {node.getNodeLocation()}"),
                html.P(f"Description: {node.getNodeDescription()}"),
                 html.P(f"Source Host: {node.getSourceHost()} Target Host:{node.getTargerHost()}")
                 
                 ]
    else:
        return "No node selected"

@callback(
    Output("graphDisplayer", "children"),
    [Input("page-content", "id")],
    [State('selected-project-store', 'data')]
)
def createGraphOnPageLoad(dummyData,projectId): #loads all the graph on page load put code into method FIX ME !
    print("Creating graph on page load...")
    project = projectManager.getProject(projectId)
    nodeGraph = project.getEventGraph()
    nodeDict = nodeGraph.getDictOfNodes()
    graphElementList = graphManager.createGraphGUIElements(nodeDict)
    return [cyto.Cytoscape(id='eventGraphGui',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},
                           elements = graphElementList, stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)',
                    'width': 90,
                    'height': 80,
                    'background-fit': 'cover',
                    'background-image': 'data(url)',
                    'border-color': '#000',
                    'border-width': 1
                    
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': 'gray',  # Apply the same line color to all edges
                    'target-arrow-color': 'gray',  # Apply arrow color
                    'target-arrow-shape': 'triangle',  # Apply arrow shape
                    'curve-style': 'bezier'  # Adjust curve style if needed
                }
            },
                {
                'selector': 'node:selected',
                'style': {
                    'overlay-color': 'blue',
                    'overlay-opacity': 0.5
                }
            },
            ])
            ]

@callback(
    Output("export-message", "children", allow_duplicate=True),
    [Input("exportButton", "n_clicks")],
    [State("eventGraphGui", "elements"),State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def exportGraphPositions(n_clicks, elements,projectId): #pulls all the info from the graph
    if n_clicks:
        graphManager.saveNodePositions(elements,projectId)
    return ""

@callback(
    Output("eventGraphGui", "elements", allow_duplicate=True),
    [Input("addEdge", "n_clicks")],
    [State("eventGraphGui", "selectedNodeData"), State("eventGraphGui", "elements"), State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def add_edge(add_clicks, tap_node, elements, projectId):
    if not add_clicks or not tap_node or len(tap_node) != 2:
        raise dash.exceptions.PreventUpdate

    new_edge = nodeManager.addEdgeToGui(tap_node[0]["id"], tap_node[1]["id"])
    elements.append(new_edge)
    nodeManager.addEdgeToNode(projectId, tap_node[0]["id"], tap_node[1]["id"])

    return elements

@callback(
    Output("eventGraphGui", "elements", allow_duplicate=True),
    [Input("deleteEdge", "n_clicks")],
    [State("eventGraphGui", "elements"), State("eventGraphGui", "tapEdge"), State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def delete_edge(delete_clicks, elements, tap_edge, projectId):
    if not delete_clicks or not tap_edge:
        raise dash.exceptions.PreventUpdate

    elements.remove({"data": tap_edge["data"]})
    nodeManager.deleteEdge(projectId, tap_edge["data"]["source"], tap_edge["data"]["target"])

    return elements

@callback(
    Output("eventGraphGui", "elements", allow_duplicate=True),
    [Input("deleteNode", "n_clicks")],
    [State("eventGraphGui", "elements"), State("eventGraphGui", "selectedNodeData"), State('selected-project-store', 'data')],
    prevent_initial_call=True
)
def delete_node(delete_clicks, elements, tap_node, projectId):
    if delete_clicks:
        elements = nodeManager.deleteNodeFromGui(elements, tap_node[0]["id"])
        nodeManager.deleteNode(projectId, tap_node[0]["id"])
        return elements
    return dash.exceptions.PreventUpdate

@callback(
    [Output("eventGraphGui", "elements",allow_duplicate=True),Output("addNodeModal", "is_open",allow_duplicate=True)],
    [Input("createNodeModal", "n_clicks")],
    [
        State("eventGraphGui", "elements"),
        State('selected-project-store', 'data'),
        State('nodeTimeStamp', 'value'),
        State('nodehour', 'value'),
        State('nodeminute', 'value'),
        State('nodesecond', 'value'),
        State('malformedInputs', 'value'),
        State('intialsInputs', 'value'),
        State('vectorIdInputs', 'value'),
        State('sourceHostInputs', 'value'),
        State('targetHostInputs', 'value'),
        State('teamInputs','value'),
        State('descriptionInputs','value'),
        State('eventLocation', 'value'),
        State("addGraphNodeIconDropDown", "value"),
     ]
    
    ,
    prevent_initial_call=True
)
def add_node_modal(create_clicks, elements,projectId,eventDate,nodehour,nodeminute,nodesecond, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,eventIcon):
    if not create_clicks:
        raise dash.exceptions.PreventUpdate
    
    eventDateTime = datetime.strptime(f"{eventDate} {nodehour}:{nodeminute}:{nodesecond}", '%Y-%m-%d %H:%M:%S') #date passes back as YMD we need it as MDY
    eventTimeStamp = eventDateTime.strftime('%m/%d/%Y %H:%M:%S')
    event = eventManager.createEvent(eventTimeStamp, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,eventLocation,"",eventIcon)
    eventManager.addEventToProject(projectId,event)
    node = nodeManager.createNode(projectId,event)
    graphManager.addNodeToGraph(node,projectId)
    new_node = {"data": {"id": node.getNodeId(), "label": node.getNodeLabel(),'url': 'url(/assets/NodeIcons/'+node.getNodeIcon()+')'}}
    elements.append(new_node)

    return elements,False
@callback(
    [Output("editNodeModal", "is_open",allow_duplicate=True),
     Output("editnodeTimeStamp", "value"),
     Output("editnodehour", "value"),
     Output("editnodeminute", "value"),
     Output("editnodesecond", "value"),
     Output("editteamInputs", "value"),
     Output("editeventLocation", "value"),
     Output("editmalformedInputs", "value"),
     Output("editsourceHostInputs", "value"),
     Output("edittargetHostInputs", "value"),
     Output("editintialsInputs", "value"),
     Output("editvectorIdInputs", "value"),
     Output("editdescriptionInputs", "value"),
     Output("graphNodeIconDropDown", "value"),
     Output("nodeId","value")
     ],
    [Input("editNode", "n_clicks"),Input("editCloseNodeModalButton", "n_clicks")],
    [State("eventGraphGui", "selectedNodeData"), State('selected-project-store', 'data')],
     prevent_initial_call=True

)
def toggleEditmodal(edit_clicks, close_clicks,selectedNode,projectId):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if button_id == "editNode":
            if(selectedNode != None and len(selectedNode) == 1):
                node = graphManager.getNode(selectedNode[0]["id"],projectId)
                node_info = node.nodeTodict()
                nodeTimeStamp = node.converTimeStampToDateTime()
                date = nodeTimeStamp.date() if nodeTimeStamp else None
                hour = nodeTimeStamp.hour if nodeTimeStamp else None
                minute = nodeTimeStamp.minute if nodeTimeStamp else None
                second = nodeTimeStamp.second if nodeTimeStamp else None
                return ( 
                True, date, hour,minute,second, node_info.get("nodeLabel", None),
                node_info.get("nodeLocation", None), node_info.get("nodeMalformed", None), node_info.get("nodeSourceHost", None), node_info.get("nodeTargetHost", None), 
                node_info.get("nodeInitals", None), node_info.get("nodeVectorId", None), node_info.get("nodeDescription", None), node_info.get("nodeIcon", None),node.getNodeId()
                )
    raise dash.exceptions.PreventUpdate

@callback(
    [Output("eventGraphGui", "elements",allow_duplicate=True),Output("editNodeModal", "is_open",allow_duplicate=True)],
    [Input("editNodeModalButton", "n_clicks")],
    [State("eventGraphGui", "elements"),
     State('selected-project-store', 'data'),
     State('nodeId', 'value'),
     State("editnodeTimeStamp", "value"),
     State("editnodehour", "value"),
     State("editnodeminute", "value"),
     State("editnodesecond", "value"),
     State("editmalformedInputs", "value"),
     State("editsourceHostInputs", "value"),
     State("edittargetHostInputs", "value"),
     State("editintialsInputs", "value"),
     State("editvectorIdInputs", "value"),
     State("editteamInputs", "value"),
     State("editdescriptionInputs", "value"),
     State("editeventLocation", "value"),
     State("graphNodeIconDropDown", "value"),

     ],
     prevent_initial_call=True
    
    )
def editNode(editNode,elements,projectId,nodeId,nodeDate,nodehour,nodeminute,nodesecond, malformedInputs,sourceHostInput,targetHostInput,intialsInput,vectorIdInput,teamInput,descriptionInput,nodeLocation,nodeIcon):
    if(editNode):
        if(nodeDate == None or nodehour == None or nodeminute == None):
            eventTimeStamp = ""
        else:
            eventDateTime = datetime.strptime(f"{nodeDate} {nodehour}:{nodeminute}:{nodesecond}", '%Y-%m-%d %H:%M:%S')
            eventTimeStamp = eventDateTime.strftime('%m/%d/%Y %H:%M:%S')
        previousEvent = eventManager.getEventFromProject(nodeId,projectId)
        event = eventManager.createEvent(eventTimeStamp, malformedInputs,intialsInput,vectorIdInput,sourceHostInput,targetHostInput,teamInput,descriptionInput,nodeLocation,previousEvent.getDataSource(),nodeIcon,nodeId)
        eventManager.addEventToProject(projectId,event)
        node = nodeManager.createNode(projectId,event)
        graphManager.addNodeToGraph(node,projectId)
        elements = graphManager.updateNodeLabel(elements,previousEvent,teamInput,nodeId,nodeIcon)
        return elements,False
    raise dash.exceptions.PreventUpdate


@callback(
    Output("eventGraphGui", "generateImage"),
    [
        Input("exportGraph", "n_clicks"),
    ])
def get_image(exportGraph):

    ctx = dash.callback_context
    if ctx.triggered:
        if ctx.triggered_id == "exportGraph":
            print("OOOO IMAGE OUT")
            action = "download"
            type = "jpg"
            return {
                'type':type,
                'action': action
                }
    raise dash.exceptions.PreventUpdate


layout = html.Div([
    html.Div(id = "dummy-divNodeSend"),
    html.Div(id = "export-message"),
    addNodeModal(),
    editNodeModal(),
    html.Br(),
    eventNavbar.eventSidebar,
    generateSyncCard()
])

