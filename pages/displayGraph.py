import dash
import dash_bootstrap_components as dbc
from dash import  html
from .  import eventNavbar
import dash_cytoscape as cyto
from dash import Input, Output, html,callback,State
import projectManager




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
                         ])
                         ),
                          html.Div([cyto.Cytoscape(id='cytoscape-two-nodes',layout={'name': 'preset'},style={'width': '100%', 'height': '400px'},elements=[])],id = "graphDisplayer"),

                dbc.Col([html.Div(html.P("",id = "node-info"))],width=4),

            


            ],
        
        ),style=eventNavbar.CONTENT_STYLE,
       
    )
)
@callback(
    Output("node-info", "children"),
    [Input("cytoscape-two-nodes", "tapNode")]
)
def update_node_info(selected_node):
    if selected_node:
        return f"Selected Node: {selected_node['data']['label']}"
    else:
        return "No node selected"

@callback(
    Output("graphDisplayer", "children"),
    [Input("page-content", "id")],
    [State('selected-project-store', 'data')]
)
def createGraphOnPageLoad(dummyData,projectId):
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
def exportGraphPositions(n_clicks, elements):
    if n_clicks:
        print(elements)
    return ""

@callback(
    Output("cytoscape-two-nodes", "elements"),
    [Input("addEdge", "n_clicks")],
    [State("cytoscape-two-nodes", "selectedNodeData"),State("cytoscape-two-nodes", "elements")] 
)
def add_edge(n_clicks, tap_node, elements):
    print("IM TRIGGERED")
    if n_clicks and tap_node and len(tap_node) == 2:
        node1_id = tap_node[0]['id']
        node2_id = tap_node[1]['id']
        new_edge = {'data': {'source': node1_id, 'target': node2_id}}
        elements.append(new_edge)
        return elements
    return dash.no_update #makes it so that elemets isint wiped on reload
 

layout = html.Div([
    html.Div(id = "export-message"),
    html.Br(),
    eventNavbar.eventSidebar,
    generateSyncCard()
])

