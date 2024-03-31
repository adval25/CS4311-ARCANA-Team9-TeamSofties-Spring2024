import dash
import dash_bootstrap_components as dbc
from dash import  html
from .  import eventNavbar
import dash_cytoscape as cyto
from dash import Input, Output, html,callback,State
import projectManager
import graphManager





dash.register_page(__name__, path='/displayGraph')

sortDropDown = [{"label": "TimeStamp", "value": "1"},{"label": "TargetHost", "value": "2"},]
logicDropDown = [{"label": "Logic", "value": "1"},{"label": "*", "value": "2"},]

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
                         ])
                         ),
                          html.Div([cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},elements=[])],id = "graphDisplayer"),

                dbc.Col([html.Div(id = "node-info")],width=12),

            


            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)
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
                html.P(f"Description: {node.getNodeDescription()}")
                 
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
    graphElementList = []
    for nodeId in nodeDict:
        node = nodeDict[nodeId]
        graphElement = {'data': {'id': node.getNodeId(), 'label': node.getNodeLabel()}, 'position': {'x': node.getNodeXPosition(), 'y': node.getNodeYPosition()}}
        graphElementList.append(graphElement)
    return [cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},
                           elements = graphElementList)
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
    [Input("addEdge", "n_clicks"),Input("deleteEdge", "n_clicks")],
    [State("cytoscape-two-nodes", "selectedNodeData"),State("cytoscape-two-nodes", "elements"),State("cytoscape-two-nodes", "tapEdge")] 
)
def edgeManager(add_clicks,delete_clicks, tap_node, elements,edge): 
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

    elif triggered_id == "deleteEdge" and delete_clicks:
        elements.remove({"data" :edge["data"]}) #formats the edge[data] to match the data in elements

    return elements

layout = html.Div([
    html.Div(id = "export-message"),
    html.Br(),
    eventNavbar.eventSidebar,
    generateSyncCard()
])

