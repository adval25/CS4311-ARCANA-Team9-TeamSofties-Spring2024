import dash
import dash_bootstrap_components as dbc
from dash import  html
from .  import eventNavbar
import dash_cytoscape as cyto
from dash import Input, Output, html,callback,State
import projectManager
import graphManager
import nodeManager




dash.register_page(__name__, path='/displayGraph')

sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

addNodeModal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Create Project")),
                dbc.ModalBody(
                    [
                        html.P("Project Name"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Project Name", placeholder="Project Name", id = "projectName" )),width = 12),)
                        ),
                        html.Br(),
                        html.P("Project Location"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="datetime-local", placeholder=":", id = "projectLocation")),width = 12),)
                        ),
                        html.Br(),
                        html.P("Log Location"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Log Directory", placeholder="Log Directory" , id = "logDirectory")),width = 12),)
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Start Date")),
                                dbc.Col(html.P("End Date")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="Start Date", placeholder="mm/dd/yyyy")))))),
                                dbc.Col(dbc.Form(dbc.Row(dbc.Col(html.Div(dbc.Input(type="End Date", placeholder="mm/dd/yyyy")))))),
                            ]
                        ),
                        html.Br(),
                        html.P("Initials"),
                        dbc.Form(
                            dbc.Row(dbc.Col(html.Div(dbc.Input(type="Initials", placeholder="III", id = "analystInitals")),width = 6),)
                        ),
                        
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Cancel", size = "lg", color="secondary", id="closeNodeModalButton", className="ms-auto", n_clicks=0)),
                                dbc.Col(dbc.Button("Create Project", size = "lg", color="primary", id="createProject", className="ms-auto", href="/manageProjects",n_clicks=0)),
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
                         dbc.Button("Export Event Graph", color="primary", className="me-1",size="md", id = "exportButton"),
                         dbc.Button("Add Edge", color="primary", className="me-1",size="md", id = "addEdge"),
                         dbc.Button("Delete Edge", color="primary", className="me-1",size="md", id = "deleteEdge"),
                         dbc.Button("Delete Node", color="primary", className="me-1",size="md", id = "deleteNode"),
                         dbc.Button("Add Node", color="primary", className="me-1",size="md", id = "addNode"),


                         ])
                         ),
                          html.Div([cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},elements=[])],id = "graphDisplayer"),

                dbc.Col([html.Div(id = "node-info")],width=12),

            


            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)
@callback(
    Output("addNodeModal", "is_open"),
    [Input("addNode", "n_clicks"), Input("closeNodeModalButton", "n_clicks")],
    [State("addNodeModal", "is_open")]
)
def toggle_modal(add_node_clicks, close_clicks, is_open):
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
    [Input("cytoscape-two-nodes", "tapNode")],
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
    graphElementList = graphManager.createGraphElements(nodeDict)
    return [cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},
                           elements = graphElementList, stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(label)'
                    
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': 'red',  # Apply the same line color to all edges
                    'target-arrow-color': 'blue',  # Apply arrow color
                    'target-arrow-shape': 'triangle',  # Apply arrow shape
                    'curve-style': 'bezier'  # Adjust curve style if needed
                }
            }
            ])
            ]

@callback(
    Output("export-message", "children"),
    [Input("exportButton", "n_clicks")],
    [State("cytoscape-two-nodes", "elements")]
)
def exportGraphPositions(n_clicks, elements): #pulls all the info from the graph
    if n_clicks:
        print(elements)
    return ""

@callback(
    Output("cytoscape-two-nodes", "elements"),
    [Input("addEdge", "n_clicks"),Input("deleteEdge", "n_clicks"),Input("deleteNode", "n_clicks"),Input("addNode", "n_clicks")],
    [State("cytoscape-two-nodes", "selectedNodeData"),State("cytoscape-two-nodes", "elements"),State("cytoscape-two-nodes", "tapEdge"),State('selected-project-store', 'data')] 
)
def edgeManager(add_clicks,deleteEdgeclicks,deleteNode,addNode,tap_node, elements,edge,projectId): 
    ctx = dash.callback_context
    if not ctx.triggered: 
        raise dash.exceptions.PreventUpdate

    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0] #stops the input from spilling over

    if triggered_id == "addEdge" and add_clicks:
        if tap_node and len(tap_node) == 2:
            node1_id = tap_node[0]["id"]
            node2_id = tap_node[1]["id"]
            new_edge = {"data": {"source": node1_id, "target": node2_id}}
            elements.append(new_edge)
            nodeManager.addEdgeToNode(projectId,tap_node[0]["id"],tap_node[1]["id"])

    elif triggered_id == "deleteEdge" and deleteEdgeclicks:
        elements.remove({"data" :edge["data"]}) #formats the edge[data] to match the data in elements
        print(edge["data"])
        nodeManager.deleteEdge(projectId,edge["data"]["source"],edge["data"]["target"])
    
    elif triggered_id == "deleteNode" and deleteNode:
        if tap_node and len(tap_node) == 1:
            node_id = tap_node[0]["id"]
            elements = [e for e in elements if "source" not in e["data"] or e["data"]["source"] != node_id]
            elements = [e for e in elements if "target" not in e["data"] or e["data"]["target"] != node_id]
            elements = [e for e in elements if e.get("data", {}).get("id") != node_id]
            nodeManager.deleteNode(projectId,node_id)
    
    elif triggered_id == "addNode" and addNode:
        #new_node_id = str(uuid.uuid4())
        new_node = {"data": {"id": "TSA", "label": "New Node"}}
        elements.append(new_node)

    return elements

layout = html.Div([
    html.Div(id = "export-message"),
    addNodeModal,
    html.Br(),
    eventNavbar.eventSidebar,
    generateSyncCard()
])

